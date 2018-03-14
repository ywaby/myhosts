from os import path, system
from shutil import rmtree
from pytk import BaseNode

class test_all(BaseNode):
    """
    test myhosts auto
    """

    def action(self):
        system('python3 -m myhosts -h')
        system('python3 -m myhosts -v')
        system('python3 -m myhosts -i')
        system('python3 -m myhosts -l')
        system('sudo python3 -m myhosts Test')


class link_conf(BaseNode):

    def action(self):
        project_path = os.path.dirname(__file__)
        src = os.path.join(project_path, "./myhosts/configure")
        link = os.path.abspath(src)
        target = "~/.config/myhosts")
        if os.path.exists(target):
            os.rmdir(target)
        os.symlink(link, target)

class clear_conf(BaseNode):
    '''clear configure files'''

    def action(self):
        conf_path = path.expanduser("~/.config/myhosts")
        if path.exists(conf_path):
            rmtree(conf_path)
