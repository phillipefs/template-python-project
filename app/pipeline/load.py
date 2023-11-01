import pandas as pd 
import os


def save_dataframe(dataframe: pd.DataFrame, path_save: str, file_name:str):
    """
    Save dataframe to excel
    args: 
        dataframe(pd.dataframe): Dataframe to save
        path_save(str): Path save
        file_name(str): File Name
    """
    if not os.path.exists(path_save):
        os.makedirs(path_save)

    dataframe.to_excel(f"{path_save}/{file_name}.xlsx", index=False)
    return "Load Success"