from PySide6.QtWidgets import QWidget, QVBoxLayout
import plotly.io as pio

class PlotWidget(QWidget):
    def __init__(self, fig):
        super().__init__()
        layout = QVBoxLayout()
        pio.show(fig)
        self.setLayout(layout)
