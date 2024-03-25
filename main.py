from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Title
        self.setWindowTitle("Simple Number Base Converter")

        # Layout
        self.setLayout(qtw.QVBoxLayout())

        # Label
        label = qtw.QLabel("Convert ")
        label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(label)

        # Entry Box
        entry_box = qtw.QLineEdit()
        entry_box.setObjectName("EntryBox")
        self.layout().addWidget(entry_box)

        # Label1
        first_label = qtw.QLabel("From: ")
        first_label.setFont(qtg.QFont('Helvetica', 18))  # Font Size
        self.layout().addWidget(first_label)

        # Combo Box 1
        first_combo = qtw.QComboBox(self)
        #           Combo Box Items
        first_combo.addItems([
            "Base 2 [Binary]",
            "Base 3 [Ternary]",
            "Base 4 [Quaternary]",
            "Base 5 [Quinary]",
            "Base 6 [Senary]",
            "Base 7 [Septenary]",
            "Base 8 [Octal]",
            "Base 9 [Nonary]",
            "Base 10 [Decimal]",
            "Base 11 [Undecimal]",
            "Base 12 [Duodecimal]",
            "Base 13 [Tridecimal]",
            "Base 14 [Tetradecimal]",
            "Base 15 [Pentadecimal]",
            "Base 16 [Hexadecimal]"
        ])
        self.layout().addWidget(first_combo)

        # Label2
        second_label = qtw.QLabel("To: ")
        second_label.setFont(qtg.QFont('Helvetica', 18))  # Font Size
        self.layout().addWidget(second_label)

        # Combo Box 2
        second_combo = qtw.QComboBox(self)
        #           Combo Box Items
        second_combo.addItem("Base 2 [Binary]", "bin")
        second_combo.addItem("Base 8 [Octal]", "oct")
        second_combo.addItem("Base 10 [Decimal]", "dec")
        second_combo.addItem("Base 16 [Hexadecimal]", "hex")
        self.layout().addWidget(second_combo)

        # Button
        button = qtw.QPushButton("Convert!", clicked=lambda: converter())
        self.layout().addWidget(button)

        # Warning/Answer
        warning_label = qtw.QLabel("")
        warning_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(warning_label)

        # Display
        self.show()

        def converter():
            combo1 = first_combo.currentIndex() + 2
            entry = entry_box.displayText().upper()
            combo2 = second_combo.currentIndex()

            if entry != "":
                try:
                    entry_10 = int(entry, combo1)
                    systems_dict = {0: 2, 1: 8, 2: 10, 3: 16}
                    systems_dict_console = {0: "bin", 1: "oct", 3: "hex"}
                    if combo2 != 2:
                        dec2 = eval(f'{systems_dict_console[combo2]}({entry_10})')[
                            2:].upper()
                        warning_label.setText(
                            f'{entry}<sub>{combo1}</sub> = {dec2}<sub>{systems_dict[combo2]}</sub>')
                    else:
                        warning_label.setText(
                            f'{entry}<sub>{combo1}</sub> = {entry_10}<sub>{10}</sub>')
                except ValueError:
                    warning_label.setText('Invalid Input!!!')
                except Exception as e:
                    # Funnily enough, I'm pretty sure this is unnecessary. 🤔
                    print(f'Error: {e}')
            else:
                warning_label.setText("Entry box cannot be empty!!!")


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
