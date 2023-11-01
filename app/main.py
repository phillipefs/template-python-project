from pipeline.extract import extract_from_excel
from pipeline.transform import concatenate_dataframes
from pipeline.load import save_dataframe



if __name__ == '__main__':
    dataframes_list = extract_from_excel("data/input")
    df_full = concatenate_dataframes(dataframes_list)
    save_dataframe(df_full, "data/output", "consolidate_file")