import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dotenv import load_dotenv

from config import SYMBOL, TIMEFRAME, LIMIT, START_DATE, END_DATE

# ── 1. Cargar claves desde .env ──────────────────────────────────────────────
load_dotenv()

API_KEY    = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

# ── 2. Cabeceras de autenticacion ────────────────────────────────────────────
headers = {
    "APCA-API-KEY-ID":     API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}

# ── 3. Llamada a la API de Alpaca ────────────────────────────────────────────
DATA_URL = "https://data.alpaca.markets/v2"

params = {
    "symbols":   SYMBOL,
    "timeframe": TIMEFRAME,
    "start":     START_DATE,
    "end":       END_DATE,
}
if LIMIT is not None:
    params["limit"] = LIMIT

response = requests.get(f"{DATA_URL}/stocks/bars", headers=headers, params=params)
response.raise_for_status()

# ── 4. Convertir respuesta a DataFrame ──────────────────────────────────────
raw   = response.json()
bars  = raw["bars"][SYMBOL]

df = pd.DataFrame(bars)
df["t"] = pd.to_datetime(df["t"])
df.rename(columns={
    "t":  "timestamp",
    "o":  "open",
    "h":  "high",
    "l":  "low",
    "c":  "close",
    "v":  "volume",
    "n":  "trades",
    "vw": "vwap"
}, inplace=True)
df.set_index("timestamp", inplace=True)
df = df[["open", "high", "low", "close", "volume", "trades", "vwap"]]

# ── 5. Guardar en data/raw/ ──────────────────────────────────────────────────
output_path = f"data/raw/{SYMBOL}_{TIMEFRAME}.csv"
df.to_csv(output_path)
print(f"Datos guardados en: {output_path}")

# ── 6. Mostrar resultado ─────────────────────────────────────────────────────
print(f"\n--- {SYMBOL} | {TIMEFRAME} | {len(df)} barras ---\n")
print(df.tail(10))

# ── 7. Generar grafico de precio close ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(df.index, df["close"], color="royalblue", linewidth=1.5, label="Close")
ax.fill_between(df.index, df["close"], alpha=0.1, color="royalblue")

ax.set_title(f"{SYMBOL} — Precio de Cierre ({TIMEFRAME})", fontsize=14, fontweight="bold")
ax.set_xlabel("Fecha")
ax.set_ylabel("Precio (USD)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(df.index[0], df.index[-1])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
fig.autofmt_xdate()

chart_path = f"charts/{SYMBOL}_{TIMEFRAME}_close.png"
plt.tight_layout()
plt.savefig(chart_path, dpi=150)
plt.close()

print(f"Grafico guardado en: {chart_path}")
