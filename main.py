from extract import extract_data
from transform import clean_retail, clean_customers
import pandas as pd
import os

def main():
    # =====================
    # Extract
    # =====================
    df_retail, df_customers = extract_data()

    # =====================
    # Transform
    # =====================
    df_retail = clean_retail(df_retail)
    df_customers = clean_customers(df_customers)

    # =====================
    # Fact Table (Ventas)
    # =====================
    fact_sales = df_retail.merge(
        df_customers,
        left_on="customer_id",
        right_on="customer_id",
        how="inner"   # solo clientes válidos con transacciones
    )

    # =====================
    # Load (guardar CSV)
    # =====================
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)  # crear carpeta si no existe
    output_path = os.path.join(output_dir, "fact_sales.csv")

    fact_sales.to_csv(output_path, index=False)

    print("ETL completado")
    print(f"Tabla de hechos guardada en: {output_path}")
    print("Vista previa:")
    print(fact_sales.head())

if __name__ == "__main__":
    main()
