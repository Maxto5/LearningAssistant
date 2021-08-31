import sys
import sqlite3 as lite
import pyrebase

import qrc_resourses

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, \
    QGridLayout, QLineEdit, QDialog, \
    QDesktopWidget, QAction, QMenuBar, QMenu, QTableWidget, QStackedWidget, QToolBar, QGroupBox, \
    QDialogButtonBox, QFormLayout, QTableWidgetItem, QSizePolicy, QHeaderView, QRadioButton, QButtonGroup, QCheckBox, \
    QTextEdit

firebaseConfig = {
    "apiKey": "AIzaSyAaTAc9C6O0o04zRkluiUpmYpsPXDPcSnE",
    "authDomain": "learning-assistant-c4f0c.firebaseapp.com",
    "databaseURL": "https://learning-assistant-c4f0c-default-rtdb.firebaseio.com",
    "projectId": "learning-assistant-c4f0c",
    "storageBucket": "learning-assistant-c4f0c.appspot.com",
    "messagingSenderId": "975200946254",
    "appId": "1:975200946254:web:b5f6308192bda1d1bf9b1f",
    "measurementId": "G-KR2V6DB0Z3"
}

firebase = pyrebase.initialize_app(firebaseConfig)


# Launcher Window with Logo and Button
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

    def btn_clicked(self):
        print("proceeding to login")
        self.window.show()
        self.close()


# The main window accessible to those who login
class Operation(QMainWindow):
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __init__(self, parent=None):
        super(Operation, self).__init__(parent)

        self.resize(450, 350)

        self.setWindowTitle('CUK Learning Assistant')
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolbars()
        self._createStatusbar()
        self._connectActions()
        self.center()

        option = Option(self)
        self.centralWidget.addWidget(option)

    def viewer(self):
        viewer = Viewer(self)
        self.centralWidget.addWidget(viewer)
        self.centralWidget.setCurrentWidget(viewer)

    def manager(self):
        manager = Manager(self)
        self.centralWidget.addWidget(manager)
        self.centralWidget.setCurrentWidget(manager)

    def home(self):
        option = Option(self)
        self.centralWidget.addWidget(option)
        self.centralWidget.setCurrentWidget(option)

    def about(self):
        self.window = About()
        self.window.show()

    def review(self):
        self.window = Review()
        self.window.show()

    def credit(self):
        self.window = Credits()
        self.window.show()

    def _createMenuBar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)
        file_menu.addAction(self.newAction)
        file_menu.addAction(self.saveAction)
        file_menu.addAction(self.exitAction)

        fileHelp = QMenu("&Help", self)
        menu_bar.addMenu(fileHelp)
        fileHelp.addAction(self.docAction)
        fileHelp.addAction(self.onlineAction)

        fileAbout = QMenu("&About", self)
        menu_bar.addMenu(fileAbout)
        fileAbout.addAction(self.aboutAction)
        fileAbout.addAction(self.creditAction)

    def _createStatusbar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready", 2000)

    def _createToolbars(self):
        topToolbar = QToolBar("&Home", self)
        topToolbar.setMovable(False)

        spacer1 = QWidget(self)
        spacer1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer2 = QWidget(self)
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer3 = QWidget(self)
        spacer3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer4 = QWidget(self)
        spacer4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.addToolBar(Qt.TopToolBarArea, topToolbar)

        topToolbar.addWidget(spacer1)
        topToolbar.addAction(self.backAction)
        topToolbar.addWidget(spacer2)
        topToolbar.addAction(self.homeAction)
        topToolbar.addWidget(spacer3)
        topToolbar.addAction(self.nextAction)
        topToolbar.addWidget(spacer4)
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
        self.backAction = QAction(QIcon(":file-back.jpeg"), "&Management", self)
        self.nextAction = QAction(QIcon(":file-next.jpeg"), "&Viewer", self)
        self.helpAction = QAction(QIcon(":file-help.jpeg"), "&Review", self)

    def _connectActions(self):
        self.homeAction.triggered.connect(self.home)
        self.backAction.triggered.connect(self.manager)
        self.nextAction.triggered.connect(self.viewer)
        self.exitAction.triggered.connect(self.close)
        self.aboutAction.triggered.connect(self.about)
        self.helpAction.triggered.connect(self.review)
        self.creditAction.triggered.connect(self.credit)

    def closeEvent(self, event):
        self.close()


