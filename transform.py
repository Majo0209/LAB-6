import re
import pandas as pd
import numpy as np
from dateutil import parser

# ======================
# Función de renombrado
# ======================
def renombrar_columnas(df: pd.DataFrame, mapa: dict) -> pd.DataFrame:
    return df.rename(columns=mapa)

# ======================
# Customers
# ======================
def transformar_phone(num, default_prefix="+1"):
    if pd.isna(num):
        return np.nan
    digits = re.sub(r"\D", "", str(num))
    if len(digits) != 10:
        return np.nan
    area, central, line = digits[:3], digits[3:6], digits[6:]
    return f"{default_prefix} ({area}) {central}-{line}"

def transformar_fecha(fecha):
    if pd.isna(fecha):
        return "No especificado"
    try:
        return parser.parse(str(fecha), dayfirst=False).strftime("%Y-%m-%d")
    except:
        try:
            return parser.parse(str(fecha), dayfirst=True).strftime("%Y-%m-%d")
        except:
            return "No especificado"


def transformar_email(email: str):
    if pd.isna(email):
        return np.nan
    email = str(email).strip().lower()
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return email
    return np.nan

def transformar_age(age):
    try:
        age = int(float(age))
        if 13 <= age <= 120:
            return str(age)   
        else:
            return "No especificado"
    except:
        return "No especificado"


# ======================
# Retail
# ======================
def transformar_amount(value):
    try:
        val = float(value)
        return val if val >= 0 else np.nan
    except:
        return np.nan

def normalizar_categoria(categoria):
    categorias_validas = ["Sports", "Clothing", "Electronics", "Toys", "Home & Kitchen"]
    if categoria in categorias_validas:
        return categoria
    return np.nan

# ======================
# Resolución de duplicados
# ======================
def resolver_ids_retail(df):
    df_clean = df.drop_duplicates()

    df_clean["transaction_id"] = (
        df_clean.groupby("transaction_id").cumcount()
        .astype(str)
        .replace("0", "")  
        .radd(df_clean["transaction_id"].astype(str))
    )

    return df_clean


def resolver_ids_customers(df):
    # 1. Eliminar duplicados exactos
    df_clean = df.drop_duplicates()

    # 2. Manejar IDs duplicados en customer_id
    df_clean["customer_id"] = (
        df_clean.groupby("customer_id").cumcount()
        .astype(str)
        .replace("0", "")  
        .radd(df_clean["customer_id"].astype(str))
    )

    return df_clean

# ======================
# Funciones de limpieza
# ======================
def clean_customers(df):
    df_clean = df.copy()
    df_clean = renombrar_columnas(df_clean, {"id": "customer_id"})

    if "phone" in df_clean.columns:
        df_clean["phone"] = df_clean["phone"].apply(transformar_phone)
    if "email" in df_clean.columns:
        df_clean["email"] = df_clean["email"].apply(transformar_email)
    if "signup_date" in df_clean.columns:
        df_clean["signup_date"] = df_clean["signup_date"].apply(transformar_fecha)
    if "age" in df_clean.columns:
        df_clean["age"] = df_clean["age"].apply(transformar_age)

    if "full_name" in df_clean.columns:
        df_clean["full_name"] = df_clean["full_name"].fillna(np.nan)
    if "address" in df_clean.columns:
        df_clean["address"] = df_clean["address"].fillna(np.nan)

    if "customer_id" in df_clean.columns:
        df_clean = resolver_ids_customers(df_clean)

    df_clean = df_clean.fillna("No especificado").astype(str)

    return df_clean

def clean_retail(df):
    df_clean = df.copy()
    df_clean = renombrar_columnas(df_clean, {"customer_id": "transaction_id", "id": "customer_id"})

    if "purchase_date" in df_clean.columns:
        df_clean["purchase_date"] = df_clean["purchase_date"].apply(transformar_fecha)
    if "product_category" in df_clean.columns:
        df_clean["product_category"] = df_clean["product_category"].apply(normalizar_categoria)
    if "amount" in df_clean.columns:
        df_clean["amount"] = df_clean["amount"].apply(transformar_amount)

    if "transaction_id" in df_clean.columns:
        df_clean = resolver_ids_retail(df_clean)

    # 🔑 Al final: reemplazar nulos con "No especificado" y convertir todo a str
    df_clean = df_clean.fillna("No especificado").astype(str)

    return df_clean
