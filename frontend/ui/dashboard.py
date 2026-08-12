from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .charts import (
    build_year_comparison_chart,
    build_category_pie_chart,
    build_stacked_bar_chart,
    build_trend_chart,
    build_confidence_interval_chart,
    build_anomaly_chart
)
from .plot_widget import PlotWidget

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Dashboard — Key Visualizations"))

        layout.addWidget(QLabel("Total Expenditure by Year"))
        layout.addWidget(PlotWidget(build_year_comparison_chart()))

        layout.addWidget(QLabel("Category Distribution"))
        layout.addWidget(PlotWidget(build_category_pie_chart()))

        layout.addWidget(QLabel("Stacked Category Totals"))
        layout.addWidget(PlotWidget(build_stacked_bar_chart()))

        layout.addWidget(QLabel("Yearly Trend"))
        layout.addWidget(PlotWidget(build_trend_chart()))

        layout.addWidget(QLabel("Confidence Interval Bounds"))
        layout.addWidget(PlotWidget(build_confidence_interval_chart()))

        layout.addWidget(QLabel("Detected Anomalies"))
        layout.addWidget(PlotWidget(build_anomaly_chart()))

        self.setLayout(layout)
