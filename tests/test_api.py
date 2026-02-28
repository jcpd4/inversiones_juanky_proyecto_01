from fastapi.testclient import TestClient
from api import app
from unittest.mock import patch
import pandas as pd

# Inicializar cliente de pruebas
client = TestClient(app)

def test_api_html_valido():
    """Verifica que el index.html se sirve correctamente en la raíz."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Trading Bot" in response.text

@patch('api.ejecutar_bot')
def test_api_simulate_success(mock_ejecutar):
    """Verifica el endpoint /api/simulate de forma aislada (Mockeando el bot)."""
    
    # Preparamos un mock muy controlado de lo que "ejecutar_bot" debería devolver
    mock_df = pd.DataFrame({
        'Close': [150.0, 155.0],
        'SMA_14': [100.0, 101.0],
        'SMA_50': [120.0, 120.5],
        'Señal': [0, 1],
        'Valor_Cartera': [100.0, 100.0]
    }, index=pd.date_range("2024-01-01", periods=2))
    
    mock_ejecutar.return_value = mock_df
    
    # Ejecutamos la llamada HTTP
    response = client.get("/api/simulate?ticker=MOCK")
    
    assert response.status_code == 200
    data = response.json()
    
    # Validaciones del payload JSON
    assert data["ticker"] == "MOCK"
    assert data["capital_inicial"] == 100.0
    assert data["capital_final"] == 100.0
    assert data["rentabilidad"] == 0.0
    
    # Validaciones estructurales de los arrays
    assert len(data["fechas"]) == 2
    assert len(data["valores_cartera"]) == 2
    assert data["senales"] == [0, 1]

@patch('api.ejecutar_bot')
def test_api_simulate_ticker_invalido(mock_ejecutar):
    """Verifica que si el bot falla (ej. ticker no existe), devuelve un error 400 controlado."""
    mock_ejecutar.side_effect = Exception("No data found for invalid ticker.")
    
    response = client.get("/api/simulate?ticker=INVALID")
    
    assert response.status_code == 400
    assert "No data found for invalid ticker" in response.json()["detail"]
