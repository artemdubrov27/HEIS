import requests
from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout

API_URL = "https://heis-backend-ihkr.onrender.com"

class CategoryTree(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Category", "Estimate"])

        layout.addWidget(self.tree)
        self.setLayout(layout)

        self.load_categories()

    def load_categories(self):
        data = requests.get(f"{API_URL}/expenditures").json()

        categories = {}

        for item in data:
            cat = item["cat_code"]
            hec = item["hec_code"]

            if cat not in categories:
                categories[cat] = {}

            categories[cat][hec] = item["estimate"]

        for cat, subcats in categories.items():
            cat_item = QTreeWidgetItem([cat])
            self.tree.addTopLevelItem(cat_item)

            for hec, estimate in subcats.items():
                sub_item = QTreeWidgetItem([hec, str(estimate)])
                cat_item.addChild(sub_item)
