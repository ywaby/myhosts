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
        'ipv4_hosts': 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts',
        'ipv6_hosts': 'https://github.com/lennylxx/ipv6-hosts'
    }
    # set local hosts path
    local_hosts = {
        # 'hosts name': path
    }
    # default path to backup,save to current path if not set
    backup_path = ''

from .action import ActionBase
class Actions(ActionBase):
    '''define action to run'''
    def default(self):
        '''default action, must exist'''
        self.backup()
        self.update(
            ('remote_hosts', 'ipv4_hosts')
        )
