# Imports
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QMessageBox
from showinfm import show_in_file_manager
from xdgenvpy import XDG

from handlers import cfghndlr, vmhndlr
from utils import system as sys_tool

# Modules
from ui.ui_createwindow import Ui_CreateWindow
from ui.ui_mainwindow import Ui_MainWindow

xdg = XDG()

# Global objects
listbox = None
run_btn = None
settings_btn = None
delete_btn = None
name_entry = None
package = None
fp_system = None
fp_user = None
fp_appimg = None
run_method = None

# Application path constants
VmCfg: str = '/Linbox.ini'
AppHome: str = 'Linbox'
XDGHome: str = xdg.XDG_CONFIG_HOME
# Join 2 constants to create our path
Path: str = os.path.join(XDGHome, AppHome)


# Main window class
class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        # Test to check if linbox folder does not exist yet
        if not os.path.exists(Path):
            try:
                # Create new folder
                os.mkdir(Path)
                os.rmdir(Path)
            except OSError as error:
                self.warning = QMessageBox()
                self.warning.setIcon(QMessageBox.Warning)
                self.warning.setWindowTitle('An error occurred.?')
                self.warning.setFixedSize(300, 200)
                self.warning.setText('Unable to create config folder:\n\n'
                                     + error.__str__() + '\n\n'
                                                         'Press OK to Quit..')
                self.warning.setStandardButtons(QMessageBox.Ok)
                self.warning.setDefaultButton(QMessageBox.Ok)
                self.warning.buttonClicked.connect(quit)
                self.warning.exec()

        # Next test if linbox folder exists already
        if not os.path.exists(Path):
            self.frw()

        super().__init__(parent)

        # Define UI
        self.ui = Ui_MainWindow()
        self.ui.setupui(self)

        # Actions
        self.ui.action_Run.triggered.connect(self.run_vm)
        self.ui.action_Settings.triggered.connect(self.run_settings)
        self.ui.action_Create.triggered.connect(self.create_window)
        self.ui.action_Quit.triggered.connect(self.quit_app)
        self.ui.action_About_Linbox.triggered.connect(self.about)

        # Make objects global for later
        global listbox, settings_btn, run_btn, delete_btn, combobox
        listbox = self.ui.listWidget
        run_btn = self.ui.run_btn
        settings_btn = self.ui.settings_btn
        delete_btn = self.ui.delete_btn
        combobox = self.ui.select_cmb

        # Populate combobox and set 86Box paths
        global package, fp_system, fp_user, fp_appimg
        if os.path.exists('/usr/bin/86Box'):
            self.ui.select_cmb.addItem('Package')
            package = '/usr/bin/86Box'
        if os.path.exists('/var/lib/flatpak/exports/bin/net._86box._86Box'):
            self.ui.select_cmb.addItem('Flatpak (System)')
            fp_system = '/var/lib/flatpak/exports/bin/net._86box._86Box'
        if os.path.exists(xdg.XDG_DATA_HOME + '/flatpak/exports/bin/net._86box._86Box'):
            self.ui.select_cmb.addItem('Flatpak (User)')
            fp_user = xdg.XDG_DATA_HOME + '/flatpak/exports/bin/net._86box._86Box'
        app_img_path = sys_tool.find_portable_path()
        if app_img_path is not None and os.path.exists(app_img_path):
            self.ui.select_cmb.addItem('AppImage')
            fp_appimg = app_img_path

        # Define other windows
        self.create = None

        # Run config handler to test if linbox.ini exists
        cfghndlr.config_create()

        # Populate list widget with existing VMs if they exist then enable UI
        self.data: list = cfghndlr.config_list()
        print(self.data)
        if self.data == '[]':
            pass
        else:
            for entries in self.data:
                self.ui.listWidget.addItems([entries])
                self.count: int = self.ui.listWidget.count()
                if self.count != 0:
                    self.ui.listWidget.setEnabled(True)
                    self.ui.listWidget.setCurrentRow(0)
                    self.ui.run_btn.setEnabled(True)
                    self.ui.settings_btn.setEnabled(True)
                    self.ui.delete_btn.setEnabled(True)

        # Connect button callbacks
        self.ui.create_btn.clicked.connect(self.create_window)
        self.ui.run_btn.clicked.connect(self.run_vm)
        self.ui.settings_btn.clicked.connect(self.run_settings)
        self.ui.quit_btn.clicked.connect(self.quit_app)
        self.ui.delete_btn.clicked.connect(self.delete)
        self.ui.open_btn.clicked.connect(self.open)

    def frw(self):
        frw = QMessageBox()
        frw.setIcon(QMessageBox.Information)
        frw.setWindowTitle('First run wizard...')
        frw.setFixedSize(300, 200)
        frw.setText('This is the first time you have run Linbox,\n'
                    'a config file will be created at:')
        frw.setInformativeText(Path)
        frw.setStandardButtons(QMessageBox.Ok)
        frw.setDefaultButton(QMessageBox.Ok)
        frw.buttonClicked.connect(frw.close)
        frw.exec()

    # Create button
    def create_window(self):
        if self.create is None:
            self.create = CreateWindow()
        self.create.show()
        # Make sure name entry has focus
        name_entry.setFocus()

    # Quit button
    @staticmethod
    def quit_app():
        quit()

    # Run button
    def run_vm(self):
        global run_method
        self.count = self.ui.select_cmb.currentIndex()
        self.value = self.ui.select_cmb.itemText(self.count)
        if self.value == 'Package':
            run_method = package
        elif self.value == 'Flatpak (System)':
            run_method = fp_system
        elif self.value == 'Flatpak (User)':
            run_method = fp_user
        elif self.value == 'AppImage':
            run_method = fp_appimg
        if self.ui.listWidget.isEnabled():
            self.vmname: str = self.ui.listWidget.currentItem().text()
            vmhndlr.run_vm(self.vmname, run_method)
        else:
            pass

    # Settings button
    def run_settings(self):
        global run_method
        self.count = self.ui.select_cmb.currentIndex()
        self.value = self.ui.select_cmb.itemText(self.count)
        if self.value == 'Package':
            run_method = package
        elif self.value == 'Flatpak (System)':
            run_method = fp_system
        elif self.value == 'Flatpak (User)':
            run_method = fp_user
        elif self.value == 'AppImage':
            run_method = fp_appimg
        if self.ui.listWidget.isEnabled():
            self.vmname: str = self.ui.listWidget.currentItem().text()
            vmhndlr.run_settings(self.vmname, run_method)
        else:
            pass

    # Delete button
    def delete(self):
        # Warning about file removal
        warning = QMessageBox(self)
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle('Delete File?')
        warning.setFixedSize(300, 200)
        warning.setText('This will remove the VM from Linbox and delete its config file,\n'
                        'your HDD images and other files WILL NOT be removed.')
        warning.setInformativeText('ARE YOU ABSOLUTELY SURE?')
        warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        warning.setDefaultButton(QMessageBox.No)

        # Only delete if user clicks OK
        ret = warning.exec()

        if ret == QMessageBox.Yes:
            self.ok()
        elif ret == QMessageBox.No:
            pass

    # Delete dialog OK button
    def ok(self):
        self.vmname: str = self.ui.listWidget.currentItem().text()
        cfghndlr.delete(self.vmname)
        self.row: int = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(self.row)
        self.count: int = self.ui.listWidget.count()
        if self.count == 0:
            self.ui.listWidget.setEnabled(False)
            self.ui.run_btn.setEnabled(False)
            self.ui.settings_btn.setEnabled(False)
            self.ui.delete_btn.setEnabled(False)

    # Open linbox folder button
    @staticmethod
    def open():
        show_in_file_manager(Path)

    def about(self):
        # About window
        about = QMessageBox()
        about.setIcon(QMessageBox.Information)
        about.setWindowTitle('About Linbox')
        about.setFixedSize(350, 200)
        about.setText('Linbox for 86Box:')
        about.setInformativeText('(C)2023 Dungeonseeker\n\n'
                                 'Linbox is licensed under the MIT license,\n'
                                 'you are free to modify and distribute it.')
        about.setStandardButtons(QMessageBox.Ok)
        about.setDefaultButton(QMessageBox.Ok)
        about.buttonClicked.connect(about.close)
        about.exec()


