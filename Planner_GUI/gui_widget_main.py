#!/usr/bin/env python
import sys
from PyQt5 import QtGui, QtWidgets


class WindowScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.string_of_commands = ''
        self.setWindowTitle("Trajectory Planner")
        self.setGeometry(300, 300, 300, 300)
        self.start_button = QtWidgets.QPushButton("Start")
        self.stop_button = QtWidgets.QPushButton("Stop")
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.start_button.clicked.connect(self.button_click)
        self.stop_button.clicked.connect(self.button_click)
        self.clear_button.clicked.connect(self.button_click)
        self.line_edit = QtWidgets.QLineEdit()
        window_horiz = self.init_ui()
        self.setLayout(window_horiz)
        self.show()

    def horizontal_lay(self):
        horizontal = QtWidgets.QHBoxLayout()
        horizontal.stretch(1)
        horizontal.addWidget(self.start_button)
        horizontal.addWidget(self.stop_button)
        horizontal.addWidget(self.clear_button)
        return horizontal

    def image_viewer(self):
        hoops_visual = QtGui.QPixmap("white.png")
        label_hoops = QtWidgets.QLabel(self)
        label_hoops.setPixmap(hoops_visual)
        return label_hoops

    def button_click(self):
        sender = self.sender()
        if sender.text() == "Clear":
            self.line_edit.clear()
            self.string_of_commands = ''

    def command_click(self, button_list):
        sender = self.sender()
        if sender.text() in button_list:
            self.string_of_commands = self.string_of_commands + sender.text()
            self.line_edit.setText(str(self.string_of_commands))

    def init_ui(self):
        grid = QtWidgets.QGridLayout()
        horizontal_layout = self.horizontal_lay()

        button_items = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']
        positions = [(i, j) for i in range(2) for j in range(5)]
        for button_name, position in zip(button_items, positions):
            button = QtWidgets.QPushButton(button_name)
            button.clicked.connect(lambda: self.command_click(button_items))
            grid.addWidget(button, *position)
        label_hoops = self.image_viewer()
        vertical_layout_1 = QtWidgets.QVBoxLayout()
        vertical_layout_1.addWidget(label_hoops)
        vertical_layout_1.addWidget(self.line_edit)
        vertical_layout_2 = QtWidgets.QVBoxLayout()
        vertical_layout_2.addLayout(grid)
        vertical_layout_2.addLayout(horizontal_layout)
        window_horizontal = QtWidgets.QHBoxLayout()
        window_horizontal.addLayout(vertical_layout_1)
        window_horizontal.addLayout(vertical_layout_2)
        return window_horizontal


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowScreen()
    sys.exit(app.exec_())
