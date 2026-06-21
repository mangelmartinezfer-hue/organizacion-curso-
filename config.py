# Aqui pongo las variables del sistema

# ─── Parametros de estrategia ───────────────────────────────────────────────
TIMEFRAME = '1h'  # Timeframe for the data (e.g., '1m', '5m', '1h', '1d')

VALOR_EMA_RAPIDA = 12
VALOR_EMA_LENTA = 26

# ─── Conexion Interactive Brokers (TWS / IB Gateway) ────────────────────────
# Requisito: tener TWS o IB Gateway abierto y el API habilitado en:
#   TWS > Edit > Global Configuration > API > Settings > Enable ActiveX and Socket Clients
IB_HOST = '127.0.0.1'   # localhost (misma maquina)
IB_PORT = 7497           # 7497 = TWS paper trading | 7496 = TWS real | 4002 = Gateway paper | 4001 = Gateway real
IB_CLIENT_ID = 1         # ID unico por conexion (puedes poner cualquier numero)

# ─── Instrumento a descargar ─────────────────────────────────────────────────
IB_SYMBOL   = 'AAPL'    # Ticker del activo
IB_SEC_TYPE = 'STK'     # STK=accion | FUT=futuro | FOREX=divisas | OPT=opcion
IB_EXCHANGE = 'SMART'   # SMART = enrutamiento automatico IB
IB_CURRENCY = 'USD'

# ─── Rango de datos historicos ───────────────────────────────────────────────
IB_DURATION  = '1 Y'    # Cantidad de historia: '1 D', '1 W', '1 M', '1 Y', '5 Y'
IB_BAR_SIZE  = '1 hour' # Tamanyo de vela: '1 min','5 mins','1 hour','1 day', etc.
IB_WHAT_TO_SHOW = 'TRADES'  # TRADES | MIDPOINT | BID | ASK
