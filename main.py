import yfinance as yf
import pandas as pd
from estrategia import aplicar_estrategia
from cartera import simular_inversion

def obtener_datos(simbolo: str) -> pd.DataFrame:
    """Descarga datos históricos de Yahoo Finance del último par de años."""
    print(f"⬇️ Descargando datos para: {simbolo}...")
    data = yf.download(simbolo, period="2y", interval="1d", progress=False)
    
    # IMPORTANTE: yfinance ahora devuelve un MultiIndex para las columnas al buscar
    # un solo Ticker. Si ocurre, aplanamos el DataFrame quedándonos con el nivel 'Price'
    if isinstance(data.columns, pd.MultiIndex):
        # Aplanamos el DataFrame para quedarnos con el primer nivel de las columnas.
        # Por ejemplo de ('Close', 'AAPL') pasamos a simplemente 'Close'
        data.columns = data.columns.droplevel(-1)
        
    return data

def ejecutar_bot(ticker: str) -> pd.DataFrame:
    """
    Función principal que orquesta la descarga, estrategia y backtesting.
    Devuelve los datos simulados que incluyen el historial de la cartera.
    """
    # 1. Obtenemos datos brutos
    datos_brutos = obtener_datos(ticker)
    
    # 2. Aplicamos la estrategia (El cerebro)
    print("🧠 Calculando indicadores y señales...")
    datos_analizados = aplicar_estrategia(datos_brutos)
    
    # 3. Aplicamos el simulador de inversión (Backtesting)
    print("📈 Simulando inversión con 100€ iniciales...")
    datos_simulados = simular_inversion(datos_analizados)
    
    # 4. Calculamos resultados finales
    valor_final = float(datos_simulados['Valor_Cartera'].iloc[-1])
    rentabilidad = ((valor_final - 100) / 100) * 100
    
    # 5. Imprimimos los resultados de forma atractiva
    print("\n" + "="*40)
    print("💰 RESULTADO DEL BACKTESTING 💰")
    print("="*40)
    print(f"Activo Analizado : {ticker}")
    print(f"Capital Inicial  : 100.00 €")
    print(f"Capital Final    : {valor_final:.2f} €")
    print(f"Rentabilidad     : {rentabilidad:.2f} %")
    print("="*40 + "\n")
    
    return datos_simulados

if __name__ == "__main__":
    # Prueba inicial por defecto
    ticker = "AAPL"
    ejecutar_bot(ticker)