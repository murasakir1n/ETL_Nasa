import pandas as pd
import sqlalchemy
import requests
import psycopg2

# Extract data from API and save it's as json file

try:
    request = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=v2mzSBrfsOPEbfHb44bkcnkWLgoCCgyRAZAen3FC")
    response = request.json()
    status_code = request.status_code
except Exception as e:
    print(f"Error: {e}\nStatus code: {status_code}")