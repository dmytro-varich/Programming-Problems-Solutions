import pandas as pd

def filter_dataframe(df: pd.DataFrame, col: str, func) -> pd.DataFrame: 
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is not present in the DataFrame.")
        
    re_func = lambda x: ~df[col].apply(func)
    filter_ = re_func(df[col])
    return pd.DataFrame(df[filter_])
