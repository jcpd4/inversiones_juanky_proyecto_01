from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
from main import ejecutar_bot

app = FastAPI(title="Trading Bot API", description="API para el simulador de inversiones basado en SMA")

# Modelo de datos para la respuesta de la API
class SimulationResponse(BaseModel):
    ticker: str
    capital_inicial: float
    capital_final: float
    rentabilidad: float
    fechas: list[str]
    valores_cartera: list[float]
    precios: list[float]
    sma_14: list[float]
    sma_50: list[float]
    senales: list[int]

@app.get("/api/simulate", response_model=SimulationResponse)
def simulate_trading(ticker: str):
    try:
        # Ejecutamos la lógica del bot usando el módulo ya existente
        df_simulados = ejecutar_bot(ticker)
        
        if df_simulados.empty:
            raise ValueError("No se obtuvieron suficientes datos.")
            
        # Reemplazar NaN por None (para que sea JSON-serializable y funcione en Javascript)
        df_simulados = df_simulados.where(pd.notnull(df_simulados), None)
        
        # Obtenemos los valores individuales para la gráfica Frontend
        valor_final = float(df_simulados['Valor_Cartera'].iloc[-1])
        rentabilidad = ((valor_final - 100) / 100) * 100
        
        # Convertimos las fechas (índices) a formato string (YYYY-MM-DD)
        fechas = [t.strftime('%Y-%m-%d') for t in df_simulados.index]
        valores_cartera = df_simulados['Valor_Cartera'].tolist()
        precios = df_simulados['Close'].tolist()
        sma_14 = df_simulados['SMA_14'].tolist()
        sma_50 = df_simulados['SMA_50'].tolist()
        senales = df_simulados['Señal'].tolist()
        
        return {
            "ticker": ticker.upper(),
            "capital_inicial": 100.0,
            "capital_final": round(valor_final, 2),
            "rentabilidad": round(rentabilidad, 2),
            "fechas": fechas,
            "valores_cartera": valores_cartera,
            "precios": precios,
            "sma_14": sma_14,
            "sma_50": sma_50,
            "senales": senales
        }
        
    except Exception as e:
        print(f"Error en simulación: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

# Servimos los archivos estáticos desde la carpeta "static"
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # Se recomienda ejecutar vía terminal: uvicorn api:app --reload
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
