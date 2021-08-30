import sys
import sqlite3 as lite
import qrc_resourses

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, \
    QGridLayout, QLineEdit, QDialog, \
    QDesktopWidget, QAction, QMenuBar, QMenu, QTableWidget, QStackedWidget, QToolBar, QSpinBox, QGroupBox, \
    QDialogButtonBox, QFormLayout, QTableWidgetItem


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.window = Login()
        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        label3 = QLabel(self)

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('Hint')
        label3.setPixmap(QPixmap("uni_logo.png"))

        btn = QPushButton("Proceed")
        btn.move(64, 32)
        btn.clicked.connect(self.btn_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(label3)
        vbox.addWidget(btn)

        self.setLayout(vbox)
        self.setWindowTitle('Learning Assistant')
        self.setMaximumSize(400, 400)
        self.setMinimumSize(400, 400)
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.resize(500, 500)
        self.move(450, 150)

    def btn_clicked(self):
        print("proceeding to login")
        self.window.show()
        self.close()


class Operation(QMainWindow):
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __init__(self, parent=None):
        super(Operation, self).__init__(parent)

        self.resize(450, 350)
        # self.window = Login()
        self.setWindowTitle('Operation mode Option')
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolbars()
        self._createStatusbar()
        self.center()

        option = Option(self)
        self.centralWidget.addWidget(option)
        option.ViewerButton.clicked.connect(self.viewer)

    def viewer(self):
        viewer = Viewer(self)
        self.centralWidget.addWidget(viewer)
        self.centralWidget.setCurrentWidget(viewer)

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        fileHelp = QMenu("&Help", self)
        menuBar.addMenu(fileHelp)
        fileHelp.addAction(self.docAction)
        fileHelp.addAction(self.onlineAction)

        fileAbout = QMenu("&About", self)
        menuBar.addMenu(fileAbout)
        fileAbout.addAction(self.aboutAction)
        fileAbout.addAction(self.creditAction)

    def _createStatusbar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready", 2000)

    def _createToolbars(self):
        topToolbar = QToolBar("&Home", self)
        topToolbar.setMovable(False)

        self.addToolBar(Qt.TopToolBarArea, topToolbar)

        topToolbar.addAction(self.homeAction)
        topToolbar.addAction(self.backAction)

        self.fontsizeSpinbox = QSpinBox()
        self.fontsizeSpinbox.setFocusPolicy(Qt.NoFocus)
        topToolbar.addWidget(self.fontsizeSpinbox)

        topToolbar.addAction(self.nextAction)
        topToolbar.addAction(self.helpAction)

    def _createActions(self):
        # file
        self.newAction = QAction("&New", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        # Help
        self.docAction = QAction("&Documentation", self)
        self.onlineAction = QAction("& Online Docs", self)
        # About
        self.aboutAction = QAction("&About App", self)
        self.creditAction = QAction("&Credits", self)

        # toolbar Actions
        self.homeAction = QAction(QIcon(":file-home.jpeg"), "&Home", self)
        self.backAction = QAction(QIcon(":file-back.jpeg"), "&Back", self)
        self.nextAction = QAction(QIcon(":file-next.jpeg"), "&Next", self)
        self.helpAction = QAction(QIcon(":file-help.jpeg"), "&Help", self)

    def closeEvent(self, event):
        self.close()


class Option(QWidget):

    def __init__(self, parent=None):
        super(Option, self).__init__(parent)
        self.setMinimumSize(700,400)
        #self.center()
        self.MngtButton = QPushButton('Management')
        self.ViewerButton = QPushButton('Viewer')
        self.initUI()

        # self.window = Viewer()

    def initUI(self):
        # ViewerButton.clicked.connect(self.btnViewer_clicked)

        Management = QLabel(self)
        Viewer = QLabel(self)

        mngmt = "<h4>Lecture Management</h4>" \
                " Lecture Management mode offers a simple interface for lecture Management \n" \
                "<ul type=square><li>In this mode the Lecturer can send notifications to the student </li>" \
                "<li> You msy make use of the provided templates or writing a custom message </li>" \
                "<li>The communications sent to the subscribers  will be received in realtime</li>" \
                "</ul>"

        viewer = "<h4>Timetable viewer</h4>" \
                 "The Viewer(Timetable viewer) is intended to offer an interface for the lecturer to browse the " \
                 "timetable " \
                 "This is crucial in case of need to reschedule a class to a later time" \
                 "<ul type=circle> " \
                 "<li>The Lecturer can view the class view of the timetable for an intended class</li>" \
                 "<li>The lecturer can also see the weekly timetable view of their own or other lecturers " \
                 "schedules</li></ul> "

        Management.setText(mngmt)
        Management.setWordWrap(True)
        Management.setStyleSheet("padding-left:20px;border:1px solid white;border-radius:18px")

        Viewer.setText(viewer)
        Viewer.setWordWrap(True)
        Viewer.setStyleSheet("padding-left:20px;border:1px solid white;border-radius:18px")

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        # hbox.addStretch(1)
        vbox.addWidget(Management)
        hbox.addWidget(self.MngtButton, 1)
        vbox.addWidget(Viewer)
        hbox.addWidget(self.ViewerButton, 1)

        # vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Login(QDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.window = Operation()
        self.window0 = Viewer()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lecturer Login')
        self.setFixedWidth(250)
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        label4 = QLabel("<a href='#'>Forgot Password</a>", self)
        label4.setOpenExternalLinks(True)
        label4.setBuddy(self)
        label4.setBuddy(label4)

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnOK.clicked.connect(self.btnok_clicked)

        btnCancel = QPushButton('&Cancel')
        btnCancel.clicked.connect(self.btnCancel_clicked)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        mainLayout.addWidget(label4, 3, 1, 1, 3)

    def btnok_clicked(self):
        print("Lecturer Loggeg in")
        self.window.show()
        self.accept()

    def btnCancel_clicked(self):
        print("going back to home page")
        self.window0.show()
        self.accept()

    def closeEvent(self, event):
        self.accept()


class Viewer(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.resize(925, 400)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Viewer')
        self.center()
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.courseLineEdit = QLineEdit()
        self.sessionLineEdit = QLineEdit()
        self.LecturerNameLineEdit = QLineEdit()
        # self.LecturerNumberLineEdit = QLineEdit()
        self.formGroupBox2 = QGroupBox("Lecturer Query")
        self.formGroupBox1 = QGroupBox("Student Query")

        self.create_student_form()
        self.create_lecturer_form()

        self.table = QTableWidget()
        self.table.setColumnCount(9)

        buttonbox1 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Reset)
        buttonbox1.accepted.connect(self.btn_student_clicked)
        # self.buttonbox.rejected.connect(self.reject)

        buttonbox2 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Reset)
        buttonbox2.accepted.connect(self.btn_lecturer_clicked)
        # self.buttonbox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()

        top = QVBoxLayout()
        sub_main_top = QHBoxLayout()
        sub_top_1 = QVBoxLayout()
        sub_top_2 = QVBoxLayout()

        sub_top_1.addWidget(self.formGroupBox1)
        sub_top_1.addWidget(buttonbox1)
        sub_top_2.addWidget(self.formGroupBox2)
        sub_top_2.addWidget(buttonbox2)

        sub_main_top.addLayout(sub_top_2)
        sub_main_top.addLayout(sub_top_1)

        bottom = QHBoxLayout()
        bottom.addWidget(self.table)

        top.addLayout(sub_main_top)

        mainLayout.addLayout(top)
        mainLayout.addLayout(bottom)

        self.setLayout(mainLayout)

    def create_student_form(self):
        form_layout = QFormLayout()
        form_layout.addRow(QLabel('Course'), self.courseLineEdit)
        form_layout.addRow(QLabel('session'), self.sessionLineEdit)
        self.formGroupBox1.setLayout(form_layout)

    def create_lecturer_form(self):
        form_layout = QFormLayout()
        form_layout.addRow(QLabel('Lecturer_name'), self.LecturerNameLineEdit)
        # form_layout.addRow(QLabel('Lecturer_number'), self.LecturerNumberLineEdit)
        self.formGroupBox2.setLayout(form_layout)

    def btnok_clicked(self):
        print("Lecturer Query")

    def btn_student_clicked(self):
        print("Student Query")
        con = None

        try:
            con = lite.connect('timetable.db')
            cur = con.cursor()
            key = str(self.courseLineEdit.text() + " " + self.sessionLineEdit.text())
            print(str(key))
            cur.execute('''SELECT * FROM timetable  where session = ''' + " \"" + key + "\"")
            self.table.setRowCount(0)

            for row, form in enumerate(cur):
                self.table.insertRow(row)
                for column, item in enumerate(form):
                    self.table.setItem(row, column, QTableWidgetItem(str(item)))

        except lite.Error as e:
            print("Error %s:" % e.args[0])
            sys.exit(1)
        finally:
            if con:
                con.close()

    def btn_lecturer_clicked(self):
        print("Lecturer Query")
        con = None

        try:
            key = self.LecturerNameLineEdit.text()
            print(key)
            con = lite.connect('timetable.db')
            cur = con.cursor()
            cur.execute('''SELECT * FROM timetable  where lecturer_name = ''' + " \"" + key + "\"")
            self.table.setRowCount(0)

            for row, form in enumerate(cur):
                self.table.insertRow(row)
                for column, item in enumerate(form):
                    self.table.setItem(row, column, QTableWidgetItem(str(item)))

        except lite.Error as e:
            print("Error %s:" % e.args[0])
            sys.exit(1)
        finally:
            if con:
                con.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Home()
    mainWindow.show()
    sys.exit(app.exec_())
