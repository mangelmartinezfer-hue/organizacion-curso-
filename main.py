import runpy
from dotenv import load_dotenv

load_dotenv()

print("=== Paso 1: Descargando datos ===")
runpy.run_path("get_alpaca_data.py")

print("=== Paso 2: Generando grafico ===")
runpy.run_path("plot_chart.py")

print("=== Proceso completado ===")
