class Configure():
    '''configure of myhost'''
    # proxy = {
    #     "http": "127.0.0.1:8087",
    #     "https": "127.0.0.1:8087"
    # }
    remote_hosts = {
        'ipv6_hosts': 'https://github.com/lennylxx/ipv6-hosts',
        'ipv4_hosts': 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    }
    local_hosts = {
        'hostsin': r'E:\develop_space\myhosts\test\hostsin'# hosts path
    }
    #default path to backup,save to current path if not set
    backup_path = r'E:\develop_space\myhosts\test'

from .action import ActionBase

class Actions(ActionBase):
    def default(self):
        '''default action, must exist'''
        self.backup()
        self.update(
            ('remote_hosts', 'ipv4_hosts')
        )

    def test(self):
        '''test action'''
        # self.backup()
        self.update(
            ('remote_hosts', 'ipv4_hosts'),
            ('local_hosts', 'hostsin')
        )
