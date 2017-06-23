import platform
import os
import argparse
from . import configure
from . import actions
from .base_action import BaseAction
from inspect import getmembers


class CommandLine():

    def prase(self):
        """Run the myhosts command line"""
        parser = argparse.ArgumentParser(prog='myhosts',
                                         description='a hosts manager tool',
                                         epilog="project at: www.github.ywaby.myhosts.com")
        parser.add_argument('-v',
                            "--version",
                            help="print myhosts version",
                            action='version',
                            version='%(prog)s 0.1.1')
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
            print('configure path: %s' % os.path.dirname(configure.__file__))
            if platform.system() == 'Windows':
                sys_root_path = os.getenv("SystemRoot")
                sys_hosts_path = os.path.join(
                    sys_root_path, r"System32\drivers\etc\hosts")
            elif platform.system() == 'Linux':
                sys_hosts_path = '/etc/hosts'
            else:
                sys_hosts_path = '/etc/hosts'
            print('hosts path: %s' % sys_hosts_path)
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
            print(name, " : ", action.__doc__)
            print()


def main():
    CommandLine().prase()
    return True

if __name__ == '__main__':
    main()
