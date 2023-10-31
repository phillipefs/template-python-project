import os
import glob
import pandas as pd
from typing import List


PATH_FILES = "data/input"
def extract_from_excel(path_files: str) -> List[pd.DataFrame]:
    """
    Read files and convert to dataframe.
    agrs: input_path(str): Path folder files
    return: list dataframes
    """
    list_files = glob.glob(os.path.join(path_files, "*.xlsx"))

    list_dataframes = list()
    for file in list_files:
        list_dataframes.append(pd.read_excel(file))

    return list_dataframes