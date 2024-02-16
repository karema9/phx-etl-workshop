import pandas as pd
import logging
import requests
import httpx

logging.basicConfig(
    level=logging.DEBUG,
    filename = "ingestion-logs.log",
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    )

def ingest_parquet(filename: str) -> pd.DataFrame:
    """Ingest data from a parquet file"""
    try:
        df = pd.read_parquet(filename)
        logging.info(f"{filename} Sucessfully Extracted: {df.shape[0]}")
    except Exception as e:
        logging.exception(f"Error {e}, while ingesting data {filename}")
        df = pd.DataFrame() # return empty dataframe if exception is raised
    return df


def ingest_csv(filepath : str) -> pd.DataFrame:
    """Ingest data from a csv file

    Parameters:
        filename : name or path of the file to be ingested
    Return:
        pandas dataFrame
    """
    try:
        df_csv = pd.read_csv(filepath)
        logging.info(f"{filepath} : extracted {df_csv.shape[0]}")
    except Exception as e:
        logging.exception(f"{filepath} - exception {e} while ingesting data from csv")
        df_csv = pd.DataFrame()
    return df_csv


# using requests library
def ingest_api(api_endpoint : str) -> pd.DataFrame:  
    """Ingest data from an API endpoint
    
    Parameters:
        api_endpoint : URI to ingest data from
    Returns:
        pandas Dataframe containing data
    """
    try:
        res = requests.get(api_endpoint)
        data = res.json()
        df_api = pd.DataFrame(data)
        logging.info(f"{df_api} - extracted from {api_endpoint}")
    except Exception as e:
        logging.error(f"{e} - while ingesting data from {api_endpoint}")
        df_api = pd.DataFrame()
    return df_api


# using the httpx library
def ingest_api_alt(api_endpoint: str) -> pd.DataFrame:
    """Ingest data from api endpoint
    Uses httpx library instead of requests

    Parameters:
        api_endpoint : URI used to ingest data from
    Returns:
        Pandas DataFrame
    """
    try:
        res = httpx.get(api_endpoint)
        data = res.text
        df_api = pd.DataFrame(data)
        logging.info(f"{df_api} - extracted data from {api_endpoint}")
    except Exception as e:
        logging.info(f"Error - {e} - while ingesting data from {api_endpoint}")
        df_api = pd.DataFrame()
    
    return df_api


def ingest_webpage(uri : str, keyword : str) -> pd.DataFrame:
    """Ingest data from a webpage into pandas DataFrame
    
    Parameters:
        uri : link to webpage containing data
        keyword : keyword used to filter data
    Returns:
        Pandas dataframe
    """
    try:
        df_html = pd.read_html(uri, match = keyword)
        df_html = df_html[0]
        logging.info(f"{uri} - ingested {df_html[0]}")
    except Exception as e:
        logging.exception(f"{uri} - exception {e} while ingesting data from {uri}")
        df_html = pd.DataFrame() # return empty dataframe if exception is raised
    return df_html 
















































































































