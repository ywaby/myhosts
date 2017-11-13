from os import path, system
from pytk import BaseNode
from shutil import copyfile, move

class purge(BaseNode):
    """
    test myhosts auto
    """

    def action(self):
        system('sudo pip3 uninstall myhosts')
        pass

class test(BaseNode):
    """
    test myhosts auto
    """

    def action(self):
        system('python3 -m myhosts -h')
        system('python3 -m myhosts -v')
        system('python3 -m myhosts -i')
        system('python3 -m myhosts -l')
        system('sudo python3 -m myhosts Test')

class Uninstall(BaseNode):

    def action(self):
        system('pip uninstall myhosts')
