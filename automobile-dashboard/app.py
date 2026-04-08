from dashboard import create_app

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

if __name__ == "__main__":
    app = create_app(DATA_URL)
    app.run(debug=False)
