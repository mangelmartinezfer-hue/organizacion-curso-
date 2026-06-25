import pandas as pd
from config import FICHERO

# ── 1. Cargar CSV usando el fichero definido en config.py ────────────────────
df = pd.read_csv(
    f"data/raw/{FICHERO}.csv",
    index_col="timestamp",
    parse_dates=True
)

# ── 2. Añadir columna dow (dia de la semana en español) ─────────────────────
dias = {
    "Monday":    "Lunes",
    "Tuesday":   "Martes",
    "Wednesday": "Miercoles",
    "Thursday":  "Jueves",
    "Friday":    "Viernes",
    "Saturday":  "Sabado",
    "Sunday":    "Domingo"
}
df["dow"] = df.index.day_name().map(dias)

# ── 3. Guardar en data/processed/ ────────────────────────────────────────────
df.to_csv(f"data/processed/{FICHERO}.csv")
print(f"DataFrame guardado en: data/processed/{FICHERO}.csv")

# ── 4. Mostrar en terminal ───────────────────────────────────────────────────
print(f"\n--- {FICHERO} | {len(df)} filas x {len(df.columns)} columnas ---\n")
print(df)
