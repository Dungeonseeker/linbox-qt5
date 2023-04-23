# Imports
import os

from handlers import cfghndlr

# Constants
AppSettings = '-S'
AppConfig = '-C'
AppRootPath = '-P'


# Create VM
def create_vm(vmname, run_method):
    # Run Virtual Machine
    command = '{0} {1} {2}{3}{4}{5} {6}'.format(run_method, AppConfig, cfghndlr.Path, '/', vmname, '.cfg',
                                                AppSettings)
    print('Create VM:\n\nIssuing... ' + command.upper() + ' ...to the operating system')
    os.system(command)


# Run Vm
def run_vm(vmname, run_method):
    # Read config file
    cfghndlr.config_read(vmname)

    # Run Virtual Machine
    command = '{0} {1} {2}'.format(run_method, AppConfig, cfghndlr.config_read(vmname))
    print('Run VM:\n\nIssuing...' + command.upper() + ' ...to the operating system')
    os.system(command)


# Run Settings
def run_settings(vmname, run_method):
    # Read config file
    cfghndlr.config_read(vmname)

    # Run Virtual Machine
    command = '{0} {1} {2} {3}'.format(run_method, AppConfig, cfghndlr.config_read(vmname), AppSettings)
    print('Run Settings\n\nIssuing...' + command.upper() + ' ...to the operating system')
    os.system(command)
