import pandas as pd
from sqlalchemy import text
from pathlib import Path
import sys

# Add project root to Python path so imports work
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.db import get_engine

# Use the shared database connection
engine = get_engine()

# Read SQL file (relative to project root)
sql_file = project_root / "sql" / "analyses" / "receiving_td_leaders.sql"
sql_query = sql_file.read_text()

# Execute query and get results as DataFrame
with engine.connect() as conn:
    df = pd.read_sql(text(sql_query), conn)

# Display results
print(df)

