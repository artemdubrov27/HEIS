# HEIS - High-level Expense Intelligence System

HEIS is a modern analytical application designed for exploring, visualizing, and understanding expenditure data.  
It combines a **FastAPI backend** with a **PySide6 desktop frontend**, providing interactive charts, anomaly detection, category insights, and statistical analysis.

---

## Overview

HEIS loads financial datasets (CSV/XLSX), stores them in a local SQLite database, and exposes analytical endpoints through FastAPI.  
The PySide6 GUI connects to these endpoints to display dynamic Plotly charts and detailed analytics.

The system is modular, scalable, and suitable for both personal finance analysis and academic research.

---

## Features

### Backend (FastAPI)
- REST API for accessing and filtering expenditure data
- Endpoints for:
  - Year totals
  - Category totals
  - Trend analysis
  - Confidence intervals
  - RSE (Relative Standard Error)
  - IQR anomaly detection
  - MAD anomaly detection
  - Heatmaps
- SQLite database integration
- Automatic data loading from CSV/Excel
- Clean modular architecture (routes, models, schemas, analytics)

### Frontend (PySide6)
- Tab-based interface:
  - **Dashboard** - year comparison, pie charts, stacked bars, trends, CI, anomalies
  - **Analytics** - RSE, IQR, MAD, heatmaps
  - **Filters** - filter by year, category, or amount range
  - **Categories** - hierarchical tree view
- Interactive Plotly charts embedded directly into PySide6 widgets
- Responsive layout and modern UI design

---

## Technologies Used

| Layer | Technologies |
|-------|-------------|
| Backend | FastAPI, Uvicorn, SQLAlchemy, Pydantic |
| Frontend | PySide6, Plotly, Requests |
| Database | SQLite |
| Data Formats | CSV, XLSX |

---

## Installation & Setup

### 1️ - Clone the repository
```bash
git clone https://github.com/<artemdubrov27>/HEIS.git
cd HEIS 
```

### 2 - Create and activate a virtual environment
bash
python -m venv venv
.\venv\Scripts\Activate.ps1

### 3 - Install dependencies
bash
pip install -r requirements.txt

### 4️ - Run the backend
bash
uvicorn backend.main:app --reload

### 5️ - Run the frontend
bash
cd frontend
python app.py

---

## How It Works
1.The backend loads expenditure data from CSV/Excel into SQLite.
2.FastAPI exposes analytical endpoints for statistical processing.
3.The frontend requests these endpoints and visualizes results using Plotly.
4.Users can interactively explore trends, anomalies, and category breakdowns.

---

## Deployment (Render)
HEIS is fully compatible with Render Free Tier (512 MB RAM).
The backend typically consumes ~150 MB RAM, making it ideal for lightweight cloud deployment.

---

## License
MIT License - free for personal and commercial use.

---

## Contributions
Contributions are welcome!
Feel free to submit pull requests or open issues for improvements, bug fixes, or new features.



