import pytest
import pandas as pd
from unittest.mock import patch
from scanner import escanear_subidas

@patch('scanner.yf.download')
def test_escanear_subidas(mock_download):
    # Crear un DataFrame ficticio para simular descargas de 5 días
    fechas = pd.date_range(start='2024-01-01', periods=5)
    
    # Precios donde el Día 2 sube un 10%, el Día 3 baja, el Día 4 sube un 5%, el Día 5 plano
    precios = [100.0, 110.0, 105.0, 110.25, 110.25]
    
    mock_df = pd.DataFrame({'Close': precios}, index=fechas)
    mock_download.return_value = mock_df
    
    # Buscar subidas del 5% o más
    resultados = escanear_subidas("TEST", "5d", 5.0)
    
    # Debería encontrar 2 eventos:
    # 2024-01-02: de 100 a 110 (+10%)
    # 2024-01-04: de 105 a 110.25 (+5%)
    assert len(resultados) == 2
    
    assert resultados[0]['fecha'] == "2024-01-02"
    assert resultados[0]['porcentaje'] == 10.0
    assert resultados[0]['precio'] == 110.0
    
    assert resultados[1]['fecha'] == "2024-01-04"
    assert resultados[1]['porcentaje'] == 5.0
    assert resultados[1]['precio'] == 110.25
