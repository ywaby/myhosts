'''docstring'''
import os
import shutil
import sys
import argparse
from inspect import getmembers

CONF_PATH = os.path.expanduser("~/.config/myhosts")
if not os.path.exists(CONF_PATH):
    os.mkdir(CONF_PATH)
if not os.path.exists(f"{CONF_PATH}/configure.py"):
    shutil.copyfile(os.path.join(os.path.dirname(__file__), "configure/configure.py"),
                    f"{CONF_PATH}/configure.py")
if not os.path.exists(f"{CONF_PATH}/actions.py"):
    shutil.copyfile(os.path.join(os.path.dirname(__file__), "configure/actions.py"),
                    f"{CONF_PATH}/actions.py")
sys.path.append(CONF_PATH)


import actions
from .base_action import HOSTS_PATH, BaseAction


def list_actions():
    '''list all tasks in files'''
    for name, action in getmembers(actions, BaseAction.is_action):
        print(name, ":", action.__doc__)
        print()


def cmd_prase():
    """Run the myhosts command line"""
    parser = argparse.ArgumentParser(prog='myhosts',
                                     description='a hosts manager tool',
                                     epilog="project at: www.github.ywaby.myhosts.com")
    parser.add_argument('-v',
                        "--version",
                        help="print myhosts version",
                        action='version',
                        version='%(prog)s 0.2.1')
    parser.add_argument('-i',
                        "--info",
                        help="show myhosts refence info",
                        action='store_true')
    parser.add_argument('-l', "--list",
                        help="list all actions",
                        action='store_true')
    parser.add_argument('action',
                        nargs='?',
                        default='Default',
                        help="action to run,Default to run if no set")
    args = parser.parse_args()
    if args.info:
        print(f'configure path: {CONF_PATH}')
        print(f'hosts path: {HOSTS_PATH}')
    elif args.list:
        print("actions in myhosts")
        print()
        list_actions()
    else:
        action = getattr(actions, args.action)
        action()


def main():
    cmd_prase()
    return True


if __name__ == '__main__':
    main()
