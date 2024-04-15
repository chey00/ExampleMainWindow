from PyQt6.QtCore import QSize, pyqtSlot
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        push_button_abc = QPushButton()
        push_button_abc.setText("Schreibe abc")

        push_button_abc.setIcon(QIcon("ausgebucht.png"))
        push_button_abc.setIconSize(QSize(128, 128))

        push_button_abc.released.connect(self.add_abc)
        push_button_abc.pressed.connect(self.temp)

        push_button_xyz = QPushButton("Schreibe xyz")

        push_button_xyz.setIcon(QIcon("schild.png"))
        push_button_xyz.setIconSize(QSize(128, 128))

        push_button_xyz.released.connect(self.add_xyz)
        push_button_xyz.pressed.connect(self.temp)

        self.line_edit = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(push_button_abc, 1, 1)
        layout.addWidget(push_button_xyz, 1, 2)
        layout.addWidget(self.line_edit, 2, 1, 1, 2)

        self.setLayout(layout)

    @pyqtSlot
    def add_abc(self):
        self.line_edit.setText("abc")

    @pyqtSlot
    def add_xyz(self):
        self.line_edit.setText("xyz")

    @pyqtSlot
    def temp(self):
        self.line_edit.setText("Button ist gedrückt...")
