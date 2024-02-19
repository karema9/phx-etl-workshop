## Capstone project

---

For the capstone project, you are to extract data from two sources, *yfinance* and *polygon* API.

The architecture diagram for the project is shown below:

![](/home/c99/Desktop/data-projects/phx-etl-workshop/capstone-project/capstone-project-architecture.png)

### Extraction

You are to extract data from two sources, yfinance and polygon API.

- From polygon API, extract all the tickers and their details that are supported by Polygon API - the tickers are 100.

- Using the list of tickers extracted from Polygon API, extract the historical period data of the tickers symbols, extract all the data for the maximum period of each company.

### Transformation

Clean the data - changing the data types, dropping unwanted columns , and transform it to conform to the schema of the data warehouse that will be provided.

### Load

Load the data into duckdb, ensure that the data is persistent.


#### Deliverables

You should be able to perform some queries on the data warehouse that you have built.

BONUS : you can dockerize your data pipeline. Note, there are no additional points for dockerizing you pipelines.
