from os import path, system
from shutil import rmtree
from pytk import BaseNode

class TestAll(BaseNode):
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
    def checker(self):
        '''judge whele to run action'''
        Clear()
        return True

    def action(self):
        system('pip uninstall myhosts')


class Clear(BaseNode):
    '''clear configure files'''

    def action(self):
        conf_path = path.expanduser("~/.config/myhosts")
        if path.exists(conf_path):
            rmtree(conf_path)
