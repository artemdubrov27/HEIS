from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from .dashboard import Dashboard
from .analytics_panel import AnalyticsPanel
from .filters import Filters
from .tree_view import CategoryTree

class Tabs(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        tabs = QTabWidget()

        tabs.addTab(Dashboard(), "Dashboard")
        tabs.addTab(CategoryTree(), "Categories")
        tabs.addTab(Filters(), "Filters")
        tabs.addTab(AnalyticsPanel(), "Analytics")

        layout.addWidget(tabs)
        self.setLayout(layout)
