from typing import List

import pandas as pd


def concatenate_dataframes(
    list_dataframes: List[pd.DataFrame],
) -> pd.DataFrame:
    return pd.concat(list_dataframes, ignore_index=True)