# Window with option either viewer or management
class Option(QWidget):

    def __init__(self, parent=None):
        super(Option, self).__init__(parent)
        self.setMinimumSize(800, 350)
        self.initUI()

    def initUI(self):
        Management = QLabel(self)
        Viewer = QLabel(self)

        mngmt = "<h4>Lecture Management</h4>" \
                " Lecture Management mode offers a simple interface for lecture Management \n" \
                "<ul type=square><li>In this mode the Lecturer can send notifications to the student </li>" \
                "<li> You may make use of the provided templates or writing a custom message </li>" \
                "<li>The communications sent to the subscribers  will be received in realtime</li>" \
                "</br> </ul>" \
                "<i>Use The left &lt;- Arrow to access this mode</i> "

        viewer = "<h4>Timetable viewer</h4>" \
                 "The Viewer(Timetable viewer) is intended to offer an interface for the lecturer to browse the " \
                 "timetable " \
                 "This is crucial in case of need to reschedule a class to a later time" \
                 "<ul type=circle> " \
                 "<li>The Lecturer can view the class view of the timetable for an intended class</li>" \
                 "<li>The lecturer can also see the weekly timetable view of their own or other lecturers " \
                 "schedules </li></ul>" \
                 "</br><i>Use the right -&gt; arrow to access this mode </i> "

        Management.setText(mngmt)
        Management.setWordWrap(True)
        Management.setStyleSheet("padding-left:20px;border:1px solid white;border-radius:18px")

        Viewer.setText(viewer)
        Viewer.setWordWrap(True)
        Viewer.setStyleSheet("padding-left:20px;border:1px solid white;border-radius:18px")

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        vbox.addWidget(Management)
        vbox.addWidget(Viewer)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


