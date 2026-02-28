import sys
import matplotlib.pyplot as plt
from main import ejecutar_bot

def mostrar_menu() -> str:
    """Muestra el menú interactivo y devuelve el ticker seleccionado."""
    print("\n" + "="*40)
    print("🤖 BIENVENIDO AL BOT DE TRADING 🤖")
    print("="*40)
    print("Elige un activo para simular inversión:")
    print("1. Apple (AAPL)")
    print("2. Bitcoin (BTC-USD)")
    print("3. Ticker personalizado")
    print("4. Salir")
    print("="*40)
    
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == '1':
        return "AAPL"
    elif opcion == '2':
        return "BTC-USD"
    elif opcion == '3':
        ticker = input("Introduce el Ticker (ej. MSFT, TSLA, ETH-USD): ").upper()
        return ticker
    elif opcion == '4':
        print("Saliendo del bot. ¡Hasta pronto! 👋")
        sys.exit()
    else:
        print("❌ Opción inválida. Inténtalo de nuevo.")
        return mostrar_menu()

def generar_grafico(datos, ticker: str):
    """Genera un gráfico de evolución de la cartera y lo guarda como imagen."""
    plt.figure(figsize=(10, 5))
    plt.plot(datos.index, datos['Valor_Cartera'], label='Valor de la Cartera (€)', color='#1f77b4', linewidth=1.5)
    
    plt.title(f'Evolución del Capital (Paper Trading) - {ticker}', fontsize=14, pad=15)
    plt.xlabel('Fecha', fontsize=11)
    plt.ylabel('Valor Total (€)', fontsize=11)
    
    # Rellenar debajo de la línea
    plt.fill_between(datos.index, datos['Valor_Cartera'], 100, where=(datos['Valor_Cartera'] >= 100), color='green', alpha=0.1)
    plt.fill_between(datos.index, datos['Valor_Cartera'], 100, where=(datos['Valor_Cartera'] < 100), color='red', alpha=0.1)
    
    # Línea base de inversión inicial
    plt.axhline(y=100, color='r', linestyle='--', label='Inversión Inicial (100€)', alpha=0.7)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    nombre_archivo = f"grafico_{ticker}.png"
    plt.savefig(nombre_archivo, dpi=300)
    print(f"📉 Gráfico generado y guardado exitosamente como '{nombre_archivo}'.")

def iniciar_bot():
    """Bucle principal de la interfaz interactiva."""
    while True:
        ticker = mostrar_menu()
        try:
            # Reutilizamos la lógica principal
            datos_simulados = ejecutar_bot(ticker)
            
            # Generamos el gráfico visual
            print("🎨 Generando el gráfico de resultados...")
            generar_grafico(datos_simulados, ticker)
            
        except ImportError as e:
            print("❌ Error de importación. Asegúrate de tener instalada la librería adecuada.")
            print(f"Detalle: {e}")
        except Exception as e:
            print(f"\n❌ Ocurrió un error al analizar '{ticker}'. ¿El Ticker está bien escrito o no hay suficientes datos?")
            print(f"Detalle técnico: {e}\n")

if __name__ == "__main__":
    # Necesitamos matplotlib para esto
    # Si el usuario no lo tiene, fallará, pero el bot capturará el error si podemos.
    try:
        iniciar_bot()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo...")
        sys.exit()
