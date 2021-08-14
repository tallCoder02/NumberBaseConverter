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
        first_combo.addItem("Binary [Base 2]", "bin")
        first_combo.addItem("Octal [Base 8]", "oct")
        first_combo.addItem("Decimal [Base 10]", "dec")
        first_combo.addItem("Hexadecimal [Base 16]", "hex")
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
            combo1 = first_combo.currentData()
            entry = entry_box.displayText()
            combo2 = second_combo.currentData()

            if entry != "":
                try:
                    if combo1 == combo2:
                        warning_label.setText(entry)
                    elif combo1 == "bin":
                        bin2dec = int(entry, 2)
                        if combo2 == "oct":
                            bin2oct = oct(bin2dec)[2:]  # To get rid of the 0o
                            warning_label.setText(bin2oct)
                        elif combo2 == "dec":
                            warning_label.setText(str(bin2dec))
                        elif combo2 == "hex":
                            bin2hex = hex(bin2dec)[2:].upper()  # To get rid of the 0x
                            warning_label.setText(bin2hex)
                    elif combo1 == "oct":
                        oct2dec = int(entry, 8)
                        if combo2 == "bin":
                            oct2bin = bin(oct2dec)[2:]  # To get rid of the 0b
                            warning_label.setText(oct2bin)
                        elif combo2 == "dec":
                            warning_label.setText(str(oct2dec))
                        elif combo2 == "hex":
                            oct2hex = hex(oct2dec)[2:].upper()  # To get rid of the 0x
                            warning_label.setText(oct2hex)
                    elif combo1 == "dec":
                        if combo2 == "bin":
                            dec2bin = bin(int(entry))[2:]  # To get rid of the 0b
                            warning_label.setText(dec2bin)
                        elif combo2 == "oct":
                            dec2oct = oct(int(entry))[2:]  # To get rid of the 0o
                            warning_label.setText(dec2oct)
                        elif combo2 == "hex":
                            dec2hex = hex(int(entry))[2:].upper()  # To get rid of the 0x
                            warning_label.setText(dec2hex)
                    elif combo1 == "hex":
                        hex2dec = int(entry, 16)
                        if combo2 == "bin":
                            hex2bin = bin(hex2dec)[2:]  # To get rid of the 0b
                            warning_label.setText(hex2bin)
                        elif combo2 == "oct":
                            hex2oct = oct(hex2dec)[2:]  # To get rid of the 0o
                            warning_label.setText(hex2oct)
                        elif combo2 == "dec":
                            warning_label.setText(str(hex2dec))
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
