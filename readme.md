myhosts is a hosts manager tool , a python tool.
myhosts, 
## license 
project is under [LGPL-v3](./LICENSE)
## usage
### install
from pip
```
pip install myhosts
```
from source code
```
python setup.py install
```
### upgrade
1. backup configure.py
2. upgrade myhosts
```
pip upgrade myhosts
```
### uninstall
```
pip uninstall myhosts
```
### usage
```
python -m myhosts [argv]
```
```
usage: myhosts [-h] [-v] [-i] [action]

positional arguments:
  action         action to run,default to run if no set

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  print myhosts version
  -i, --info     show myhosts refence info
```
### configure
find configure.py path
```
python -m myhosts -i
```
```
class Configure():
    '''configure of myhost'''
    proxy = {
        "http": "127.0.0.1:8087",
        "https": "127.0.0.1:8087"
    }
    remote_hosts = {
        'ipv6_hosts': 'https://github.com/lennylxx/ipv6-hosts',
        'ipv4_hosts': 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    }
    local_hosts = {
        'hostsin': r'E:\develop_space\myhost\test\hostsin'# hosts path
    }
    #default path to backup,save to current path if not set
    backup_path = r'E:\develop_space\myhost\test'

class Actions(ActionBase):
    def default(self):
        '''default action, must exist'''
        self.backup()
        self.update(
            ('remote_hosts', 'ipv4_hosts')
        )

    def test(self):
        '''test action'''
        self.backup()
        self.update(
            ('remote_hosts', 'ipv4_hosts'),
            ('local_hosts', 'hostsin')
        )
```

## roadmap
- linux test
- pip
- doc
- setup.py
- auto test,build
- ...
- UI