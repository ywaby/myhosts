import os
import shutil
import sys

conf_path = os.path.expanduser("~/.config/myhosts")
if not os.path.exists(conf_path):
    os.mkdir(conf_path)
if not os.path.exists(f"{conf_path}/configure.py"):
    src = os.path.join(os.path.dirname(__file__), "configure/configure.py")
    shutil.copyfile(src, f"{conf_path}/configure.py")
if not os.path.exists(f"{conf_path}/actions.py"):
    src = os.path.join(os.path.dirname(__file__), "configure/actions.py")
    shutil.copyfile(src, f"{conf_path}/actions.py")
sys.path.append(conf_path)

import platform
import os
import sys
import argparse
from inspect import getmembers
from .base_action import hosts_path,BaseAction
import actions

class CommandLine():
    def init(self):
        pass

    def prase(self):
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
            print(f'configure path: {conf_path}')
            print(f'hosts path: {hosts_path}')
        elif args.list:
            print("actions in myhosts")
            print()
            self.list_actions()
        else:
            action = getattr(actions, args.action)
            action()

    def list_actions(self):
        '''list all tasks in files'''
        for name, action in getmembers(actions, BaseAction.is_action):
            print(name, ":", action.__doc__)
            print()


def main():
    CommandLine().prase()
    return True


if __name__ == '__main__':
    main()
