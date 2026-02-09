import pandas as pd

def aplicar_estrategia(datos):
    """
    Recibe un DataFrame de yfinance, calcula medias móviles
    y genera una señal de compra (1) o venta (-1).
    """
    # Hacemos una copia para no alterar el original
    df = datos.copy()
    
    # 1. Calcular Medias Móviles Simples (SMA)
    # Si yfinance devuelve MultiIndex, a veces hay que especificar la columna con cuidado.
    # Usamos 'Close' que es el precio de cierre.
    df['SMA_14'] = df['Close'].rolling(window=14).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    
    # 2. Limpieza de datos
    # Las primeras 50 filas tendrán NaN (vacío) porque no hay suficientes datos para la media.
    # Las borramos.
    df.dropna(inplace=True)
    
    # 3. Generar la Señal
    # Creamos la columna 'Señal' llena de ceros
    df['Señal'] = 0
    
    # Condición de COMPRA (1): La media rápida (14) supera a la lenta (50)
    # Significa que el precio está subiendo con fuerza
    df.loc[df['SMA_14'] > df['SMA_50'], 'Señal'] = 1
    
    # Condición de VENTA (-1): La media rápida (14) cae por debajo de la lenta (50)
    # Significa que el precio está perdiendo fuerza
    df.loc[df['SMA_14'] < df['SMA_50'], 'Señal'] = -1
    
    return df