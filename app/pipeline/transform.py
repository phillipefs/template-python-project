import pandas as pd
from typing import List

def concatenate_dataframes(list_dataframes: List[pd.DataFrame])->pd.DataFrame:
    return pd.concat(list_dataframes, ignore_index=True)



