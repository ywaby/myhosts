myhosts is a hosts manager tool base on python3.  
myhosts can updata hosts from remote & local.  
myhosts can be used to switch hosts between diffrent scene.

## License 
project is under [LGPL-3.0](./LICENSE)

## Usage

### Install
from source code
```shell
python setup.py install
```

### Upgrade
task.py -> UpgrageFromSetup

### Uninstall
```shell
pip uninstall myhosts
```

### Command Reference
please used under sudo, if need to change system hosts.

```sh
usage: myhosts [-h] [-v] [-i] [-l] [action]

positional arguments:
  action         action to run,default to run if no set

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  print myhosts version
  -i, --info     show myhosts refence info
  -l, --list     list all actions
```

### Configure
find path
```shell
myhosts -i
```

configure.py 
```py

class Configure():
    '''configure of myhost'''
    # remote download timeout set
    timeout = 30
    # set proxy,if not use proxy,do not set it
    proxy = {
        # "http": "127.0.0.1:8087",
        # "https": "127.0.0.1:8087"
    }
    # set remote hosts link
    remote_hosts = {
        # 'hosts name': link
        'ipv4 hosts': 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts',
        'ipv6 hosts': 'https://github.com/lennylxx/ipv6-hosts'
    }
    # set local hosts path
    local_hosts = {
        # 'hosts name': path
        'github hosts': r'E:\develop_space\python\myhosts\test\github_hosts'
    }
    # default path to backup,save to current path if not set
    backup_path = ''

```

### Action
actions.py
```py
class ActionName(BaseAction):
    '''doc of action'''

    def execute(self):
        # backup hosts
        self.backup(r"E:\develop_space\python\myhosts\test")
        # update hosts from list
        self.update(
            ('remote_hosts', 'ipv4 hosts'),
            ('local_hosts', 'github hosts')
        )
```

## Roadmap
- conf at home
- android test
- pip package