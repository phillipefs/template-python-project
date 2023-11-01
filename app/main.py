from pipeline.extract import extract_from_excel
from pipeline.load import save_dataframe
from pipeline.transform import concatenate_dataframes

if __name__ == '__main__':
    dataframes_list = extract_from_excel('data/input')
    df_full = concatenate_dataframes(dataframes_list)
    save_dataframe(df_full, 'data/output', 'consolidate_file')
