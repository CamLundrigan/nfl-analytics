import nflreadpy as nfl
import pandas as pd
import os
from sqlalchemy import create_engine
import datetime as dt
from dotenv import load_dotenv


load_dotenv()  # loads .env from the current working directory
# Load current season play-by-play data
year=dt.date.today().year
pbp = nfl.load_pbp(year).to_pandas()


# Build SQLAlchemy engine from environment
pg_user = os.getenv("POSTGRES_USER")
pg_pass = os.getenv("POSTGRES_PASSWORD")
pg_host = os.getenv("POSTGRES_HOST")
pg_port = os.getenv("POSTGRES_PORT", "5432")
pg_db   = os.getenv("POSTGRES_DB")




engine = create_engine(
    f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
)

# Upload to database
pbp.to_sql('nfl_pbp', engine, if_exists='replace', index=False)

print("Data loaded successfully")