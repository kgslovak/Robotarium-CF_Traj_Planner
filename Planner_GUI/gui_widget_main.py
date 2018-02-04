#!/usr/bin/env python
import sys
from PyQt5 import QtGui, QtWidgets


class WindowScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Trajectory Planner")
        grid = QtWidgets.QGridLayout()
        startbutton = QtWidgets.QPushButton("Start")
        stopbutton = QtWidgets.QPushButton("Stop")
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.stretch(1)
        horizontal_layout.addWidget(startbutton)
        horizontal_layout.addWidget(stopbutton)

        button_output = QtWidgets.QLabel("[string of clicks goes here]")
        button_items = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']
        positions = [(i, j) for i in range(2) for j in range(5)]
        for button_name, position in zip(button_items, positions):
            button = QtWidgets.QPushButton(button_name)
            grid.addWidget(button, *position)
        hoops_visual = QtGui.QPixmap("white.png")
        label_hoops = QtWidgets.QLabel(self)
        label_hoops.setPixmap(hoops_visual)
        window_horizontal = QtWidgets.QHBoxLayout()
        # window_horizontal.addWidget(label_hoops)
        vertical_layout_1 = QtWidgets.QVBoxLayout()
        vertical_layout_1.addWidget(label_hoops)
        vertical_layout_1.addWidget(button_output)
        vertical_layout_2 = QtWidgets.QVBoxLayout()
        vertical_layout_2.addLayout(grid)
        vertical_layout_2.addLayout(horizontal_layout)
        window_horizontal.addLayout(vertical_layout_1)
        window_horizontal.addLayout(vertical_layout_2)
        self.setGeometry(300, 300, 300, 300)
        self.setLayout(window_horizontal)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowScreen()
    sys.exit(app.exec_())
