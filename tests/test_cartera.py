import pytest
import pandas as pd
from cartera import simular_inversion

def test_simular_inversion_matematica_precisa():
    """
    Simula 5 días de trading estructurado para comprobar 
    matemáticamente cada céntimo.
    
    Día 1: Precio 10, Señal 0. Nada cambia (100€ líquidos).
    Día 2: Precio 20, Señal 1. Compra acciones (5 acciones). Capital Líquido 0. Valor Total: 100€
    Día 3: Precio 25, Señal 0. Nada cambia (5 acciones). Capital Líquido 0. Valor Total: 125€
    Día 4: Precio 10, Señal -1. Vende todo (5 * 10 = 50€). Capital Líquido 50. Valor Total 50€
    Día 5: Precio 15, Señal 0. Nada cambia. Capital líquido 50. Valor Total 50€
    """
    
    datos = {
        'Close': [10.0, 20.0, 25.0, 10.0, 15.0],
        'Señal': [0, 1, 0, -1, 0]
    }
    df = pd.DataFrame(datos)
    
    resultado = simular_inversion(df)
    valores_esperados = [100.0, 100.0, 125.0, 50.0, 50.0]
    
    for i, esperado in enumerate(valores_esperados):
        assert abs(resultado.iloc[i]['Valor_Cartera'] - esperado) < 0.001

def test_multiples_compras_sin_fondos():
    """
    Verifica que la señal "1" (Compra) sea ignorada si ya invertimos el capital.
    """
    datos = {
        'Close': [5.0, 10.0, 20.0],
        'Señal': [1, 1, 1] # 3 compras seguidas
    }
    df = pd.DataFrame(datos)
    resultado = simular_inversion(df)
    
    # Día 1: Compra 20 acciones (100 / 5)
    # Día 2: Señal 1, pero 0 liquidez -> Ignorado. Valor cartera = 20 * 10 = 200
    # Día 3: Señal 1, pero 0 liquidez -> Ignorado. Valor cartera = 20 * 20 = 400
    
    assert abs(resultado.iloc[-1]['Valor_Cartera'] - 400.0) < 0.001

def test_multiples_ventas_sin_acciones():
    """
    Verifica que la señal "-1" (Venta) sea anulada si no existen acciones poseídas.
    """
    datos = {
        'Close': [10.0, 5.0, 50.0],
        'Señal': [-1, -1, -1] # 3 ventas seguidas
    }
    df = pd.DataFrame(datos)
    resultado = simular_inversion(df)
    
    # Como nunca compró, su valor sigue siendo 100 líquidos constantemente.
    assert resultado['Valor_Cartera'].iloc[0] == 100.0
    assert resultado['Valor_Cartera'].iloc[-1] == 100.0
