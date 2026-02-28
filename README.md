# 📈 Bot de Trading & Simulador de Inversiones (Paper Trading)

## 📌 Descripción del Proyecto
Este proyecto es un **Bot de Inversión Algorítmica y Simulador de Paper Trading** en Python equipado con una **Interfaz Web Premium** (FastAPI + Vanilla JS/CSS). Diseñado como una herramienta robusta para realizar *backtesting* de estrategias de mercado, el ecosistema descarga el histórico de precios reales de Yahoo Finance, aplica algoritmos para buscar oportunidades de mercado y simula la compra/venta de posiciones.

El objetivo de esta herramienta es evaluar la rentabilidad teórica de un capital inicial (100€) asumiendo una operativa automatizada. 

## 🧠 Estrategia Implementada: Cruce de Medias Móviles (SMA)
El "cerebro" del bot toma sus decisiones basado en una de las estrategias clásicas y más reconocidas del análisis técnico: **El Cruce de Medias Móviles Simples (SMA)**.

1. **SMA Rápida (14 días)**: Reacciona de forma veloz a los cambios recientes de precio.
2. **SMA Lenta (50 días)**: Indica la tendencia general subyacente del mercado en el mediano plazo.
   
**Señales de Trading Generadas**:
- 🟢 **Señal de Compra (Golden Cross / 1)**: Se activa cuando la media rápida de 14 días cruza por encima de la media lenta de 50 días. Esto indica un impulso alcista. El bot invierte automáticamente el capital líquido disponible asumiendo una tendencia al alza.
- 🔴 **Señal de Venta (Death Cross / -1)**: Se activa cuando la media rápida cruza por debajo de la lenta. Esto señala debilidad y un posible cambio a tendencia bajista. El bot vende la totalidad de las acciones para asegurar y proteger el capital.

## 🛠 Requisitos Previos e Instalación
- Python 3.9 o superior.
- `pip` (Gestor de paquetes de Python).
- Conexión a internet (para las descargas de Yahoo Finance).

### 1. Clonar el repositorio
```bash
git clone https://github.com/jcpd4/inversiones_juanky_proyecto_01.git
cd inversiones_juanky_proyecto_01
```

### 2. Entorno virtual (Recomendado)
```bash
python -m venv venv
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 3. Instalar dependencias
Instala las librerías Core, de Inteligencia de Datos y el Servidor Web:
```bash
pip install pandas yfinance matplotlib fastapi uvicorn
```

## 🚀 Uso del Aplicativo Web (Modo Frontend)
El sistema ha sido mejorado para incluir una interfaz de usuario en el navegador con un diseño Premium y visualización de gráficos nativa (*Chart.js*).

1. Inicia el servidor backend y el manejador de archivos estáticos:
```bash
uvicorn api:app --reload
```
2. Abre tu navegador web e ingresa a `http://127.0.0.1:8000`.
3. Selecciona un activo en el menú lateral o escribe uno personalizado (ej. NVDA, AMZN) y ejecuta la simulación interactiva.

## 🖥 Uso del CLI Clásico (Línea de Comandos)
Si prefieres generar las visualizaciones offline (usando Matplotlib) y utilizar la consola, aún puedes usar el bot original:
```bash
python bot.py
```
O usar el motor puro:
```bash
python main.py
```

## 💼 Perfil Profesional y Contexto
Este ecosistema forma parte de mi portafolio de Ingeniería Informática, concebido para demostrar competencias avanzadas:
- **Analítica de Datos**: (Pandas, yfinance).
- **Backend / APIs**: (FastAPI, RESTful patterns).
- **Frontend Moderno**: Arquitectura asíncrona (Fetch API), Vanilla UI/UX Premium (*Glassmorphism*, Variables CSS), *Chart.js*.
- **Código de Calidad**: Docstrings, separación de responsabilidades, *Clean Code*.