myhosts is a hosts manager tool base on python3.  
myhosts can updata hosts from remote & local files.  
myhosts can be used to switch hosts between diffrent scene.

project is under [MIT](./LICENSE)


### Install
from source code
```shell
sudo python setup.py install
```

uninstall
```sh
pip uninstall myhosts
# remove configure file
rm  ~/.config/config.json
```



## Usage

### Command Reference
please used under sudo, if need to change system hosts.

```sh
usage: myhosts [-h] [-v] [-i] [-l] [action]

positional arguments:
  action         action to run,default action if unset

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  print myhosts version
  -l, --list     list all actions
```

### configure
~/.config/config.json
```json
{
    "actions": {
        "default": {
            "note": "default action",
            "update": [
                "ipv4 gfw",
                "local hosts"
            ],
            "backup": true,
            "clear": false
        },
        "test": {
            "note": "",
            "update": [
                "ipv4 gfw",
                "local hosts"
            ],
            "backup": true,
            "clear": false
        },
        "clear": {
            "note": "",
            "update": [],
            "backup": true,
            "clear": true
        }
    },
    "timeout": 30,
    "proxy": {
        "http": "127.0.0.1:8087",
        "https": "127.0.0.1:8087"
    },
    "hosts": {
        "ipv4 gfw": "https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts-files/hosts",
        "ipv6 gfw": "https://github.com/lennylxx/ipv6-hosts",
        "local hosts": "~/.config/myhosts/extra_hosts"
    },
    "backup_path": "~/.config/myhosts/backup"
}
```
