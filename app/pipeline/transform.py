from typing import List

import pandas as pd


def concatenate_dataframes(
    list_dataframes: List[pd.DataFrame],
) -> pd.DataFrame:
    """
    Concatenate list dataframes
    args:
        list_dataframes(List[pd.DataFrame]): List Dataframes
    """
    return pd.concat(list_dataframes, ignore_index=True)
