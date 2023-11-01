import pytest
import pandas as pd

@pytest.fixture
def df_fixture():
    return pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

@pytest.fixture
def output_fixture():
    return ("data/output/", "output")

from app.pipeline.load import save_dataframe

def test_load_to_excel(df_fixture, output_fixture):
    """Test using Arrange, Act, Assert pattern."""
    output_folder, output_file = output_fixture

    # Arrange
    expected = "Load Success"

    # Act salve o result em um temp file

    result = save_dataframe(df_fixture, output_folder, output_file)

    # Assert
    assert result == expected