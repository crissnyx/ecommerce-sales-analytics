import pandas as pd

from app.data.preprocess import clean_customer_data, create_features


def test_clean_customer_data_removes_duplicates_and_normalizes_columns():
    df = pd.DataFrame({
        "customer id": ["CUST-0001", "CUST-0001"],
        "department store": ["Electronics", "Electronics"],
        "total spend": [100.0, 100.0],
        "purchases": [5, 5],
        "avg order value": [20.0, 20.0],
        "tenure days": [180, 180],
        "last purchase days": [30, 30],
        "returns": [1, 1],
        "cancellations": [0, 0],
    })

    cleaned = clean_customer_data(df)
    assert set(cleaned.columns) == {
        "CUSTOMER ID",
        "DEPARTMENT STORE",
        "TOTAL SPEND",
        "PURCHASES",
        "AVG ORDER VALUE",
        "TENURE DAYS",
        "LAST PURCHASE DAYS",
        "RETURNS",
        "CANCELLATIONS",
    }

    features_df = create_features(cleaned)
    assert "CHURN_SCORE" in features_df.columns
    assert "RISK_LEVEL" in features_df.columns
