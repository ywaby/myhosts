from shutil import rmtree, copytree
from os import path
from invoke import task
import os

conf_path = path.expanduser("~/.config/myhosts")


@task
def test_all(ctx):
    """
    test myhosts auto
    """
    ctx.run('python3 -m myhosts -h')
    ctx.run('python3 -m myhosts -v')
    ctx.run('python3 -m myhosts -i')
    ctx.run('python3 -m myhosts -l')
    ctx.run('sudo python3 -m myhosts Test')


@task
def clear_conf(ctx):
    '''clear configure files'''
    if path.exists(conf_path):
        rmtree(conf_path)


@task(clear_conf)
def install_conf(ctx):
    copytree("./config/myhosts", conf_path)
