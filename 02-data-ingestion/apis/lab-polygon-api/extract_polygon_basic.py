import pandas as pd
import requests


def extract_companies_overview(endpoint: str, api_key: str):
    """
    Extract company information, financial ratios and other key metrics for the equity
    specified

    Parameters:
       endpoint(str) :
       api_key(str) :

    Return:
       DataFrame containing company's overview information
    """
    API_KEY = "<enter-your-api-key>"
    parameters = {
        "count": 500,
        "apiKey": API_KEY,
    }
    # make a get request to the api endpoint
    try:
        response = requests.get(endpoint, params=parameters)
        data = response.json()["results"]
        df = pd.DataFrame(data)

    except Exception as e:
        print(f"Error {e} while fetching data from dataframe")

    return df


if __name__ == "__main__":
    auth_key = "one9fzytfjoE67utMkopidSJDQ9s5p37"
    data = extract_companies_overview(
        "https://api.polygon.io/v3/reference/tickers", auth_key
    )
    data["last_updated_utc"] = pd.to_datetime(data.last_updated_utc)
    print(data.head())

