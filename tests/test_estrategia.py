import pytest
import pandas as pd
from estrategia import aplicar_estrategia

@pytest.fixture
def datos_mock():
    # Crear un DataFrame ficticio simulando una caída y luego una subida
    # para forzar cruces de medias (Death Cross y Golden Cross)
    fechas = pd.date_range(start='2024-01-01', periods=100)
    
    # 1. Los primeros 60 días el precio sube constantemente.
    #    Acá la SMA_14 estará por encima de la SMA_50 (Golden Cross inicial)
    # 2. Los siguientes 20 días el precio cae bruscamente.
    #    La SMA_14 debería cruzar abajo de la SMA_50 (Death Cross)
    # 3. Los últimos 20 días el precio vuelve a subir muy fuerte.
    #    La SMA_14 debería cruzar de nuevo arriba (Golden Cross)
    precios = []
    for i in range(100):
        if i < 60:
            precios.append(100 + i) 
        elif i < 80:
            precios.append(159 - ((i - 59) * 5)) 
        else:
            precios.append(59 + ((i - 79) * 8))

    df = pd.DataFrame({'Close': precios}, index=fechas)
    return df

def test_aplicar_estrategia_estructura(datos_mock):
    """Verifica que el output tenga la estructura y limpieza correcta."""
    resultado = aplicar_estrategia(datos_mock)
    
    # Después de las medias móviles, se pierden las primeras 49 filas por los NaN de la SMA_50
    assert len(resultado) == len(datos_mock) - 49
    
    # Verificar que las columnas esperadas existan
    expected_columns = ['Close', 'SMA_14', 'SMA_50', 'Señal']
    for col in expected_columns:
        assert col in resultado.columns
        
    # No debe haber nulos
    assert resultado.isnull().sum().sum() == 0

def test_aplicar_estrategia_senales(datos_mock):
    """Verifica que las señales 1 y -1 se generen correctamente en las zonas esperadas."""
    resultado = aplicar_estrategia(datos_mock)
    
    # Analizamos la tendencia para comprobar que el 1 y -1 funcionan.
    # Para la primera parte limpia (índices 49 al ~65) el mercado subía.
    assert resultado.iloc[0]['Señal'] == 1
    
    # Identificar si existe al menos una señal de venta (-1) en la caída 
    # y al menos una señal de compra (1) tras la recuperación.
    vende = (resultado['Señal'] == -1).any()
    compra = (resultado['Señal'] == 1).any()
    
    assert vende == True, "Debería haber generado al menos una señal de VENTA"
    assert compra == True, "Debería haber generado al menos una señal de COMPRA"
    
    # Verificar que nunca hay una señal distinta de 0, 1 o -1
    senales_invalidas = resultado[~resultado['Señal'].isin([0, 1, -1])]
    assert len(senales_invalidas) == 0
