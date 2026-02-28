import pandas as pd

def aplicar_estrategia(datos: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe un DataFrame de precios históricos y aplica una estrategia basada en
    el cruce de Medias Móviles Simples (SMA).
    
    Args:
        datos (pd.DataFrame): DataFrame que contiene al menos la columna 'Close'.
        
    Returns:
        pd.DataFrame: Un DataFrame actualizado que incluye la media móvil corta ('SMA_14'), 
                      la media móvil larga ('SMA_50') y una columna 'Señal' (1 para compra, -1 para venta).
    """
    df = datos.copy()
    
    # 1. Calcular la Media Móvil Simple (SMA) de 14 y 50 días
    df['SMA_14'] = df['Close'].rolling(window=14).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    
    # 2. Limpiar los valores nulos generados por las medias móviles
    df.dropna(inplace=True)
    
    # 3. Crear la columna 'Señal'
    # 1 (Compra) cuando la SMA corta cruza por encima de la larga
    # -1 (Venta) cuando la SMA corta cruza por debajo de la larga
    df['Señal'] = 0
    df.loc[df['SMA_14'] > df['SMA_50'], 'Señal'] = 1
    df.loc[df['SMA_14'] < df['SMA_50'], 'Señal'] = -1
    
    return df