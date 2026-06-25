import yfinance as yf
import pandas as pd
from config import TICKER_YAHOO, YAHOO_TIMEFRAME, START_DATE, END_DATE

# ── 1. Descargar datos de Yahoo Finance ──────────────────────────────────────
print(f"Descargando {TICKER_YAHOO} desde Yahoo Finance...")

INTRADIARIOS = {"1m", "2m", "5m", "15m", "30m", "60m", "1h"}
PERIOD_MAP   = {"1m": "7d", "2m": "60d", "5m": "60d", "15m": "60d",
                "30m": "60d", "60m": "60d", "1h": "60d"}

if YAHOO_TIMEFRAME in INTRADIARIOS:
    df = yf.download(
        TICKER_YAHOO,
        period=PERIOD_MAP[YAHOO_TIMEFRAME],
        interval=YAHOO_TIMEFRAME,
        auto_adjust=True,
        progress=False
    )
else:
    df = yf.download(
        TICKER_YAHOO,
        start=START_DATE,
        end=END_DATE,
        interval=YAHOO_TIMEFRAME,
        auto_adjust=True,
        progress=False
    )

# ── 2. Limpiar columnas ──────────────────────────────────────────────────────
df.columns = [col[0].lower() if isinstance(col, tuple) else col.lower()
              for col in df.columns]
df.index.name = "timestamp"

# ── 3. Guardar en data/raw/ ──────────────────────────────────────────────────
output_path = f"data/raw/{TICKER_YAHOO}_{YAHOO_TIMEFRAME}_yahoo.csv"
df.to_csv(output_path)
print(f"Datos guardados en: {output_path}")

# ── 4. Mostrar resultado ─────────────────────────────────────────────────────
print(f"\n--- {TICKER_YAHOO} | {YAHOO_TIMEFRAME} | {len(df)} barras ---\n")
print(df.tail(10))
