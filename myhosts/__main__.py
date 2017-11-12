import platform
import os
import sys
import argparse
from inspect import getmembers

# conf_path = "/home/ywaby/文档/project/python/myhosts/myhosts/configure"
conf_path = "/usr/local/configs/myhosts"
sys.path.append(conf_path)
import actions
from .base_action import BaseAction


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
            print(f'hosts path: {BaseAction.hosts_path}')
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
