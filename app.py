import os
import sys
import pathlib

from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox

# ------------------------ End of Python & PySide imports --------------------------- #

os.environ['JAVA_HOME'] = str(pathlib.Path('target/jdk').resolve())

import jnius_config

jnius_config.set_classpath('target/app/PythonJavaExample.jar')

from jnius import autoclass

# ------------------------ End of Pyjnius imports ---------------------------------- #


def button_slot(message, window):
    return QMessageBox.information(window, 'Message', message)


if __name__ == '__main__':
    main_class = autoclass("pythonjavaexample.Main")
    main_object = main_class()
    message = main_object.sayHello()

    # -------------------- End of Java bridge code -------------------------------- #

    app = QApplication()

    window = QPushButton('Push Me')
    window.resize(600, 400)
    window.show()

    window.clicked.connect(lambda: button_slot(message, window))

    sys.exit(app.exec())