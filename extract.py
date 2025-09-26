import pandas as pd
import os

def extract_data():
    """
    Extract step: reads retail_data.csv and customer_data.csv
    from the 'data' folder and returns them as two DataFrames.
    """
    data_dir = "data"

    # Rutas de los archivos
    retail_path = os.path.join(data_dir, "retail_data.csv")
    customers_path = os.path.join(data_dir, "customer_data.csv")

    # Validación de existencia
    if not os.path.exists(retail_path):
        raise FileNotFoundError(f"No se encontró {retail_path}")
    if not os.path.exists(customers_path):
        raise FileNotFoundError(f"No se encontró {customers_path}")

    # Lectura
    df_retail = pd.read_csv(retail_path)
    df_customers = pd.read_csv(customers_path)

    return df_retail, df_customers
