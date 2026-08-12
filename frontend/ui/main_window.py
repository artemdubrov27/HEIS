from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class MainWindowUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HEIS Dashboard")

        layout = QVBoxLayout()

        title = QLabel("Household Expenditure Intelligence System")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        btn_load = QPushButton("Load CSV into SQL")
        layout.addWidget(btn_load)

        btn_show = QPushButton("Show All Expenditures")
        layout.addWidget(btn_show)

        self.setLayout(layout)
