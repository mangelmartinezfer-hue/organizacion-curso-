import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from config import SYMBOL, TIMEFRAME

# ── 1. Cargar datos desde CSV ────────────────────────────────────────────────
csv_path = f"data/raw/{SYMBOL}_{TIMEFRAME}.csv"
df = pd.read_csv(csv_path, index_col="timestamp", parse_dates=True)

# ── 2. Crear el grafico ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(df.index, df["close"], color="royalblue", linewidth=1.5, label="Close")

ax.fill_between(df.index, df["close"], alpha=0.1, color="royalblue")

# ── 3. Formato del grafico ───────────────────────────────────────────────────
ax.set_title(f"{SYMBOL} — Precio de Cierre ({TIMEFRAME})", fontsize=14, fontweight="bold")
ax.set_xlabel("Fecha")
ax.set_ylabel("Precio (USD)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(df.index[0], df.index[-1])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
fig.autofmt_xdate()

# ── 4. Guardar PNG en charts/ ────────────────────────────────────────────────
output_path = f"charts/{SYMBOL}_{TIMEFRAME}_close.png"
plt.tight_layout()
plt.savefig(output_path, dpi=150)
plt.close()

print(f"Grafico guardado en: {output_path}")
