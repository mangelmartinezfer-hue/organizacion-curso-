# Aqui pongo las variables del sistema

# --- Alpaca endpoint ---------------------------------------------------------
ALPACA_BASE_URL = "https://paper-api.alpaca.markets/v2"

# --- Parametros de estrategia ------------------------------------------------
SYMBOL    = 'NVDA'   # Ticker del activo a descargar
TIMEFRAME = '1Hour'  # Timeframe Alpaca: '1Min', '5Min', '1Hour', '1Day'
LIMIT     = None     # None = todas las barras del rango | numero = limitar

START_DATE = "2025-01-01"   # Fecha inicio  (YYYY-MM-DD) | None = sin limite
END_DATE   = "2025-12-31"   # Fecha fin      (YYYY-MM-DD) | None = hoy

VALOR_EMA_RAPIDA = 12
VALOR_EMA_LENTA  = 26
