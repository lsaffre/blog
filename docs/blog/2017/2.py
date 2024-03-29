import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
                             QDesktopWidget, QMainWindow, QAction, qApp,
                             QTextEdit, QHBoxLayout, QVBoxLayout)
# from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class DetailForm(QWidget):

    def __init__(self, title="Detail Form"):
        super().__init__()
        self.setWindowTitle(title)
        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        # self.show()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.setGeometry(300, 300, 300, 220)
        self.center()
        self.setWindowTitle('2.py')
        self.setWindowIcon(QIcon('../../.static/logo.png'))
        self.setToolTip('This is a <b>QWidget</b> widget')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

        a = QAction(QIcon('detail.png'), '&Detail', self)
        a.triggered.connect(self.show_detail)
        fileMenu.addAction(a)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # btn = QPushButton('Quit', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)

        self.show()

        self.statusBar().showMessage('Ready')

    def show_detail(self, event):
        self.detail_form = DetailForm()
        self.detail_form.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, 'MessageBox', "This will close the window! Are you sure?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
