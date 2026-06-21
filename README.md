# Este es el proyecto que me va hacer Rico

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Copia `.env.example` como `.env` y rellena tus claves de API:

```bash
cp .env.example .env
```

## Estructura del proyecto

```
organizacion_proyecto/
├── data/
│   ├── raw/          # Datos descargados sin procesar
│   └── processed/    # Datos limpios y transformados
├── strategies/       # Estrategias de trading
├── backtesting/      # Scripts de backtesting
├── notebooks/        # Jupyter notebooks de análisis
├── logs/             # Logs de ejecución
├── results/          # Resultados de backtests
├── main.py           # Punto de entrada
├── requirements.txt
└── .env              # Claves de API (no subir a git)
```
