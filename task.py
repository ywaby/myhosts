from os import path, system
from pytk import BaseNode
from shutil import copyfile, move


class Test(BaseNode):

    def action(self):
        system('python -m myhosts -h')
        system('python -m myhosts -v')
        system('python -m myhosts -i')
        system('python -m myhosts -l')
        system('python -m myhosts Test')


class Update(BaseNode):

    def action(self):
        system('python -m setup.py install')


class UpdateFromPip(BaseNode):

    def action(self):
        import myhosts
        cfg_src = myhosts.actions.__file__
        actions_src = myhosts.configure.__file__
        home = path.expanduser('~')
        cfg_bak = path.join(home, path.basename(cfg_src))
        actions_bak = path.join(home, path.basename(actions_src))
        copyfile(cfg_src, cfg_bak)
        copyfile(actions_src, actions_bak)
        system('pip install myhosts')
        move(actions_bak, actions_src)
        move(cfg_bak, cfg_src)


class UpdateFromSetup(BaseNode):

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
        system('python -m setup.py install')
        from myhosts import actions
        from myhosts import configure
        cfg_src = actions.__file__
        actions_src = configure.__file__
        move(actions_bak, actions_src)
        move(cfg_bak, cfg_src)


class Uninstall(BaseNode):

    def action(self):
        system('pip uninstall myhosts')
