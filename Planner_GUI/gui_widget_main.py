#!/usr/bin/env python
import sys
from PyQt5 import QtGui, QtWidgets, QtCore


#create class for QPix map that just changes picture based on button pressest

class WindowScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.string_of_commands = ''
        self.setWindowTitle("Trajectory Planner")
        self.setGeometry(500, 500, 900, 500)
        self.start_button_settings()
        self.stop_button_settings()
        self.clear_button_settings()
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setReadOnly(True)
        window_horiz = self.init_ui()
        self.setLayout(window_horiz)
        self.show()

    def start_button_settings(self):
        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.setStyleSheet("background-color: green")
        self.start_button.setFixedHeight(70)
        self.start_button.clicked.connect(self.button_click)

    def stop_button_settings(self):
        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.setStyleSheet("background-color: red")
        self.stop_button.setFixedHeight(70)
        self.stop_button.clicked.connect(self.button_click)

    def clear_button_settings(self):
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.setFixedHeight(70)
        self.clear_button.clicked.connect(self.button_click)

    def horizontal_lay(self):
        horizontal = QtWidgets.QHBoxLayout()
        horizontal.stretch(1)
        horizontal.addWidget(self.start_button)
        horizontal.addWidget(self.stop_button)
        horizontal.addWidget(self.clear_button)
        return horizontal

    def image_viewer(self):
        hoops_visual = QtGui.QPixmap("hooplayout.PNG")
        hoops_visual = hoops_visual.scaled(512, 512, QtCore.Qt.KeepAspectRatio)
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
        positions = [(i, j) for i in range(3) for j in range(4)]
        for button_name, position in zip(button_items, positions):
            button = QtWidgets.QPushButton(button_name)
            button.setFixedHeight(50)
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
