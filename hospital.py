import os
import data
from data import *
from file import *
from val import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QAction, QStyledItemDelegate
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import doctor
import patient
import schedule

class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        with open('config/config.json') as f:
            config = json.load(f)
        self.cnx = data.connect_sql(config)
        data.connect_database(self.cnx,config['database_name'])
        self.cursor = self.cnx.cursor()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(899, 749)
        icon = QtGui.QIcon()
        self.setWindowIcon(QtGui.QIcon("./icon/logo.png"))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        delegate = ReadOnlyDelegate(self)
        self.tableWidget.setItemDelegateForColumn(0, delegate)
        self.tableWidget.setItemDelegateForColumn(1, delegate)
        self.tableWidget.setItemDelegateForColumn(2, delegate)
        self.tableWidget.setItemDelegateForColumn(3, delegate)
        self.tableWidget.setItemDelegateForColumn(4, delegate)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 701, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 100, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 150, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 370, 741, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 671, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 39, 541, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 30, 571, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 70, 571, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 110, 571, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 150, 571, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuPrograms = QtWidgets.QMenu(self.menubar)
        self.menuPrograms.setObjectName("menuPrograms")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionConfig = QtWidgets.QAction(self)
        self.actionConfig = QAction(QtGui.QIcon("./icon/set.png"), "&Your button", self)
        self.actionConfig.setObjectName("actionConfig")
        self.actionDoctor = QtWidgets.QAction(self)
        self.actionDoctor = QAction(QtGui.QIcon("./icon/set.png"), "&Your button", self)
        self.actionDoctor.setObjectName("actionDoctor")
        self.actionPatient = QtWidgets.QAction(self)
        self.actionPatient = QAction(QtGui.QIcon("./icon/set.png"), "&Your button", self)
        self.actionPatient.setObjectName("actionPatient")
        self.actionSchedule = QtWidgets.QAction(self)
        self.actionSchedule = QAction(QtGui.QIcon("./icon/set.png"), "&Your button", self)
        self.actionSchedule.setObjectName("actionSchedule")
        self.menuSetting.addAction(self.actionConfig)
        self.menuPrograms.addAction(self.actionDoctor)
        self.menuPrograms.addAction(self.actionPatient)
        self.menuPrograms.addAction(self.actionSchedule)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuPrograms.menuAction())
        self.actionConfig.triggered.connect(self.config)
        self.actionDoctor.triggered.connect(self.open_doctor)
        self.actionPatient.triggered.connect(self.open_patient)
        self.actionSchedule.triggered.connect(self.open_schedule)

        self.init_data(data.get_all_records(self.cnx.cursor(),'hospital'))
        self.pushButton.clicked.connect(self.import_button_click)
        self.pushButton_2.clicked.connect(self.export_button_click)
        self.pushButton_3.clicked.connect(self.search_hospital)
        self.pushButton_4.clicked.connect(self.add_hospital)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Hospital Manage"))
        self.label.setText(_translate("MainWindow", "Hospitals"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Delete"))

        self.pushButton.setText(_translate("MainWindow", "Import"))
        self.pushButton_2.setText(_translate("MainWindow", "Export"))
        self.groupBox.setTitle(_translate("MainWindow", "Search hospital"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.pushButton_3.setText(_translate("MainWindow", "Search hospital"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Search"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Phone:"))
        self.label_5.setText(_translate("MainWindow", "Address:"))
        self.label_6.setText(_translate("MainWindow", "Description:"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add new"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuPrograms.setTitle(_translate("MainWindow", "Programs"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
        self.actionDoctor.setText(_translate("MainWindow", "Doctor"))
        self.actionPatient.setText(_translate("MainWindow", "Patient"))
        self.actionSchedule.setText(_translate("MainWindow", "Schedule"))

    def config(self):
        filename = 'config/config.json'
        with open(filename) as f:
            data = json.load(f)
            os.system('notepad.exe {}'.format(filename))
            print(data)
            data['user']
            self.cnx = mysql.connector.connect(host=data['host'], database=data['database_name'], user=data['user'],
                                               password=data['password'])


    def open_doctor(self):
        self.ui_doctor = doctor.Ui_MainWindow()
        self.ui_doctor.setupUi()
        self.ui_doctor.show()

    def open_patient(self):
        self.ui_patient = patient.Ui_MainWindow()
        self.ui_patient.setupUi()
        self.ui_patient.show()

    def open_schedule(self):
        self.ui_schedule = schedule.Ui_MainWindow()
        self.ui_schedule.setupUi()
        self.ui_schedule.show()

    def init_data(self,results):
        for i in range(0, len(results)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(results[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(results[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(results[i][2])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(results[i][3])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(results[i][4])))

            self.detail_btn = QtWidgets.QPushButton(self)
            self.detail_btn.clicked.connect(self.edit_btn_click)
            self.detail_btn.setText("Edit")
            self.tableWidget.setCellWidget(i, 5, self.detail_btn)

            self.detail_btn = QtWidgets.QPushButton(self)
            self.detail_btn.clicked.connect(self.delete_btn_click)
            self.detail_btn.setText("Delete")
            self.tableWidget.setCellWidget(i, 6, self.detail_btn)

    def search_hospital(self):
        name_input = self.lineEdit.text()
        result = data.search_by_name(self.cursor, 'hospital',name_input)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        if len(result) != 0:
            self.init_data(result)
        else:
            QMessageBox.information(self, 'Message', 'Nothing found!', QMessageBox.Close)

    def edit_btn_click(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id_index = table_model.index(index.row(), 0)
        id = table_model.data(id_index)
        name_index = table_model.index(index.row(), 1)
        name = table_model.data(name_index)
        phone_index = table_model.index(index.row(), 2)
        phone = table_model.data(phone_index)
        address_index = table_model.index(index.row(), 3)
        address = table_model.data(address_index)
        description_index = table_model.index(index.row(), 4)
        description = table_model.data(description_index)
        print(id, name, phone, address, description)
        labels = ('name', 'phone', 'address', 'description')
        values = (name, phone, address, description)
        update_by_id(self.cnx,'hospital', labels, values, id)

    def add_hospital(self):
        name = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        if not valid_phone(phone):
            QMessageBox.information(self, 'Error', 'Phone is not valid', QMessageBox.Close)
            return
        address = self.lineEdit_4.text()
        descrip = self.lineEdit_5.text()
        labels = ('name', 'phone', 'address', 'description')
        values = (name, phone, address, descrip)
        if insert_table(self.cnx, 'hospital', labels, values):
            result = get_last_n_rows(self.cnx.cursor(), 'hospital', 1)
            if result:
                self.init_data(result)

    def delete_btn_click(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id_index = table_model.index(index.row(), 0)
        id = table_model.data(id_index)
        print(id)
        name_index = table_model.index(index.row(), 1)
        name = table_model.data(name_index)
        ques = QMessageBox.question(self, 'System', f'Are you sure you want to delete hospital: {name}?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ques == QMessageBox.Yes:
            if delete_by_id(self.cnx, 'hospital', id):
                QMessageBox.about(self, "System", f"Successfully delete the hospital: {name}")
                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(0)
                self.init_data(data.get_all_records(self.cnx.cursor(),'hospital'))
            else:
                QMessageBox.about(self, "System", "Delete failed, try again")



    def import_button_click(self):
        try:
            Tk().withdraw()
            fname = askopenfilename()
            if fname == '':
                return False

            tail = re.findall("[.]{1}\w+$", fname)[0]
            if not tail == '.xlsx':
                QMessageBox.information(self, 'Error', 'Must be an excel file', QMessageBox.Close)
                return False

            df = load_from_file(fname).fillna('')
            count = 0
            attributes = ('name', 'phone', 'address', 'description')
            for i in range(len(df)):
                name = str(df.iloc[i]['name'])
                phone = str(df.iloc[i]['phone'])
                if not valid_phone(phone):
                    continue

                address = str(df.iloc[i]['address'])
                description = str(df.iloc[i]['description'])
                values = [name, phone, address, description]
                count += 1
                insert_table(self.cnx, 'hospital', attributes, values)

            records = get_last_n_rows(self.cnx.cursor(), 'hospital', count)
            QMessageBox.information(self, 'Success', 'Import successfully', QMessageBox.Close)
        except:
            print('Error')

    def export_button_click(self):
        try:
            records = get_all_records(self.cnx.cursor(), 'hospital')
            attributes = ('id', 'name', 'phone', 'address', 'description')
            save_to_file('hospital', records, attributes)
            return True
        except:
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
