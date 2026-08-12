import plotly.graph_objects as go
import plotly.express as px
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------- BASIC CHARTS ----------------
def build_year_comparison_chart():
    data = requests.get(f"{API_URL}/stats/year_totals").json()
    years = [item["year"] for item in data]
    totals = [item["total"] for item in data]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=totals, name="Total Expenditure"))
    fig.update_layout(title="Total Expenditure by Year", xaxis_title="Year", yaxis_title="Total")
    return fig

def build_category_pie_chart():
    data = requests.get(f"{API_URL}/stats/category_totals").json()
    labels = [item["cat_code"] for item in data]
    values = [item["total"] for item in data]
    fig = px.pie(names=labels, values=values, title="Category Distribution")
    return fig

def build_stacked_bar_chart():
    data = requests.get(f"{API_URL}/stats/category_totals").json()
    labels = [item["cat_code"] for item in data]
    values = [item["total"] for item in data]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=labels, y=values, name="Total"))
    fig.update_layout(barmode="stack", title="Stacked Category Totals")
    return fig

def build_trend_chart():
    data = requests.get(f"{API_URL}/stats/yearly_trend").json()
    years = [item["year"] for item in data]
    totals = [item["total"] for item in data]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=totals, mode="lines+markers", name="Trend"))
    fig.update_layout(title="Yearly Trend", xaxis_title="Year", yaxis_title="Total")
    return fig

def build_confidence_interval_chart():
    data = requests.get(f"{API_URL}/expenditures").json()
    years = [item["year"] for item in data]
    lower = [item["lower_cib"] for item in data]
    upper = [item["upper_cib"] for item in data]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=lower, fill=None, mode="lines", name="Lower CIB"))
    fig.add_trace(go.Scatter(x=years, y=upper, fill="tonexty", mode="lines", name="Upper CIB"))
    fig.update_layout(title="Confidence Interval Bounds", xaxis_title="Year", yaxis_title="CIB")
    return fig

def build_anomaly_chart():
    data = requests.get(f"{API_URL}/stats/anomalies").json()
    cat = [item["cat_code"] for item in data]
    est = [item["estimate"] for item in data]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cat, y=est, mode="markers", name="Anomalies"))
    fig.update_layout(title="Anomalies by Category", xaxis_title="Category", yaxis_title="Estimate")
    return fig

# ---------------- ADVANCED ANALYTICS ----------------
def build_heatmap_chart():
    data = requests.get(f"{API_URL}/stats/heatmap").json()
    fig = px.imshow(data, text_auto=True, title="Correlation Heatmap")
    return fig

def build_iqr_anomaly_chart():
    data = requests.get(f"{API_URL}/stats/anomalies_iqr").json()
    fig = px.scatter(x=[d["cat_code"] for d in data],
                     y=[d["estimate"] for d in data],
                     title="IQR Anomalies")
    return fig

def build_mad_anomaly_chart():
    data = requests.get(f"{API_URL}/stats/anomalies_mad").json()
    fig = px.scatter(x=[d["cat_code"] for d in data],
                     y=[d["estimate"] for d in data],
                     title="MAD Anomalies")
    return fig

def build_category_trend_chart(cat):
    data = requests.get(f"{API_URL}/stats/category_trends").json()[cat]
    fig = px.line(x=[d["year"] for d in data],
                  y=[d["total"] for d in data],
                  title=f"Trend for Category {cat}")
    return fig
