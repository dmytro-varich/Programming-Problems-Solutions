import pandas as pd

def rename_columns(df: pd.DataFrame, names: tuple) -> pd.DataFrame:  
    df2 = df.copy()
    df2.columns = names
    return df2
