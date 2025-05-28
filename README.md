# ghost

Este repositorio contiene un script que despierta automáticamente tus aplicaciones Streamlit para que no entren en modo suspensión.

## ¿Cómo funciona?

- `ping_once.py` hace peticiones HTTP periódicas a las URLs de tus apps.
- GitHub Actions ejecuta este script cada x minutos.
- Así mantienes activas tus apps sin servidores ni tareas manuales.

## Apps mantenidas activas

- [Calculadoras Náuticas](https://calculadorasnauticas.streamlit.app/)
- [Rectas de Altura](https://rectasaltura.streamlit.app/)

## Configuración

1. Edita `ping_once.py` si cambias las URLs.

2. Sube todos los archivos al repositorio `ghost`.

## Uso

- Automáticamente cada 5 minutos GitHub ejecutará el script.
- También puedes lanzarlo manualmente desde la pestaña **Actions**.

## Requisitos

- Python 3.x
- Paquete `requests`

---

> GitHub Actions es gratis e ilimitado para repos públicos.
