import yfinance as yf
from estrategia import aplicar_estrategia  # <-- Importamos tu nueva función

def obtener_datos(simbolo):
    print(f"⬇️ Descargando datos para: {simbolo}...")
    # Bajamos 2 años para asegurarnos de tener suficientes datos para la media de 50
    data = yf.download(simbolo, period="2y", interval="1d")
    return data

if __name__ == "__main__":
    ticker = "AAPL" # Apple
    
    # 1. Obtenemos datos brutos
    datos_brutos = obtener_datos(ticker)
    
    # 2. Aplicamos la estrategia (El cerebro)
    print("🧠 Calculando indicadores y señales...")
    datos_analizados = aplicar_estrategia(datos_brutos)
    
    # 3. Mostramos el resultado
    print("\n--- 📊 RESULTADO DEL ANÁLISIS ---")
    # Seleccionamos solo las columnas que nos interesan para ver
    columnas_clave = ['Close', 'SMA_14', 'SMA_50', 'Señal']
    
    # Mostramos las últimas 10 filas
    print(datos_analizados[columnas_clave].tail(10))