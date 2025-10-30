import nflreadpy as nfl
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Load current season play-by-play data
pbp = nfl.load_pbp().to_pandas()
print(pbp.columns.tolist())

# Create connection to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="NFL-STATS",
    user="postgres",
    password="STINKY"
)

# Upload to database
pbp.to_sql('nfl_pbp', conn, if_exists='replace', index=False)

print("Data loaded successfully")