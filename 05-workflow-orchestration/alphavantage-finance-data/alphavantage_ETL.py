from prefect import task, flow
import pandas as pd
import duckdb
import requests
import logging


@task(name="extract_tickers_polygon", log_prints=True, retries=3)
def extract_ticker_daily(function: str = "TIME_SERIES_DAILY", ticker: str = "IBM"):
    """Extract daily time series(date, daily, open, high, low, volume)
      of the global equity specified

    Parameters:
        function : time series of your choice, defaults to TIME_SERIES_DAILY
        symbol : ticker symbol of equity of choice, defaults to IBM

    Returns:
        json data of the specified equity
    """
    ENDPOINT = "https://www.alphavantage.co/query?"
    KEY = "08QEH6LPOHADA7VX"
    params = {
        "function": function,
        "symbol": ticker,
        "outputsize": "full",
        "apikey": KEY,
    }

    logging.info(f"Extracting data from {ENDPOINT}......")
    try:
        res = requests.get(ENDPOINT, params=params)
        data = res.json()
        logging.info(f"Successfully extracted data from {ENDPOINT}")
    except Exception as e:
        print(f"Error {e} while fetching data from {ENDPOINT}")
        data = pd.DataFrame()

    return data


@task(name="transform_raw_data", log_prints=True, retries=3)
def transform(extracted_data):
    """Perform transformation on json file and load to a dataframe

    Parameters:
      data : input data in json format

    Output:
      df : pandas dataframe of transformed data

    """

    filtered_json = extracted_data["Time Series (Daily)"]

    logging.info("Starting data transformation......")

    # Extract and store dates in an array
    dates_arr = []
    for dates in filtered_json.keys():
        dates_arr.append(dates)

    # Flatten the json file
    transformed = []
    for date in dates_arr:
        transformed.append(
            {
                "date": dates_arr,
                "open": filtered_json[date]["1. open"],
                "high": filtered_json[date]["2. high"],
                "low": filtered_json[date]["3. low"],
                "close": filtered_json[date]["4. close"],
            }
        )

    # load the data to a pandas dataframe
    df = pd.DataFrame(transformed)

    # convert date column from object to datatime
    df["date"] = pd.to_datetime(dates_arr)

    # set the datetime column as the index
    df = df.set_index("date")

    # cast all the columns as floats
    for col in df.columns:
        df[f"{col}"] = df[f"{col}"].astype(float)

    logging.info(
        f"Transformations  complete, rows : {df.shape[0]}, columns : {df.shape[1]}"
    )

    return df


@task(name="load transformed data", log_prints=True, retries=3)
def load_to_sql(dataframe, db_name, table_name):
    """Load the cleaned dataframe into a duckdb database"""
    # connect to duckdb
    con = duckdb.connect(db_name)

    # write the dataframe to duckdb
    dataframe.to_sql(name=table_name, con=con, if_exists="replace", index="True")
    print(f"Data succesfully written to {db_name}")


@flow(name="run-pipeline", log_prints=True, retries=3)
def run_alphavantage_pipeline():
    """
    Run the entire ETL pipeline
    """

    raw_df = extract_ticker_daily("TIME_SERIES_DAILY", "AMZN")
    transformed_df = transform(raw_df)
    load_to_sql(transformed_df, "historical-finance.db", "amazon_historical")


if __name__ == "__main__":
    #run_alphavantage_pipeline()
    run_alphavantage_pipeline.serve(name="alphavantage-etl")
