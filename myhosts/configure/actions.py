'''doc'''
from myhosts.base_action import BaseAction


class Default(BaseAction):
    '''
    default action, must exist
    '''

    def action(self):
        self.update(
            ('remote_hosts', 'ipv4 hosts')
        )


class Clear(BaseAction):
    '''
    default action, must exist
    '''

    def action(self):
        BaseAction.clear()


class Test(BaseAction):
    '''
    backup->hosts=(remote ipv4 hosts+local add hosts)
    '''

    def action(self):
        BaseAction.backup("/home/ywaby/文档/project/python/myhosts/test/backup")
        self.update(
            ('remote_hosts', 'ipv4 hosts'),
            ('local_hosts', 'github hosts')
        )
