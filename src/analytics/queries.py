import pandas as pd
from sqlalchemy import text
from pathlib import Path
from src.utils.db import get_engine

# Use the shared database connection
engine = get_engine()

# Read SQL file
sql_file = Path("sql/analyses/receiving_td_leaders.sql")
sql_query = sql_file.read_text()

# Execute query and get results as DataFrame
with engine.connect() as conn:
    df = pd.read_sql(text(sql_query), conn)

# Display results
print(df)

