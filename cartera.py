import pandas as pd

def simular_inversion(datos: pd.DataFrame) -> pd.DataFrame:
    """
    Simula una inversión iterando día a día sobre los datos históricos y las señales,
    comprando todo lo posible con la señal 1 y vendiendo todo con la señal -1.
    
    Args:
        datos (pd.DataFrame): DataFrame que incluye 'Close' y 'Señal'.
        
    Returns:
        pd.DataFrame: El DataFrame actualizado con la nueva columna 'Valor_Cartera'.
    """
    df = datos.copy()
    
    # Variables iniciales
    capital_inicial = 100.0
    dinero_disponible = capital_inicial
    acciones_poseidas = 0.0
    
    historial_valor_cartera = []
    
    # Usamos iterrows para la simulación día a día
    for indice, fila in df.iterrows():
        precio_actual = fila['Close']
        senal = fila['Señal']
        
        # Lógica de COMPRA
        if senal == 1 and dinero_disponible > 0:
            # Compramos todas las acciones posibles (permitimos fracciones para mayor precisión)
            acciones_compradas = dinero_disponible / precio_actual
            acciones_poseidas += acciones_compradas
            dinero_disponible = 0.0
            
        # Lógica de VENTA
        elif senal == -1 and acciones_poseidas > 0:
            # Vendemos todas las acciones que poseemos
            dinero_obtenido = acciones_poseidas * precio_actual
            dinero_disponible += dinero_obtenido
            acciones_poseidas = 0.0
            
        # Registrar el valor total de la cartera en este día
        valor_total = dinero_disponible + (acciones_poseidas * precio_actual)
        historial_valor_cartera.append(valor_total)
        
    # Añadimos el historial como una nueva columna al DataFrame
    df['Valor_Cartera'] = historial_valor_cartera
    
    return df
