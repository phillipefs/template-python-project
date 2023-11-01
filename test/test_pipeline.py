import pandas as pd

from app.pipeline.transform import concatenate_dataframes

df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})


def test_concatenate_dfs():
    """
    Test function concat dataframes
    """
    df = concatenate_dataframes([df1, df2])
    assert df.shape == (4, 2)
