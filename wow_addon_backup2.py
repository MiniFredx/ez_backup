from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, zipfile


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 176)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Backup Button
        self.buttonAddonBackup = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_backup(self.lineBackupDir.text(), self.lineBackupLocationDir.text()))
        self.buttonAddonBackup.setGeometry(QtCore.QRect(350, 110, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonAddonBackup.setFont(font)
        self.buttonAddonBackup.setObjectName("buttonAddonBackup")
        self.lineBackupDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBackupDir.setGeometry(QtCore.QRect(90, 30, 311, 21))
        self.lineBackupDir.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineBackupDir.setClearButtonEnabled(False)
        self.lineBackupDir.setObjectName("lineBackupDir")
        self.lineBackupLocationDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBackupLocationDir.setGeometry(QtCore.QRect(90, 60, 311, 21))
        self.lineBackupLocationDir.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineBackupLocationDir.setClearButtonEnabled(False)
        self.lineBackupLocationDir.setObjectName("lineBackupLocationDir")
        self.labelAddonDir = QtWidgets.QLabel(self.centralwidget)
        self.labelAddonDir.setGeometry(QtCore.QRect(0, 30, 71, 21))
        self.labelAddonDir.setObjectName("labelAddonDir")
        self.labelBackupDir = QtWidgets.QLabel(self.centralwidget)
        self.labelBackupDir.setGeometry(QtCore.QRect(0, 60, 81, 21))
        self.labelBackupDir.setObjectName("labelBackupDir")
        #Button for the addon dir
        self.toolButton = QtWidgets.QToolButton(self.centralwidget, clicked= lambda: self.press_changeAddonDir())
        self.toolButton.setGeometry(QtCore.QRect(410, 30, 25, 19))
        self.toolButton.setObjectName("toolButton")
        #Button for the addon dir
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget, clicked= lambda: self.press_changeAddonBackupDir())
        self.toolButton_2.setGeometry(QtCore.QRect(410, 60, 25, 19))
        self.toolButton_2.setObjectName("toolButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WoW AddOn Backup"))
        self.buttonAddonBackup.setText(_translate("MainWindow", "Backup AddOns"))
        self.lineBackupDir.setText(_translate("MainWindow", r"C:\Program Files (x86)\World of Warcraft\_retail_\Interface\Addons"))
        #Get the users documents folder path
        self.documents_path = os.environ['USERPROFILE'] + f'\Documents'
        self.lineBackupLocationDir.setText(_translate("MainWindow", self.documents_path))
        self.labelAddonDir.setText(_translate("MainWindow", "Addon Dir:"))
        self.labelBackupDir.setText(_translate("MainWindow", "Backup Location:"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))

    def press_changeAddonDir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        # fileName, _ = QFileDialog.getOpenFileName(QFileDialog(),"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        fileName=QFileDialog.getExistingDirectory(QFileDialog(),"Choose Directory","C:\\", options=options)
        if fileName:
            self.lineBackupDir.setText(QtCore.QDir.toNativeSeparators(fileName))
    def press_changeAddonBackupDir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        # fileName, _ = QFileDialog.getOpenFileName(QFileDialog(),"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        fileName=QFileDialog.getExistingDirectory(QFileDialog(),"Choose Directory","C:\\", options=options)
        if fileName:
            self.lineBackupLocationDir.setText(QtCore.QDir.toNativeSeparators(fileName))



    def press_backup(self, folder, destination):
    # Backup the entire contents of "folder" into a ZIP file.

        folder = os.path.abspath(folder)  # make sure folder is absolute
        os.chdir(destination)

        # Figure out the filename this code should used based on
        # what files already exist.

        number = 1

        while True:
            zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

            if not os.path.exists(zipFilename):
                break
            number = number + 1

        # Create the ZIP file.
        print(f'Creating {zipFilename}...')
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        # Walk the entire folder tree and compress the files in each folder.

        # for foldername, subfolders, filenames in os.walk(os.path.relpath(folder)):
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                print(f'Adding files in {zipFilename}...')
                # Add the current folder to the ZIP file.
                # writing each file one by one
                filename = os.path.join(foldername, filename)
                backupZip.write(filename, filename.replace(folder, ''))

        backupZip.close()
        print('Done.')

        # Pop up box
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Confirmation")
        msg.setText("Your AddOn folder has been backed up to {}.".format(destination))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        # run_it = msg.exec_()
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
