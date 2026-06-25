# Aqui pongo las variables del sistema

# --- Alpaca endpoint ---------------------------------------------------------
ALPACA_BASE_URL = "https://paper-api.alpaca.markets/v2"

# --- Activo a trabajar -------------------------------------------------------
# Cambia solo esta linea para trabajar con cualquier activo
# Ejemplos: 'NVDA', 'TSLA', 'AAPL', 'MSFT', 'AMZN', 'SPY'
SYMBOL    = 'NVDA'

TIMEFRAME = '1Hour'  # Timeframe Alpaca: '1Min', '5Min', '1Hour', '1Day'
LIMIT     = None     # None = todas las barras del rango | numero = limitar

# Nombre del fichero generado automaticamente segun SYMBOL y TIMEFRAME
FICHERO   = f"{SYMBOL}_{TIMEFRAME}"  # Ej: NVDA_1Hour, TSLA_1Day

START_DATE = "2025-01-01"   # Fecha inicio  (YYYY-MM-DD) | None = sin limite
END_DATE   = "2025-12-31"   # Fecha fin      (YYYY-MM-DD) | None = hoy

VALOR_EMA_RAPIDA = 12
VALOR_EMA_LENTA  = 26

# --- Yahoo Finance -----------------------------------------------------------
TICKER_YAHOO  = "TSLA"  # Ticker symbol for Yahoo Finance data retrieval
YAHOO_TIMEFRAME = "5m"  # Timeframe Yahoo: 1m,2m,5m,15m,30m,60m,1h,4h,1d,1wk