# Login DialogBox  using pyrebase email/password authentication
class Login(QDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.window = Operation()
        self.window0 = Viewer()
        self.window1 = Error()
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

        emailLabel = QLabel('&Email', self)
        self.emailLineEdit = QLineEdit(self)
        emailLabel.setBuddy(self.emailLineEdit)

        passwordLabel = QLabel('&Password', self)
        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordLabel.setBuddy(self.passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnOK.clicked.connect(self.btnok_clicked)

        btnCancel = QPushButton('&Cancel')
        btnCancel.clicked.connect(self.btnCancel_clicked)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(emailLabel, 0, 0)
        mainLayout.addWidget(self.emailLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        mainLayout.addWidget(label4, 3, 1, 1, 3)

    def btnok_clicked(self):
        print("Lecturer Logged in")
        #self.window.show()
        self.login()
        #self.accept()

    def btnCancel_clicked(self):
        print("going back to home page")
        self.window0.show()
        #self.accept()

    def closeEvent(self, event):
        self.accept()

    def login(self):

        try:
            auth = firebase.auth()
            email = self.emailLineEdit.text()
            password = self.passwordLineEdit.text()
            auth.sign_in_with_email_and_password(email, password)
            print("Successfully /logged in")
            self.window.show()
            self.accept()

        except:
            print("Invalid email or password")
            self.window1.show()





# Window providing for querying the sqlite Database and displaying results to the table widget
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
        self.table.setHorizontalHeaderLabels(
            ['Unit Code', 'Unit Title', 'Class', 'Size', 'Mode', 'Lecturer', 'Day', 'Time', 'Venue'])
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header = self.table.horizontalHeader()
        # header.setSectionResizeMode(1 ,QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeToContents)

        buttonbox1 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox1.accepted.connect(self.btn_student_clicked)
        buttonbox1.rejected.connect(self._input_reset1)

        buttonbox2 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox2.accepted.connect(self.btn_lecturer_clicked)
        buttonbox2.rejected.connect(self._input_reset2)

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
        bottom.stretch(2)

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

    def _input_reset2(self):
        print("resetting")
        self.LecturerNameLineEdit.clear()

    def _input_reset1(self):
        self.sessionLineEdit.clear()
        self.courseLineEdit.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        self.close()


# window providing for sending information to the students
class Manager(QWidget):

    def __init__(self, parent=None):
        super(Manager, self).__init__(parent)
        self.setMinimumSize(700, 400)
        # self.center()
        self.mngmt_Button = QPushButton('SEND')
        self.initUI()

    def initUI(self):
        # mngmt_Button.clicked.connect(self.btnViewer_clicked)

        Management = QLabel(self)
        Audience = QLabel(self)
        audience = "<center><h4><b>Target Students: </b></h4> </center>"
        Audience.setText(audience)
        Audience.setStyleSheet("font-family:arial")

        Viewer = QLabel(self)

        courseLabel = QLabel(self)
        courseLineEdit = QLineEdit(self)
        courseLabel.setText("Course")

        sessionLabel = QLabel(self)
        sessionLineEdit = QLineEdit(self)
        sessionLabel.setText("session")

        mngmt = "<center><h4>Lecture State</h4></center>Provide clarification about the Lecture attendance "

        viewer = "<center><h4>Lecture Activity</h4></center>Please Provide Details of the scheduled Lecture Activity"

        Management.setText(mngmt)
        Management.setWordWrap(True)
        Management.setStyleSheet("font-family:arial;padding-left:20px;")

        Viewer.setText(viewer)
        Viewer.setWordWrap(True)
        Viewer.setStyleSheet("font-family:arial;padding-left:20px;")

        # Checkboxes
        layout1 = QVBoxLayout()
        self.b1 = QCheckBox("Class")
        self.b1.setChecked(False)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        layout1.addWidget(self.b1)

        self.b2 = QCheckBox("CAT")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        layout1.addWidget(self.b2)

        self.b3 = QCheckBox("LAB PRACTICAL")
        self.b3.toggled.connect(lambda: self.btnstate(self.b3))
        layout1.addWidget(self.b3)

        self.b4 = QCheckBox("GUIDED ASSIGNMENT")
        self.b4.toggled.connect(lambda: self.btnstate(self.b4))
        layout1.addWidget(self.b4)

        # RadioButtons
        layout = QVBoxLayout()  # layout for the central widget
        widget = QWidget(self)  # central widget
        widget.setLayout(layout)

        number_group = QButtonGroup(widget)  # Number group
        r0 = QRadioButton("On Schedule")
        number_group.addButton(r0)
        r1 = QRadioButton("Possible Delay")
        number_group.addButton(r1)
        r2 = QRadioButton("Postponed")
        number_group.addButton(r2)

        layout.addWidget(r0)
        layout.addWidget(r1)
        layout.addWidget(r2)

        message = QTextEdit(self)
        messageLabel = QLabel(self)
        messageLabel.setText("Enter Custom Message to convey")

        vbox = QVBoxLayout()
        top_hbox = QHBoxLayout()
        top_hbox2 = QHBoxLayout()
        hbox1 = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()

        # hbox.addStretch(1)
        vbox1.addWidget(Management)
        vbox1.addWidget(widget)
        vbox2.addWidget(Viewer)
        vbox2.addLayout(layout1)

        # vbox.addStretch(1)
        top_hbox2.addWidget(Audience)
        top_hbox.addWidget(courseLabel)
        top_hbox.addWidget(courseLineEdit)
        top_hbox.addWidget(sessionLabel)
        top_hbox.addWidget(sessionLineEdit)

        vbox3.addWidget(messageLabel)
        vbox3.addWidget(message)
        vbox3.addWidget(self.mngmt_Button, 1)

        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)

        vbox.addLayout(top_hbox2)
        vbox.addLayout(top_hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(vbox3)

        self.setLayout(vbox)

    def btnstate(self, b):
        if b.text() == "Button1":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        if b.text() == "Button2":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")


# About App in the menu menu
class About(QDialog):
    def __init__(self):
        super().__init__()
        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        abt = "<center>Learning Assistant Desktop</center>" \
              "<ul>" \
              "<li>Built Using PyQT {Python Bindings for the C++ QT GUI Framework}</li>" \
              "<li>Database Used is SQLite3 Database</li>" \
              "<li>Pyrebase: Firebase python Implementation is used for the login</li>" \
              "</ul>"

        mail = QLabel(
            "For Support and Enquiries contact: <a href='mailto:wafula.barasa@student.cuk.ac.ke'>Barasa Mathews</a>",
            self)
        mail.setOpenExternalLinks(True)
        mail.setAlignment(Qt.AlignCenter)
        label2 = QLabel(self)
        label2.setText(abt)
        label2.setWordWrap(True)
        label2.setStyleSheet("font-family:nimbus;font-size:12px")
        label3 = QLabel(self)

        label3.setToolTip('Hint')
        label3.setPixmap(QPixmap("logo.jpeg"))

        vbox = QVBoxLayout()
        vbox.addWidget(label3)
        vbox.addWidget(label2)
        vbox.addWidget(mail)

        self.setLayout(vbox)
        self.setWindowTitle('Learning Assistant')
        self.setMaximumSize(400, 400)
        self.setMinimumSize(400, 400)
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))


# App Review
class Review(QDialog):
    def __init__(self):
        super().__init__()
        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        app_abt = "<center> <u>Learning Assistant Desktop</u></center> \n A  PC Application program  for use by the C.U.K Lecturers and Students" \
                  "<ul type='circle'> <li> It is specifically suited for lecturer use since it provides a window for Lecture Management</li>" \
                  "<li> Students may also use it since the viewer can be acccessed without having to login</li></ul>"

        features = "The following are some of the app features" \
                   "<ul>" \
                   "<li> Viewer: An interface to custom query the timetable and selective retrieval </li>" \
                   "<li> Management: An interface for generating and sending communication to students<li> </ul>"

        app_review_p1 = QLabel(self)
        app_review_p1.setText(app_abt)
        app_review_p1.setWordWrap(True)

        app_review_p2 = QLabel(self)
        app_review_p2.setText(features)
        app_review_p2.setWordWrap(True)

        vbox = QHBoxLayout(self)
        vbox.addWidget(app_review_p1)
        vbox.addWidget(app_review_p2)

        self.setLayout(vbox)
        self.setWindowTitle('App Review')
        self.setMaximumSize(600, 200)
        self.setMinimumSize(600, 200)


# List of Group Members
class Credits(QDialog):
    def __init__(self):
        super().__init__()
        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        credits = "<u> Group Members</u>" \
             "<ul type='circle'> " \
                  "<li> Barasa Mathews</li>" \
                  "<li> Kipyegon Dennis</li>" \
                  "<li> Munyua Pius</li>" \
                  "<li> Kariuki Kevin</li>" \
                  "<li> Kimanii Titus</li>" \
                  "<li> Jane Wangari</li></ul>"

        app_review_p1 = QLabel(self)
        app_review_p1.setText(credits)
        app_review_p1.setWordWrap(True)

        vbox = QHBoxLayout(self)
        vbox.addWidget(app_review_p1)

        self.setLayout(vbox)
        self.setWindowTitle('Members')
        self.setMaximumSize(200, 200)
        self.setMinimumSize(200, 200)
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))


class Error(QDialog):
    def __init__(self):
        super().__init__()
        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        msg = "Invalid email or password"

        app_review_p1 = QLabel(self)
        app_review_p1.setText(msg)
        app_review_p1.setWordWrap(True)

        vbox = QHBoxLayout(self)
        vbox.addWidget(app_review_p1)

        self.setLayout(vbox)
        self.setWindowTitle('login error')
        self.setMaximumSize(200, 100)
        self.setMinimumSize(200, 100)
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Home()
    mainWindow.show()
    sys.exit(app.exec_())
