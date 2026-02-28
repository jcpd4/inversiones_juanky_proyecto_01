import yfinance as yf
import pandas as pd

def escanear_subidas(ticker: str, periodo: str, porcentaje_objetivo: float) -> list[dict]:
    """
    Descarga el historial de un activo durante el periodo especificado y calcula 
    los días en donde el incremento porcentual respecto al cierre anterior 
    haya sido mayor o igual al porcentaje objetivo.

    Args:
        ticker (str): Símbolo financiero (ej. AAPL).
        periodo (str): Rango de tiempo de yfinance (ej. '1mo', '1y', 'max').
        porcentaje_objetivo (float): Porcentaje mínimo de subida para registrar (ej. 2.0).

    Returns:
        List[dict]: Lista de eventos estructurada con fecha, porcentaje y precio de cierre.
    """
    print(f"🔎 Escaneando subidas de {ticker} ({periodo}) objetivo: {porcentaje_objetivo}%...")
    
    # Descargar datos
    data = yf.download(ticker, period=periodo, interval="1d", progress=False)
    
    if data.empty:
        return []
        
    # Arreglar posible MultiIndex (nuevo en yfinance al descargar un ticker individual)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(-1)
        
    # Calcular el cambio porcentual diario respecto al día anterior y pasarlo a % (x 100)
    data['Pct_Change'] = data['Close'].pct_change() * 100
    
    # Filtrar solo los días donde el cambio sea mayor o igual al objetivo (y eliminar NaN del primer día)
    subidas = data[data['Pct_Change'] >= porcentaje_objetivo].copy()
    
    # Construir la lista de resultados ordenados cronológicamente
    resultados = []
    
    for index, row in subidas.iterrows():
        resultados.append({
            "fecha": index.strftime('%Y-%m-%d'),
            "precio": round(float(row['Close']), 2),
            "porcentaje": round(float(row['Pct_Change']), 2)
        })
        
    return resultados
