# tests/test_data_loader.py

from dashboard.data_loader import load_data


def test_load_data():
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
    df = load_data(url)

    assert not df.empty
    assert "Year" in df.columns
    assert "Automobile_Sales" in df.columns
