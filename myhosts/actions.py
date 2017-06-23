
from .base_action import BaseAction


class Default(BaseAction):
    '''
    default action, must exist
    '''

    def action(self):
        self.update(
            ('remote_hosts', 'ipv4 hosts')
        )


class Test(BaseAction):
    '''
    backup->hosts=(remote ipv4 hosts+local add hosts)
    '''

    def action(self):
        self.backup("E:/develop_space/python/myhosts/test/backup")
        self.update(
            ('remote_hosts', 'ipv4 hosts'),
            ('local_hosts', 'github hosts')
        )
