myhosts is a hosts manager tool writed by python3.
myhosts can updata hosts from remote & local.
myhosts can be used to switch hosts between diffrent scene.
## license 
project is under [LGPL-3.0](./LICENSE)
## usage
### install
from pip
```shell
pip install myhosts
```
from source code
```shell
python setup.py install
```
### upgrade
1. backup configure.py
2. upgrade myhosts
```shell
pip upgrade myhosts
```
3. recover configure.py with backup
### uninstall
```shell
pip uninstall myhosts
```
### usage
```shell
# use under su,if need to update system hosts
myhosts action
myhosts argv
```
```shell
usage: myhosts [-h] [-v] [-i] [action]

positional arguments:
  action         action to run,default to run if no set

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  print myhosts version
  -i, --info     show myhosts refence info
```
### configure
1. find configure.py path
```shell
myhosts -i
```
2. modify configure
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

from .action import ActionBase
class Actions(ActionBase):
    '''define action to run'''
    def default(self):
        '''default action, must exist'''
        # self.backup()
        self.update(
            ('remote_hosts', 'ipv4 hosts'),
            ('local_hosts', 'github hosts')
        )

```
## android
use qpython3
## roadmap
- linux/qpython test
- pip
- auto test,build
- info of hosts(update time)
- upgrade