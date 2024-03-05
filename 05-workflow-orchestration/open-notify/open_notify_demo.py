import requests
import pandas as pd
from prefect import task, flow


@task(name="extract-ISS-coordinates", log_prints=True, retries=2)
def get_iss_coordinates():
  """
  Fetch the current coordinates of the ISS

  Returns:
    JSON response containing coordinates
  """
  try:
    res = requests.get("http://api.open-notify.org/iss-now.json")
    data = res.json()
    print("Request successful")
  except Exception as e:
    print(f"Exception {e} while fetching ISS coordinates")
    data = "Error"    
  
  return data


@task(name="Flatten JSON", log_prints=True, retries=2)
def transform_coords(response):
  """
  Extract the relevant data from the JSON
  
  Returns:
    coordinates_dict = dictionary object containing coordinates and timestamp
  """
  coordinates_dict = {
                      'timestamp' : response['timestamp'],
                      'latitude' : response['iss_position']['latitude'],
                      'longitude' : response['iss_position']['longitude']
                      }

  return coordinates_dict


@flow(name="ISS-coordinates", log_prints=True, retries=2)
def run_functions():
  raw_coordinates = get_iss_coordinates()
  transformed = transform_coords(raw_coordinates)

  arr = []
  arr.append(transformed)

  coords_df = pd.DataFrame(arr)

  print(coords_df.shape[0])


if __name__ == "__main__":
    run_functions.serve(name="Open Notify Demo",
                      cron = "* * * * *",
                     tags = ["open-notify", "ISS coordinates"]
                       )
  #run_functions()





