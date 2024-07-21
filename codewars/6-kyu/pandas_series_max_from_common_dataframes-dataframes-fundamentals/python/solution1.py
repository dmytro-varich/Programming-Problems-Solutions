import pandas as pd

def max_common(df_a: pd.DataFrame, df_b: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df_a, df_b])[df_a.columns].groupby(level=0).max()
