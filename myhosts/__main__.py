import sys
import platform
import os
from . import configure

def main():
    import argparse
    parser = argparse.ArgumentParser(prog='myhosts',
                                     description='update hosts from github',
                                     epilog="project at: www.github.ywaby.pytk.com")

    parser.add_argument('-v', "--version", help="print version",action='version', version='%(prog)s 0.0.1')
    parser.add_argument('-i', "--info", help="show info", action='store_true')
    parser.add_argument('action', nargs='?', default='default', help="action to run,default to run if no set")
    args = parser.parse_args()
    if args.info:
        print('configure path: %s'%configure.__file__)
        if platform.system() == 'Windows':
            sys_root_path = os.getenv("SystemRoot")
            sys_hosts_path = os.path.join(sys_root_path, "System32\drivers\etc\hosts")
        elif platform.system() == 'Linux':
            sys_hosts_path = '/etc/hosts'
        else:
            sys_hosts_path = '/etc/hosts'
        print('hosts path: %s'%sys_hosts_path)
    else :
        action = getattr(configure.Actions(),args.action)
        action()
        os.system('pause')

if __name__ == '__main__':
    main()
