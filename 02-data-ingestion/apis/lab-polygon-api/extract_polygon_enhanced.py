import pandas as pd
import requests
import logging

# This extraction script utilizes logging for observability
# define the top level loggin module
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s",filename="polygon-api.log")


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
    parameters = {
        "count": 500,
        "apiKey": api_key,
    }
    # make a get request to the api endpoint
    try:
        logging.info(f"Extracting companies data from {endpoint}.....")
        response = requests.get(endpoint, params=parameters)
        data = response.json()["results"]
        df = pd.DataFrame(data)
        logging.info("Extraction successfull")

    except Exception as e:
        print(f"Error {e} while fetching data from dataframe")
        logging.exception(f"Error {e} while extracting data")

    return df


if __name__ == "__main__":
    auth_key = "<your-api-key>"
    data = extract_companies_overview(
        "https://api.polygon.io/v3/reference/tickers", auth_key
    )
    data["last_updated_utc"] = pd.to_datetime(data.last_updated_utc)
    print(data.columns)
