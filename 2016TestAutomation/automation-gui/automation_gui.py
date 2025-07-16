import sys
import os
import configparser
import threading
import nose

from PyQt4 import QtGui, QtCore, uic

import steps
from steps.base_module import BaseModule

form_class = uic.loadUiType('geofeedia-automation.ui')[0]
exitFlag = 0


class AutomationGUI(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        config = configparser.ConfigParser()
        config.read('config.ini')

        drives_model = QtGui.QFileSystemModel(self)
        drives_model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Dirs | QtCore.QDir.Files)
        drives_model.setRootPath(config.get('BASE_PATH', 'PATH'))
        self.tv_folder_view.setModel(drives_model)
        self.tv_folder_view.setRootIndex(drives_model.index(QtCore.QDir.homePath()))
        self.tv_folder_view.hideColumn(1)
        self.tv_folder_view.hideColumn(2)
        self.tv_folder_view.hideColumn(3)

        env = [i[1] for i in config.items('ENVIRONMENTS')]
        self.cb_environment.addItems(env)
        self.cb_browser.addItems(config.get('BROWSERS', 'BROWSERS').split('|'))

        try:
            os.environ['WEBDRIVER_PATH']
        except KeyError:
            self.btn_run.setEnabled(False)
        self.btn_run.clicked.connect(self.execute_test)
        self.btn_webdriver.clicked.connect(self.define_webdriver_path)

    def execute_test(self):
        automation_thread = TestExecutionThread('Automation-Thread', self)
        automation_thread.start()

    def define_webdriver_path(self):
        os.environ['WEBDRIVER_PATH'] = QtGui.QFileDialog.getExistingDirectory()
        self.btn_run.setEnabled(True)


class TestExecutionThread(threading.Thread):
    def __init__(self, name, parent):
        threading.Thread.__init__(self)
        self.name = name
        self.parent = parent
        sys.stdout = EmittingStream(text_written=self.normalOutputWritten)
        steps.base_module.stream = sys.stdout

    def normalOutputWritten(self, text):
        cursor = self.parent.tb_output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.parent.tb_output.setTextCursor(cursor)
        self.parent.tb_output.ensureCursorVisible()

    def run(self):
        print("Starting " + self.name)
        index = self.parent.tv_folder_view.selectionModel().currentIndex()
        model = self.parent.tv_folder_view.model()
        test_path = model.filePath(index)
        os.environ['PATH'] = os.environ['WEBDRIVER_PATH'] + ':' + os.environ['PATH']
        os.environ['AUTOMATION_URL'] = self.parent.cb_environment.currentText()
        os.environ['AUTOMATION_BROWSER'] = self.parent.cb_browser.currentText()
        nose.run(defaultTest=test_path)
        print("Exiting " + self.name)


class EmittingStream(QtCore.QObject):
    text_written = QtCore.pyqtSignal(str)

    def write(self, text):
        self.text_written.emit(str(text))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = AutomationGUI(None)
    myWindow.show()
    sys.exit(app.exec_())
