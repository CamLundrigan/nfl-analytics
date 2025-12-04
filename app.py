from flask import Flask
import os
from pathlib import Path
import sys
import pandas as pd
from sqlalchemy import text
from src.utils.db import get_engine


project_root = Path(__file__).parent


sys.path.insert(0, str(project_root))


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/stats/<query_name>')
def show_stats(query_name):
    engine = get_engine()
    sql_file = project_root / "sql" / "analyses" / f"{query_name}.sql"
    sql_query = sql_file.read_text()
    with engine.connect() as conn:
        df = pd.read_sql(text(sql_query), conn)
    return df.to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True)