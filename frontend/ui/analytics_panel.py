from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .charts import (
    build_trend_chart,
    build_confidence_interval_chart,
    build_anomaly_chart,
    build_heatmap_chart,
    build_iqr_anomaly_chart,
    build_mad_anomaly_chart
)
from .plot_widget import PlotWidget
import requests

API_URL = "http://127.0.0.1:8000"

class AnalyticsPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Basic stats
        rse_stats = requests.get(f"{API_URL}/stats/rse").json()
        anomalies = requests.get(f"{API_URL}/stats/anomalies").json()

        layout.addWidget(QLabel("Analytics Overview"))
        layout.addWidget(QLabel(f"Average RSE: {rse_stats['average_rse']}"))
        layout.addWidget(QLabel(f"Max RSE: {rse_stats['max_rse']}"))
        layout.addWidget(QLabel(f"Min RSE: {rse_stats['min_rse']}"))
        layout.addWidget(QLabel(f"Anomalies detected: {len(anomalies)}"))

        # Trend chart
        layout.addWidget(QLabel("Yearly Trend"))
        layout.addWidget(PlotWidget(build_trend_chart()))

        # Confidence Interval chart
        layout.addWidget(QLabel("Confidence Interval Chart"))
        layout.addWidget(PlotWidget(build_confidence_interval_chart()))

        # Basic anomaly chart
        layout.addWidget(QLabel("Anomaly Chart"))
        layout.addWidget(PlotWidget(build_anomaly_chart()))

        # Heatmap
        layout.addWidget(QLabel("Correlation Heatmap"))
        layout.addWidget(PlotWidget(build_heatmap_chart()))

        # IQR anomalies
        layout.addWidget(QLabel("IQR Anomalies"))
        layout.addWidget(PlotWidget(build_iqr_anomaly_chart()))

        # MAD anomalies
        layout.addWidget(QLabel("MAD Anomalies"))
        layout.addWidget(PlotWidget(build_mad_anomaly_chart()))

        self.setLayout(layout)
