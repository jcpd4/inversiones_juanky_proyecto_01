# 🤖 Bot de Trading & Simulador de Inversiones

Este proyecto es un bot de inversión automatizado desarrollado en Python como parte de mi portafolio de Ingeniería Informática. 

El objetivo principal es realizar **Paper Trading**: simular una inversión inicial de **100€** y aplicar estrategias de análisis técnico (medias móviles) sobre datos reales para evaluar la rentabilidad automática de la cartera.

---

## 🗺️ Roadmap del Proyecto

### FASE 1: Configuración del Entorno (Setup) 🛠️
*El objetivo es tener un lienzo en blanco listo y profesional.*
- [x] Crear un repositorio nuevo en GitHub (vacío).
- [x] Clonar el repositorio en tu ordenador local.
- [ ] Crear un entorno virtual de Python (`python -m venv venv`).
- [ ] Activar el entorno virtual.
- [ ] Crear un archivo `.gitignore` y añadir la línea `venv/` (para no subir librerías basura a GitHub).
- [ ] Crear un archivo `main.py` vacío.
- [ ] Hacer el primer commit: "Initial commit: estructura básica".
- [ ] Subir los cambios a GitHub (`git push`).

### FASE 2: Instalación y Datos (Data Ingestion) 📊
*El objetivo es que tu código pueda "ver" el mercado.*
- [ ] Instalar librería de datos (`pip install yfinance`).
- [ ] Instalar librería de manipulación (`pip install pandas`).
- [ ] Crear un archivo `requirements.txt` (`pip freeze > requirements.txt`).
- [ ] En `main.py`, importar `yfinance`.
- [ ] Escribir una función simple `obtener_datos(simbolo)` que descargue datos de Apple ('AAPL').
- [ ] Hacer que la función imprima por pantalla las últimas 5 filas de los datos (`print(df.tail())`).
- [ ] Ejecutar el script y verificar que ves números (precios) en la consola.
- [ ] Commit: "Feature: Conexión con API de yfinance establecida".

### FASE 3: Definición de la Estrategia (El Cerebro) 🧠
*El objetivo es definir cuándo comprar y cuándo vender.*
- [ ] Crear un nuevo archivo `estrategia.py`.
- [ ] Crear una función que reciba el DataFrame de datos.
- [ ] Calcular la "Media Móvil Simple" (SMA) de 14 días y guardarla en una columna nueva.
- [ ] Calcular la "Media Móvil Simple" de 50 días y guardarla en otra columna.
- [ ] Limpiar los datos vacíos (`dropna`) que se generan al calcular medias.
- [ ] Crear una columna nueva llamada `Señal`.
- [ ] Lógica: Escribir código que ponga un `1` (Compra) en `Señal` cuando la media corta cruce por encima de la larga.
- [ ] Lógica: Escribir código que ponga un `-1` (Venta) cuando la media corta cruce por debajo de la larga.
- [ ] Devolver el DataFrame limpio con las señales.
- [ ] Commit: "Feature: Lógica de cruce de medias móviles implementada".

### FASE 4: El Motor de Backtesting (La Cartera) 💰
*Aquí es donde simulamos los 100€.*
- [ ] Crear un nuevo archivo `cartera.py`.
- [ ] Definir una variable `capital_inicial = 100`.
- [ ] Definir una variable `dinero_disponible = 100`.
- [ ] Definir una variable `acciones_poseidas = 0`.
- [ ] Crear una función `simular_inversion(datos)` que recorra el DataFrame fila por fila (bucle for).
- [ ] Dentro del bucle: Si la columna `Señal` es `1` (Compra) Y tengo dinero > comprar tantas acciones como pueda.
- [ ] Restar el costo de la compra a `dinero_disponible` y sumar cantidad a `acciones_poseidas`.
- [ ] Dentro del bucle: Si la columna `Señal` es `-1` (Venta) Y tengo acciones > vender todo.
- [ ] Sumar la venta a `dinero_disponible` y poner `acciones_poseidas` a 0.
- [ ] Guardar en una lista el valor total de la cartera (dinero + valor acciones) en cada día.
- [ ] Commit: "Feature: Motor de simulación de compra/venta creado".

### FASE 5: Análisis de Resultados (El Reporte) 📉
*Ver si ganamos o perdimos dinero.*
- [ ] En `main.py`, conectar todo: bajar datos -> aplicar estrategia -> simular cartera.
- [ ] Al final de la simulación, calcular el valor final total.
- [ ] Calcular la rentabilidad: `((valor_final - 100) / 100) * 100`.
- [ ] Imprimir un mensaje bonito: "Resultado: Empezaste con 100€ y acabaste con X€".
- [ ] Imprimir: "Rentabilidad total: X%".
- [ ] Commit: "Feature: Calculadora de rentabilidad finalizada".

### FASE 6: Conversión a BOT (Interacción) 🤖
*Hacer que te "hable" o funcione automático.*
- [ ] Crear un archivo `bot.py`.
- [ ] Crear un menú simple en consola: "1. Analizar Apple, 2. Analizar Bitcoin, 3. Salir".
- [ ] Hacer que el usuario pueda escribir el símbolo de la acción (`input`).
- [ ] Ejecutar la simulación basada en lo que el usuario escribió.
- [ ] (Opcional - Nivel Pro) Instalar `matplotlib`.
- [ ] (Opcional - Nivel Pro) Generar un gráfico simple que muestre cómo crecieron (o bajaron) tus 100€.
- [ ] Commit: "Feature: Interfaz de línea de comandos (CLI) creada".

### FASE 7: Limpieza y Documentación (Para el CV) ✨
*Esto es lo que mirará el reclutador.*
- [ ] Borrar cualquier `print` que usaste para depurar y no sirva.
- [ ] Añadir "Docstrings" a las funciones (comentarios que explican qué hace cada función).
- [ ] Crear un archivo `README.md` potente.
- [ ] Escribir en el README: Título del proyecto.
- [ ] Escribir en el README: Descripción ("Bot que simula inversión algorítmica...").
- [ ] Escribir en el README: Instrucciones de instalación ("Clonar, pip install...").
- [ ] Escribir en el README: Un ejemplo de uso (captura de pantalla de la consola).
- [ ] Commit final: "Release: Versión 1.0 lista para portafolio".

---
*Autor: Juanky Tranky*