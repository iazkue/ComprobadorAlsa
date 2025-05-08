import time
import argparse
import logging
from requests_html import HTMLSession
from plyer import notification

# Configuración de logging
logging.basicConfig(
    filename="comprobador_alsa.log",  # Archivo donde se guardarán los logs
    level=logging.INFO,              # Nivel de log (INFO, DEBUG, ERROR, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Intervalo de comprobación en segundos (1 minuto)
CHECK_INTERVAL = 60

def check_availability(url):
    session = HTMLSession()

    try:
        logging.info("Realizando la solicitud a la URL: %s", url)
        # Hacer la solicitud HTTP y renderizar JavaScript
        response = session.get(url)
        response.html.render(sleep=2)  # Renderizar con soporte de JavaScript y esperar 2 segundos

        # Buscar el texto específico en el contenido renderizado
        if "No hay plazas disponibles." in response.html.text:
            logging.info("No hay plazas disponibles. Se volverá a comprobar en 1 minuto.")
            print("No hay plazas disponibles. Se volverá a comprobar en 1 minuto.")
        else:
            logging.info("¡Plazas detectadas!")
            print("¡Plazas detectadas!")
            notification.notify(
                title="¡Atención!",
                message="Hay plazas disponibles en ALSA.",
                timeout=10
            )
    except Exception as e:
        logging.error("Error al realizar la comprobación: %s", e, exc_info=True)
        print(f"Error al realizar la comprobación: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description="Comprobador de disponibilidad de plazas para Alsa.")
    parser.add_argument("url", type=str, help="La URL de la página de Alsa a comprobar")

    # Parsear los argumentos
    args = parser.parse_args()

    # Obtener la URL desde los argumentos
    url = args.url

    try:
        logging.info("Iniciando el comprobador para la URL: %s", url)
        # Ejecutar comprobaciones en un bucle infinito
        while True:
            check_availability(url)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        logging.info("Interrupción detectada. Cerrando el script...")
        print("\nInterrupción detectada. Cerrando el script...")
    except Exception as e:
        logging.error("Error inesperado: %s", e, exc_info=True)
        print(f"Error inesperado: {e}")
    finally:
        logging.info("Script finalizado.")