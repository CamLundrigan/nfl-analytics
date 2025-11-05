# NFL Analytics Project

A data analytics project combining SQL and Python to analyze NFL statistics, with plans for a web application front-end.

## Project Goals

- Learn SQL and Python together through hands-on data analytics
- Analyze NFL player and team performance using real data
- Create queries that provide insights into player comparisons and team analysis
- Build predictive models and comparative analytics
- Eventually develop a web application front-end for interactive data exploration

## Technology Stack

- **Data Source**: `nflreadpy` - Python library for accessing NFL data from nflverse
- **Database**: PostgreSQL - Store and query play-by-play data
- **Backend**: Python (pandas, SQLAlchemy) - Data processing and analysis
- **Frontend**: Flask (planned) - Web application for displaying stats

## Project Structure

```
nfl-analytics/
├── src/
│   ├── ingest/          # Data loading scripts
│   ├── analytics/        # Python scripts that execute SQL queries
│   └── utils/            # Shared utilities (database connections)
├── sql/
│   └── analyses/        # Saved SQL query files
├── templates/           # HTML templates for web app (planned)
└── app.py              # Flask web application (planned)
```

## Current Features

- Load play-by-play data from nflreadpy into PostgreSQL
- Execute SQL queries to analyze player statistics
- Query receiving touchdown leaders and other player metrics

## Planned Features

- Multiple SQL queries for various player/team statistics
- Player comparison tools
- Team performance analysis
- Web interface for selecting and viewing different stats
- Interactive filtering and search capabilities

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Required packages (see `requirements.txt`)

### Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` file with PostgreSQL credentials
3. Load data: `python src/ingest/load_data.py`
4. Run queries: `python src/analytics/queries.py`

## Learning Approach

This project emphasizes hands-on learning of SQL and Python through:
- Writing and executing SQL queries
- Understanding database structures
- Using Python for data processing and analysis
- Building towards a complete web application

