import pandas as pd

def flatten(dataframe: pd.DataFrame, col: str) -> pd.DataFrame: 
    return dataframe.explode(col).reset_index(drop=True)
