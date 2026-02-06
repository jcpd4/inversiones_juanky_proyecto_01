# 📈 Bot de Trading Algorítmico - Proyecto Inversiones 01

Este proyecto es un bot de inversión automatizado desarrollado en Python. El objetivo es simular una cartera de inversión de 100€ (Paper Trading), aplicando estrategias de Análisis Técnico sobre datos financieros en tiempo real para tomar decisiones de compra y venta.

## 📋 Roadmap del Proyecto (Micro-tareas)

### FASE 1: Configuración del Entorno (Setup) 🛠️
- [ ] Crear un entorno virtual de Python (`python -m venv venv`).
- [ ] Activar el entorno virtual.
- [ ] Crear archivo `.gitignore` y añadir `venv/` y `.DS_Store`.
- [ ] Crear archivo `main.py` vacío.
- [ ] Hacer el primer commit de estructura básica.

### FASE 2: Instalación y Datos (Data Ingestion) 📊
- [ ] Instalar librería de datos (`pip install yfinance`).
- [ ] Instalar librería de manipulación (`pip install pandas`).
- [ ] Crear archivo `requirements.txt` (`pip freeze > requirements.txt`).
- [ ] En `main.py`: Importar `yfinance`.
- [ ] En `main.py`: Crear función `obtener_datos(simbolo)` para descargar precios.
- [ ] Verificar que la función imprime los últimos datos en consola.

### FASE 3: Definición de la Estrategia (El Cerebro) 🧠
- [ ] Crear archivo `estrategia.py`.
- [ ] Crear función que reciba el DataFrame de datos.
- [ ] Calcular Media Móvil Simple (SMA) de 14 días.
- [ ] Calcular Media Móvil Simple (SMA) de 50 días.
- [ ] Limpiar datos vacíos (`dropna`).
- [ ] Crear columna `Señal`: poner `1` cuando la media corta cruce por encima de la larga (Compra).
- [ ] Crear columna `Señal`: poner `-1` cuando la media corta cruce por debajo de la larga (Venta).

### FASE 4: El Motor de Backtesting (La Cartera) 💰
- [ ] Crear archivo `cartera.py`.
- [ ] Definir variables: `capital_inicial = 100`, `dinero_disponible`, `acciones_poseidas`.
- [ ] Crear función `simular_inversion(datos)` que recorra el DataFrame fila por fila.
- [ ] Lógica de Compra: Si `Señal == 1` y hay dinero -> Comprar (restar dinero, sumar acciones).
- [ ] Lógica de Venta: Si `Señal == -1` y hay acciones -> Vender (sumar dinero, restar acciones).
- [ ] Guardar historial del valor total de la cartera día a día.

### FASE 5: Análisis de Resultados 📉
- [ ] En `main.py`: Conectar módulos (Datos -> Estrategia -> Cartera).
- [ ] Calcular valor final total (Dinero + Valor Acciones actuales).
- [ ] Calcular Rentabilidad: `((Valor Final - 100) / 100) * 100`.
- [ ] Imprimir reporte en consola: "Iniciaste con 100€, terminaste con X€".

### FASE 6: Conversión a BOT (Interacción) 🤖
- [ ] Crear archivo `bot.py` o adaptar `main.py`.
- [ ] Crear menú en consola: "1. Analizar Acción, 2. Salir".
- [ ] Permitir al usuario escribir el símbolo (ej: 'BTC-USD', 'AAPL').
- [ ] Ejecutar simulación basada en el input del usuario.

### FASE 7: Limpieza y Finalización ✨
- [ ] Eliminar `print` de depuración innecesarios.
- [ ] Añadir comentarios (Docstrings) explicando las funciones.
- [ ] Actualizar este README con instrucciones de uso finales.