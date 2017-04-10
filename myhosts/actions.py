
from .base_action import BaseAction


class Default(BaseAction):
    '''default action, must exist'''

    def execute(self):
        self.update(
            ('remote_hosts', 'ipv4 hosts')
        )



class Test(BaseAction):
    '''backup->hosts=(remote ipv4 hosts+local github hosts)'''

    def execute(self):
        self.backup(r"E:\develop_space\python\myhosts\test\backup")
        self.update(
            ('remote_hosts', 'ipv4 hosts'),
            ('local_hosts', 'github hosts')
        )
