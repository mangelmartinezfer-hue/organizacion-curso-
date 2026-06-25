import os
import sys
import requests
import pandas as pd
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import TIMEFRAME, LIMIT, START_DATE, END_DATE

load_dotenv()

API_KEY    = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

# DIA es el ETF que replica el Dow Jones Industrial Average
SYMBOL = "DIA"

headers = {
    "APCA-API-KEY-ID":     API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}

DATA_URL = "https://data.alpaca.markets/v2"

# Usar los timestamps de NVDA como rango si existe el archivo
nvda_path = "data/raw/NVDA_{}.csv".format(TIMEFRAME)
if os.path.exists(nvda_path):
    nvda_df    = pd.read_csv(nvda_path, index_col="timestamp", parse_dates=True)
    start_date = str(nvda_df.index[0].date())
    end_date   = str(nvda_df.index[-1].date())
    print(f"Usando timestamps de NVDA: {start_date} a {end_date}")
else:
    start_date = START_DATE
    end_date   = END_DATE

params = {
    "symbols":   SYMBOL,
    "timeframe": TIMEFRAME,
    "start":     start_date,
    "end":       end_date,
}
if LIMIT is not None:
    params["limit"] = LIMIT

response = requests.get(f"{DATA_URL}/stocks/bars", headers=headers, params=params)
response.raise_for_status()

raw  = response.json()
bars = raw["bars"][SYMBOL]

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

output_path = f"data/raw/{SYMBOL}_{TIMEFRAME}.csv"
df.to_csv(output_path)

print(f"Datos guardados en: {output_path}")
print(f"\n--- {SYMBOL} (Dow Jones ETF) | {TIMEFRAME} | {len(df)} barras ---\n")
print(df.tail(10))
