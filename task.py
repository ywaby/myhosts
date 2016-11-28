import os
def update():
    uninstall()
    install()
def install():
    os.system('python setup.py install')
def uninstall():
    os.system('pip uninstall myhosts')
def test():