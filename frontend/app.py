import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.tabs import Tabs
from ui.style import STYLE

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HEIS — Household Expenditure Intelligence System")
        self.resize(1400, 900)

        tabs = Tabs()
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
app.setStyleSheet(STYLE)

window = MainApp()
window.show()
app.exec()
