# Retail Analytics System

End-to-end retail analytics project that collects store audit data, stores it in SQLite, generates insights with Pandas, and visualizes results in a Streamlit dashboard.

This repository is designed for portfolio showcase and interview discussions.

## What This Project Demonstrates

- API-driven data ingestion for retail field audits
- Structured storage using SQLite
- Insight generation (low-stock risk, visibility metrics, store-level distribution)
- Interactive dashboard for business-friendly visualization

## Tech Stack

- Python
- FastAPI (backend APIs)
- SQLite (database)
- Pandas (analysis)
- Streamlit (dashboard)

## Architecture

Client/API Request -> FastAPI -> SQLite -> Pandas -> Streamlit Dashboard

## Repository Structure

```text
retail-audit-system/
|- app.py
|- database.py
|- data_generator.py
|- dashboard.py
|- requirements.txt
|- .gitignore
|- README.md
`- screenshots/
```

## Features

- POST endpoint to ingest store audit records
- GET reports endpoint with structured insights:
  - low stock count and items
  - average visibility score
  - store stock distribution
- Streamlit dashboard with:
  - KPI cards
  - low stock table
  - stores needing attention chart
  - stock-by-store chart
  - product distribution chart
  - best performing products chart

## API Endpoints

- `GET /` - health message
- `POST /store-audit` - add one audit record
- `GET /reports` - analytics summary

### Sample Request

```json
{
  "store_id": "S1",
  "product": "Milk",
  "stock": 5,
  "visibility_score": 7,
  "timestamp": "2026-03-24"
}
```

## Quick Start

### 1. Clone

```bash
git clone https://github.com/<your-username>/retail-audit-system.git
cd retail-audit-system
```

### 2. Create and activate virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run backend API

```bash
uvicorn app:app --reload
```

Open API docs at:

- http://127.0.0.1:8000/docs

### 5. Generate sample data (optional)

```bash
python data_generator.py
```

### 6. Run dashboard

```bash
streamlit run dashboard.py
```

Open dashboard at:

- http://localhost:8501

## Dashboard Preview (Important for Recruiters)

### Full Dashboard

![Dashboard Overview](screenshots/dashboard-overview.png)

### KPI + Low Stock Panel

![KPI and Low Stock](screenshots/dashboard-kpi-low-stock.png)

### Store Insights Panel

![Stores Attention and Stock](screenshots/dashboard-store-insights.png)

### Product Insights Panel

![Product Distribution and Performance](screenshots/dashboard-product-insights.png)

If any image is not visible yet, add these files in the `screenshots` folder:

- `screenshots/dashboard-overview.png`
- `screenshots/dashboard-kpi-low-stock.png`
- `screenshots/dashboard-store-insights.png`
- `screenshots/dashboard-product-insights.png`

## Suggested GitHub Repository Settings

- Use repository name: `retail-audit-system`
- Pin this repo on your GitHub profile
- Add topics: `fastapi`, `streamlit`, `pandas`, `sqlite`, `analytics`, `python`

## Future Improvements

- Pydantic request models for stricter validation
- Authentication and role-based access
- PostgreSQL migration for production scale
- Deploy API + dashboard to cloud

## Author

Shivansh
