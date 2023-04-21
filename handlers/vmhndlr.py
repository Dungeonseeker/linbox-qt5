# Imports
import os

from handlers import cfghndlr

# Constants
AppName = '86Box'
AppSettings = '-S'
AppConfig = '-C'
AppRootPath = '-P'


# Create VM
def create_vm(vmname):
    # Run Virtual Machine
    command = '{0} {1} {2}{3}{4}{5} {6}'.format(AppName, AppConfig, cfghndlr.Path, '/', vmname, '.cfg',
                                                AppSettings)
    print('Create VM:\n\nIssuing... ' + command.upper() + ' ...to the operating system')
    os.system(command)


# Run Vm
def run_vm(vmname):
    # Read config file
    cfghndlr.config_read(vmname)

    # Run Virtual Machine
    command = '{0} {1} {2}'.format(AppName, AppConfig, cfghndlr.config_read(vmname))
    print('Run VM:\n\nIssuing...' + command.upper() + ' ...to the operating system')
    os.system(command)


# Run Settings
def run_settings(vmname):
    # Read config file
    cfghndlr.config_read(vmname)

    # Run Virtual Machine
    command = '{0} {1} {2} {3}'.format(AppName, AppConfig, cfghndlr.config_read(vmname), AppSettings)
    print('Run Settings\n\nIssuing...' + command.upper() + ' ...to the operating system')
    os.system(command)
