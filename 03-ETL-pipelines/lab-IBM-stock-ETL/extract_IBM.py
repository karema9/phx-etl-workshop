import requests 
import logging
import pandas as pd
# import pprint


logging.basicConfig(level=logging.INFO,filename="py_log.log",format="%(asctime)s %(levelname)s %(message)s", )

def extract_ticker_daily(function:str="TIME_SERIES_DAILY", ticker:str="IBM"):
    """Extract daily time series(date, daily, open, high, low, volume)
      of the global equity specified
      
    Parameters:
        function : time series of your choice, defaults to TIME_SERIES_DAILY
        symbol : ticker symbol of equity of choice, defaults to IBM

    Returns:
        json data of the specified equity
      """
    ENDPOINT = "https://www.alphavantage.co/query"
    KEY = "08QEH6LPOHADA7VX"
    params = {"function" : function,
              "symbol" : ticker,
              "outputsize" : "full",
               "apikey" : KEY}
    try:
        res = requests.get(ENDPOINT, params=params)
        logging.INFO(f"Extracting data from {ENDPOINT}......")
        data = res.json()["Time Series (Daily)"]
        #df = pd.DataFrame(data)
        logging.info(f"Successfully extracted data from {ENDPOINT}")
    except Exception as e:
        logging.info(f"Error {e} while fetching data from {ENDPOINT}")
        #df = pd.DataFrame() # return empty dataframe if exception is raised

    return data


def transform(filename):
    """
    
    """
    data = extract_ticker_daily()

    logging.info("Starting data transformation......")

    # Extract and store dates in an array
    dates_arr =  []
    for dates in data.keys():
      dates_arr.append(dates)

    # Array to store, dictionaries of data
    transformed = []
    for date in dates_arr:
      transformed.append({"date" : dates_arr,
                      "open" : data[date]["1. open"],
                      "high" : data[date]["2. high"],
                      "low" : data[date]["3. low"],
                      "close" : data[date]["4. close"]})
      
    # load the data to a pandas dataframe
    df = pd.DataFrame(transformed)
    # convert date column from object to datatime
    df["date"] = pd.to_datetime(dates_arr)
    # set the datetime column as the index
    df = df.set_index("date")
    # cast all the columns as floats
    for col in df.columns:
       df[f"{col}"] = df[f"{col}"].astype(float)

    return df



if __name__ == "__main__":
    #data = extract_IBM_daily()
    #print(data.head())

   
    df = pd.read_csv("IBM_stock_history.csv")
    df_2 = df.stack(level=1)
    df = df.T
    df.reset_index(inplace=True)
    
    print(df.columns)