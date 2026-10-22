import pandas as pd

from app.data.loader import load_csv


def test_load_csv_reads_data(tmp_path):
    file_path = tmp_path / "customers.csv"
    df = pd.DataFrame({
        "CUSTOMER ID": ["CUST-0001"],
        "DEPARTMENT STORE": ["Electronics"],
        "TOTAL SPEND": [100.0],
        "PURCHASES": [5],
        "AVG ORDER VALUE": [20.0],
        "TENURE DAYS": [180],
        "LAST PURCHASE DAYS": [30],
        "RETURNS": [1],
        "CANCELLATIONS": [0],
    })
    df.to_csv(file_path, index=False)

    loaded_df = load_csv(file_path)
    assert list(loaded_df.columns) == list(df.columns)
    assert len(loaded_df) == 1
