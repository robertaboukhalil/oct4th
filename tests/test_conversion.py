import numpy as np
import pandas as pd
import oct4th

TEST_CSV = "./data/test.csv"
TEST_XLSX = "./data/test.xlsx"


def test_conversion():
    # Run the conversion
    oct4th.csv_to_xlsx(
        file_in=TEST_CSV,
        file_out=TEST_XLSX,
        force=True
    )

    # Load result
    df = pd.read_excel(io=TEST_XLSX, sheet_name="Sheet1")
    print(df)

    # Make sure genes weren't changed to dates
    assert df.GeneName.tolist() == ['TP53', 'OCT4', 'DEC1', 'MARCH1', 'MARCH2', 'MARC2']
    # Make sure the numbers weren't stored as text
    assert df.SomeValue.dtypes == np.float64
