from PyQt6.QtCore import QSize, pyqtSlot, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit, QTextBrowser


class CentralWidget(QWidget):
    set_value = pyqtSignal(int)

    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.counter = 0

        push_button_abc = QPushButton()
        push_button_abc.setText("Schreibe abc")

        push_button_abc.setIcon(QIcon("ausgebucht.png"))
        push_button_abc.setIconSize(QSize(128, 128))

        # Einfachster Fall für Signal and Slots:
        # Ein Signal wird innerhalb einer Klasse mit einem Slot verbunden.
        # Dafür sind drei Schritte notwendig.
        # 1) Sie wählen das Signal aus. Hier released beim loslassen der Maus.
        # 2) Sie verbinden das Signal mit einem Slot. Den Slot add_abc programmieren wir selbst.
        #    Beachten Sie: - beim Namen des Signals, hier released, stehen keine Klammern.
        #                  - beim Namen des Slots sind auch keine Klammern da.
        #    Aufbau:
        #    Objekt_des_Senders . Name_des_Signals . connect ( Ziel_Slot )
        # 3) Siehe Zeile 52ff
        push_button_abc.released.connect(self.add_abc)
        push_button_abc.pressed.connect(self.temp)

        push_button_xyz = QPushButton("Schreibe xyz")

        push_button_xyz.setIcon(QIcon("schild.png"))
        push_button_xyz.setIconSize(QSize(128, 128))

        push_button_xyz.released.connect(self.add_xyz)
        push_button_xyz.pressed.connect(self.temp)

        self.text_browser = QTextBrowser()

        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_browser.append)

        layout = QGridLayout()
        layout.addWidget(push_button_abc, 1, 1)
        layout.addWidget(push_button_xyz, 1, 2)
        layout.addWidget(self.line_edit, 2, 1, 1, 2)
        layout.addWidget(self.text_browser, 3, 1, 2, 2)

        self.setLayout(layout)

    # Zuerst müssen Sie bei einem eigenen Slot das Schlüsselwort @pyqtSlot() hinzufügen.
    @pyqtSlot()
    # Dann deklarieren Sie die Funktion wie gewohnt in Python.
    def add_abc(self):
        # Hier folgt nun der gewünschte Programmmablauf.
        self.line_edit.setText("abc")

        self.counter += 1
        self.set_value.emit(self.counter)


    @pyqtSlot()
    def add_xyz(self):
        self.line_edit.setText("xyz")

    @pyqtSlot()
    def temp(self):
        self.line_edit.setText("Button ist gedrückt...")
