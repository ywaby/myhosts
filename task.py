from os import path, system
from pytk import BaseNode
from shutil import copyfile, move


class test(BaseNode):
    """
    test myhosts auto
    """

    def action(self):
        system('python -m myhosts -h')
        system('python -m myhosts -v')
        system('python -m myhosts -i')
        system('python -m myhosts -l')
        system('python -m myhosts Test')

class UpdateFromPip(BaseNode):
    """
    upgrade myhosts from pip
    """

    def action(self):
        from myhosts import actions
        from myhosts import configure
        cfg_src = actions.__file__
        actions_src = configure.__file__
        home = path.expanduser('~')
        cfg_bak = path.join(home, path.basename(cfg_src))
        actions_bak = path.join(home, path.basename(actions_src))
        copyfile(cfg_src, cfg_bak)
        copyfile(actions_src, actions_bak)
        del actions
        del configure
        system('pip upgrade myhosts')
        from myhosts import actions
        from myhosts import configure
        cfg_src = actions.__file__
        actions_src = configure.__file__
        move(actions_bak, actions_src)
        move(cfg_bak, cfg_src)


class UpdateFromSetup(BaseNode):
    """
    upgrade myhosts from setuptool
    """

    def action(self):
        from myhosts import actions
        from myhosts import configure
        cfg_src = actions.__file__
        actions_src = configure.__file__
        home = path.expanduser('~')
        cfg_bak = path.join(home, path.basename(cfg_src))
        actions_bak = path.join(home, path.basename(actions_src))
        copyfile(cfg_src, cfg_bak)
        copyfile(actions_src, actions_bak)
        del actions
        del configure
        system('python setup.py install')
        from myhosts import actions
        from myhosts import configure
        cfg_src = actions.__file__
        actions_src = configure.__file__
        move(actions_bak, actions_src)
        move(cfg_bak, cfg_src)


class Uninstall(BaseNode):

    def action(self):
        system('pip uninstall myhosts')
