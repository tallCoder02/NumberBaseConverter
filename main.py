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
            "Binary [Base 2]",
            "3",
            "4",
            "5",
            "6",
            "7",
            "Octal [Base 8]",
            "9",
            "Decimal [Base 10]",
            "11",
            "12",
            "13",
            "14",
            "15",
            "Hexadecimal [Base 16]"
            ])
        self.layout().addWidget(first_combo)

        # Label2
        second_label = qtw.QLabel("To: ")
        second_label.setFont(qtg.QFont('Helvetica', 18))  # Font Size
        self.layout().addWidget(second_label)

        # Combo Box 2
        second_combo = qtw.QComboBox(self)
        #           Combo Box Items
        second_combo.addItem("Binary [Base 2]", "bin")
        second_combo.addItem("Octal [Base 8]", "oct")
        second_combo.addItem("Decimal [Base 10]", "dec")
        second_combo.addItem("Hexadecimal [Base 16]", "hex")
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
            entry = entry_box.displayText()
            combo2 = second_combo.currentData()

            if entry != "":
                try:
                    entry_10 = int(entry, combo1)
                    if combo2 == "bin":
                        dec2bin = bin(int(entry_10))[2:]  # To get rid of the 0b
                        warning_label.setText(dec2bin)
                    elif combo2 == "oct":
                        dec2oct = oct(int(entry_10))[2:]  # To get rid of the 0o
                        warning_label.setText(dec2oct)
                    elif combo2 == "hex":
                        dec2hex = hex(int(entry_10))[2:].upper()  # To get rid of the 0x
                        warning_label.setText(dec2hex)
                    elif combo2 == "dec":
                        warning_label.setText(str(entry_10))
                except ValueError:
                    warning_label.setText('Invalid Input!!!')
                except Exception as e:
                    print(f'Error: {e}')  # Funnily enough, I'm pretty sure this is unnecessary. 🤔
            else:
                warning_label.setText("Entry box cannot be empty!!!")


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
