# 📈 Bot de Trading & Simulador de Inversiones (Paper Trading)

## 📌 Descripción del Proyecto
Este proyecto es un **Bot de Inversión Algorítmica y Simulador de Paper Trading** desarrollado en Python. Diseñado como una herramienta robusta para realizar *backtesting* de estrategias de mercado, el bot descarga el histórico de precios de activos financieros reales, aplica cálculo de indicadores técnicos para buscar oportunidades de mercado y simula la compra y venta de las posiciones.

El objetivo de esta herramienta es evaluar la rentabilidad teórica de un capital inicial (100€) asumiendo una operativa automatizada. 

## 🧠 Estrategia Implementada: Cruce de Medias Móviles (SMA)
El "cerebro" del bot toma sus decisiones basado en una de las estrategias clásicas y más reconocidas del análisis técnico: **El Cruce de Medias Móviles Simples (SMA)**.

1. **SMA Rápida (14 días)**: Reacciona de forma veloz a los cambios recientes de precio.
2. **SMA Lenta (50 días)**: Indica la tendencia general subyacente del mercado en el mediano plazo.
   
**Señales de Trading Generadas**:
- 🟢 **Señal de Compra (Golden Cross / 1)**: Se activa cuando la media rápida de 14 días cruza por encima de la media lenta de 50 días. Esto indica un impulso alcista. El bot invierte automáticamente el capital líquido disponible asumiendo una tendencia al alza.
- 🔴 **Señal de Venta (Death Cross / -1)**: Se activa cuando la media rápida cruza por debajo de la lenta. Esto señala debilidad y un posible cambio a tendencia bajista. El bot vende la totalidad de las acciones para asegurar y proteger el capital.

## 🛠 Requisitos Previos
- Python 3.8 o superior.
- `pip` (Gestor de paquetes de Python).
- Conexión a internet (para las descargas de Yahoo Finance).

Es necesario tener instaladas las siguientes librerías core: `pandas`, `yfinance` y `matplotlib`.

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/inversiones_01.git
cd inversiones_01
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
```bash
pip install pandas yfinance matplotlib
```

### 4. Puesta en Marcha (Interfaz Interactiva CLI)
```bash
python bot.py
```
Aparecerá un menú interactivo en tu terminal que te permitirá seleccionar perfiles predefinidos (Apple, Bitcoin) o ingresar el *Stock Ticker* de tu preferencia.

El bot ejecutará la descarga de datos, el procesamiento de la estrategia y el backtesting, mostrando por consola una tabla atractiva con el **Capital Final** y la **Rentabilidad (%)**. Finalmente, el script guardará una gráfica `.png` proyectando la evolución de tu inversión teórica de 100€ a lo largo del tiempo.

También puedes ejecutar directamente la lógica cruda para desarrollo:
```bash
python main.py
```

## 💼 Perfil Profesional y Contexto
Este script forma parte de mi portafolio de Ingeniería Informática, concebido para demostrar competencias clave demandadas en el mercado laboral: analítica de datos aplicada a finanzas (Quant/FinTech), desarrollo modular, programación defensiva bajo Python y un uso sólido de ecosistema de librerías como Pandas y Matplotlib.