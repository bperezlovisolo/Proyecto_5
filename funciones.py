import pandas as pd

def dataset_overview(df):
    print("Shape")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    
    print("Data Types")
    print(df.dtypes.value_counts())
    
    print("Missing Values")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values")

def col_numericas(df):
    num_df = df.select_dtypes(include=['int64', 'float64'])
    
    summary = num_df.describe().T
    summary['skew'] = num_df.skew()
    
    return summary

def col_categoricas(df):
    cat_df = df.select_dtypes(include=['object'])
    
    summary = cat_df.describe().T
    summary['unique'] = cat_df.nunique()
    
    return summary

def drop_columns (df, columns):
    df.drop(columns, axis=1, inplace=True)

def contar_duplicados(df):
    """
    Determina el número de filas duplicadas en un DataFrame de pandas.
    
    Args:
    df (pd.DataFrame): El DataFrame en el que se buscarán duplicados.
    
    Returns:
    int: El número de filas duplicadas en el DataFrame.
    """
    num_duplicados = df.duplicated().sum()
    print(f"El DataFrame tiene {num_duplicados} filas duplicadas.")

    num_duplicados_perc = round(num_duplicados / df.shape[0] * 100, 2)
    print(f"Esto equivale a un: {num_duplicados_perc} %.\n")
    
    return num_duplicados



# Ejemplo de uso:
# num_duplicados = contar_duplicados(df)