# Create new vm window class
class CreateWindow(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateWindow()
        self.ui.setupui(self)
        self.ui.ok_btn.clicked.connect(self.ok)
        self.ui.cancel_btn.clicked.connect(self.cancel)

        global name_entry
        name_entry = self.ui.name_entry

    # Create window ok button
    def ok(self):
        self.vmname: str = self.ui.name_entry.text()
        if self.vmname == "":
            pass
        else:
            self.vms: list = cfghndlr.config_list()

            # Input handler, change illegal chars to -
            self.vmname = self.vmname.translate(str.maketrans({' ': '-', '/': '-', '\"': '-'}))
            print(self.vmname)

            # Check if vmname already exists
            if self.vmname in self.vms:
                self.warning = QMessageBox()
                self.warning.setIcon(QMessageBox.Warning)
                self.warning.setWindowTitle('Name already exists')
                self.warning.setFixedSize(300, 200)
                self.warning.setText('A VM with that name already exists,\n'
                                     'please recreate with a different name.')
                self.warning.setStandardButtons(QMessageBox.Ok)
                self.warning.setDefaultButton(QMessageBox.Ok)
                self.warning.buttonClicked.connect(self.bailout)
                self.warning.exec()
            else:
                # Set launch method based on combobox selection
                global run_method, package, fp_system, fp_user, fp_appimg
                count = combobox.currentIndex()
                self.value = combobox.itemText(count)
                if self.value == 'Package':
                    self.run_method = package
                elif self.value == 'Flatpak (System)':
                    self.run_method = fp_system
                elif self.value == 'Flatpak (User)':
                    self.run_method = fp_user
                elif self.value == 'AppImage':
                    self.run_method = fp_appimg
                vmhndlr.create_vm(self.vmname, self.run_method)
                self.check(self.vmname)
                self.close()
        return

    # Check existing name function bailout method
    def bailout(self):
        self.ui.name_entry.setText('')
        self.close()

    # Create window cancel button
    def cancel(self):
        # Reset entry box
        self.ui.name_entry.setText('')
        self.close()

    # Check if user closed 86Box without saving
    def check(self, vmname):
        # Reset entry box
        self.ui.name_entry.setText('')

        # Check if config file exists
        command: str = '{0}{1}{2}{3}'.format(Path, '/', vmname, '.cfg')
        if not os.path.exists(command):
            self.close()
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Information)
            self.warning.setWindowTitle('Nothing Saved')
            self.warning.setFixedSize(300, 200)
            self.warning.setText('It looks like you closed 86Box without saving,\n'
                                 'no changes were made.')
            self.warning.setStandardButtons(QMessageBox.Ok)
            self.warning.setDefaultButton(QMessageBox.Ok)
            self.warning.buttonClicked.connect(self.warning.close)
            self.warning.exec()
            print("86Bow window cancelled, nothing saved")
        else:
            cfghndlr.config_write(vmname)
            self.close()

            # Use global objects from earlier
            global listbox, run_btn, settings_btn, delete_btn

            # Add new vm to list
            listbox.addItem(vmname)

            # Enable UI if first VM created
            self.count: int = listbox.count()
            if self.count != 0:
                listbox.setEnabled(True)
                listbox.setCurrentRow(0)
                run_btn.setEnabled(True)
                settings_btn.setEnabled(True)
                delete_btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    linbox = MainWindow()
    linbox.show()
    app.exec()
