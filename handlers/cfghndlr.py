# Imports
import configparser
import os

from PySide6.QtWidgets import QMessageBox
from xdgenvpy import XDG

xdg = XDG()

# Constants
VmCfg: str = '/Linbox.ini'
AppHome: str = 'Linbox'
XDGHome: str = xdg.XDG_CONFIG_HOME.__str__()

# Join 2 constants to create our paths
Path: str = os.path.join(XDGHome, AppHome)
Ini: str = Path + VmCfg


# Create Linbox.ini
def config_create():
    # Test if path exists and ...
    if os.path.exists(Path):
        # if yes do nothing or ...
        pass
    else:
        try:
            # ... if no try to create it
            os.mkdir(Path)

            # Load config parser
            config = configparser.ConfigParser()

            # Default section for settings at a later time
            config['DEFAULT'] = {'Linbox_Location': Ini}

            # Open Linbox config (Y variable) and write everything to it
            with open(Ini, 'w') as configfile:
                config.write(configfile)

            print('Config Create:\n\nLinbox config file... ' + Ini.upper() + ' ...created successfully.')

        # Finally fire an error and quit if creation of config file fails
        except OSError as error:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle('An Error Occurred')
            warning.setFixedSize(300, 200)
            warning.setText('Unable to create Linbox config:')
            warning.setInformativeText(str(error))
            warning.setStandardButtons(QMessageBox.Quit)
            warning.setDefaultButton(QMessageBox.Quit)
            warning.buttonClicked.connect(warning.close)
            warning.exec()
            print('An error ' + str(error) + 'occurred, bailing out.')
            quit()


# Write a new VM to Linbox.ini
def config_write(vmname):
    # Load config parser
    config = configparser.ConfigParser()

    # Generate the path of the new VM CFG
    location: str = '{0}{1}{2}{3}{4}{5}'.format(XDGHome, '/', AppHome, '/', vmname, '.cfg')

    # Create new config section with our VM Name variable
    config[vmname] = {}

    # Save path into a subsection called location
    config[vmname]["location"] = location

    # Open Linbox config and write everything to it
    with open(Ini, 'a') as configfile:
        config.write(configfile)

    print('Config Write:\n\nSection... ' + vmname.upper() + ' ...successfully appended to... ' + Ini.upper())

    # Return
    return


# Parse Linbox.ini, return 86Box cfg location
def config_read(vmname):
    # Load config parser
    config = configparser.ConfigParser()

    # Read Linbox config.ini
    config.read(Ini)

    # Read Location from Linbox.ini, return result
    location: str = config[vmname]['location']

    # Return result
    return location


# Parse Linbox.ini and return all items as a list
def config_list():
    # Load config parser
    config = configparser.ConfigParser()

    # Read Linbox.ini
    config.read(Ini)

    # Get list of sections from config and add them to variable
    value: list = config.sections()

    # Return result
    return value


# Delete a VM from Linbox.ini and remove its associated 86Box cfg
def delete(vmname):
    # Load config parser
    config = configparser.SafeConfigParser()

    # Generate the path of the VM CFG
    X: str = '{0}{1}{2}{3}{4}{5}'.format(XDGHome, '/', AppHome, '/', vmname, '.cfg')

    # Delete file
    try:
        os.remove(X)
    except OSError as error:
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle('An Error Occurred')
        warning.setFixedSize(300, 200)
        warning.setText('Unable to delete 86Box config:')
        warning.setInformativeText(str(error))
        warning.setStandardButtons(QMessageBox.Cancel)
        warning.setDefaultButton(QMessageBox.Cancel)
        warning.buttonClicked.connect(bailout)
        warning.exec()
        print('An error ' + str(error) + 'occurred, bailing out.')

    # Read Linbox.ini
    with open(Ini, 'r+') as configfile:
        config.read_file(configfile)

        # Remove section
        config.remove_section(vmname)
        configfile.seek(0)

        # Write changes
        config.write(configfile)
        print('Config Delete:\n\nSection... ' + vmname.upper() + ' ...successfully removed from... ' + Ini.upper())
        configfile.truncate()


# Delete function bailout method
def bailout():
    return
