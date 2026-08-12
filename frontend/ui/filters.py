from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
import requests

API_URL = "http://127.0.0.1:8000"

class Filters(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Year filter
        year_box = QHBoxLayout()
        self.year_input = QLineEdit()
        btn_year = QPushButton("Filter by Year")
        btn_year.clicked.connect(self.filter_year)
        year_box.addWidget(QLabel("Year:"))
        year_box.addWidget(self.year_input)
        year_box.addWidget(btn_year)
        layout.addLayout(year_box)

        # Category filter
        cat_box = QHBoxLayout()
        self.cat_input = QLineEdit()
        btn_cat = QPushButton("Filter by Category")
        btn_cat.clicked.connect(self.filter_category)
        cat_box.addWidget(QLabel("Category:"))
        cat_box.addWidget(self.cat_input)
        cat_box.addWidget(btn_cat)
        layout.addLayout(cat_box)

        # Range filter
        range_box = QHBoxLayout()
        self.low_input = QLineEdit()
        self.high_input = QLineEdit()
        btn_range = QPushButton("Filter by Range")
        btn_range.clicked.connect(self.filter_range)
        range_box.addWidget(QLabel("Low:"))
        range_box.addWidget(self.low_input)
        range_box.addWidget(QLabel("High:"))
        range_box.addWidget(self.high_input)
        range_box.addWidget(btn_range)
        layout.addLayout(range_box)

        self.setLayout(layout)

    def filter_year(self):
        year = self.year_input.text()
        print(requests.get(f"{API_URL}/expenditures/year/{year}").json())

    def filter_category(self):
        cat = self.cat_input.text()
        print(requests.get(f"{API_URL}/expenditures/category/{cat}").json())

    def filter_range(self):
        low = self.low_input.text()
        high = self.high_input.text()
        print(requests.get(f"{API_URL}/expenditures/range/{low}/{high}").json())
