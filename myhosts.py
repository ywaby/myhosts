import json
import os
import argparse
from urllib import request as urlrequest
import time

config={}
with open(os.path.expanduser('~/.config/myhosts.config.json'), 'r') as fp:
    config = json.load(fp)

HOSTS_PATH=""
if os.name == 'nt':
    HOSTS_PATH = os.path.join(os.getenv("SystemRoot"),r"System32\drivers\etc\hosts")
elif os.name == "posix":
    HOSTS_PATH = '/etc/hosts'
else:
    raise Exception('unsupport system')

def _get_hosts(url):
    if '://' not in url:
        url = "file://"+(os.path.abspath(url))
    req = urlrequest.Request(url)
    response = urlrequest.urlopen(req, timeout=config["timeout"])
    data = response.read()
    return data

def clear():
    sys_hosts = open(HOSTS_PATH, mode='w')
    sys_hosts.close()
    print("finish clear hosts")
    return

def backup(path=None, name=None):
    '''backup system hosts to path'''
    import shutil
    if not path:
        path = config["backup_path"]
    if not name:
        name = "hosts" + \
            time.strftime(" %Y-%m-%d %H-%M-%S", time.localtime())
    backup_path = os.path.join(path, name)
    shutil.copyfile(HOSTS_PATH, backup_path)
    print('hosts backup: ' + backup_path)

def update(srcs):
    '''update hosts from sources'''
    data = b''
    tim = time.strftime(" %Y-%m-%d %H-%M-%S", time.localtime())
    data += (f'# update time:{tim}\n\n').encode('utf-8')
    
    for src in srcs:
        url = config['hosts'][src]
        print(f'getting {src}:{url}')
        data += (f'# START: {src}\n').encode('utf-8')
        data += _get_hosts(url)
        data += (f'\n# END: {src}\n\n').encode('utf-8')
    sys_hosts = open(HOSTS_PATH, mode='wb+')
    sys_hosts.write(data)
    sys_hosts.close()
    if os.name == 'nt':
        os.system('ipconfig /flushdns')
    print('finish hosts update')

def exec_action(action_name):
    if action_name not in config["actions"]:
        print(f'action {action_name} not exist')
        return
    action = config["actions"][action_name]
    if action['backup']:
        backup()
    if action['update']:
        update(action['update'])
    if action['clear']:
        clear()

def list_actions(actions):
    '''list all actions in files'''
    for key,action in actions.items():
        print(key, ":",action['note'])
    print()



def cli_prase():
    """Run the myhosts command line"""
    parser = argparse.ArgumentParser(prog='myhosts',
                                     description=f'''a hosts manager tool.
                                                config at "~/.config/myhosts",
                                                system hosts at "{HOSTS_PATH}"''',
                                     epilog="project maintance at: www.github.com/ywaby/myhosts")
    parser.add_argument('-v',
                        "--version",
                        help="print myhosts version",
                        action='version',
                        version='%(prog)s 0.3.0')
    parser.add_argument('-l', "--list",
                        help="list all actions",
                        action='store_true')
    parser.add_argument('action',
                        nargs='?',
                        default='default',
                        help="action to run,default action if unset")
    args = parser.parse_args()
    if args.list:
        print("actions in myhosts")
        print()
        list_actions(config['actions'])
    else:
        exec_action(args.action)

def main():
    cli_prase()
    return True


if __name__ == '__main__':
    main()
