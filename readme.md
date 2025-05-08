# Comprobador Alsa

Este script en Python permite comprobar la disponibilidad de plazas en una página de Alsa de manera periódica, cada minuto.

## Uso

Ejecuta el script pasando la URL como argumento:

```bash
python comprobador_alsa.py "URL_DE_LA_PÁGINA_ALSA"
```

El script comprueba cada minuto si aparece el mensaje "No hay plazas disponibles." en la página especificada. Si no se encuentra ese mensaje, te notificará que hay plazas disponibles.

## Requisitos

Instala las dependencias requeridas con:

```bash
pip install -r requirements.txt
```

## Notificaciones

El script utiliza `plyer` para mostrar notificaciones en tu sistema operativo.

## Contribución

Si deseas contribuir, abre un pull request o reporta problemas en la sección de issues.
