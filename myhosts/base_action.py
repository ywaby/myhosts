'''docstring
'''
import os
from urllib import request as urlrequest
from configure import Configure

if os.name == 'nt':
    HOSTS_PATH = os.path.join(os.getenv("SystemRoot"),
                              r"System32\drivers\etc\hosts")
elif os.name == "posix":
    HOSTS_PATH = '/etc/hosts'
else:
    raise Exception('unsupport system')


class BaseAction():
    '''action base class'''

    def __init__(self):
        self.action()

    def action(self):
        pass

    @staticmethod
    def _get_local_hosts(path):
        hosts_file = open(path, mode='rb')
        data = hosts_file.read()
        hosts_file.close()
        return data

    @staticmethod
    def _get_remote_hosts(link):
        req = urlrequest.Request(link)
        if hasattr(Configure, 'proxy'):
            if link.startswith('https://') and Configure.proxy.get('https'):
                req.set_proxy(Configure.proxy['https'], 'https')
                req.set_proxy(Configure.proxy['https'], 'https')
            elif link.startswith('http://')and Configure.proxy.get('https'):
                req.set_proxy(Configure.proxy['http'], 'http')
                req.set_proxy(Configure.proxy['http'], 'http')
        if not hasattr(Configure, 'timeout'):
            Configure.timeout = 30
        response = urlrequest.urlopen(req, timeout=Configure.timeout)
        data = response.read()
        return data

    def update(self, *sources):
        '''update system hosts from sources'''
        data = b''
        for hosts_type, src in sources:
            if hosts_type == 'local_hosts':
                src_path = Configure.local_hosts.get(src)
                if not src_path:
                    raise Exception('action (%s,%s) can not found' %
                                    (hosts_type, src))
                if not os.path.isfile(src_path):
                    raise Exception('file(%s) can not found' % (src_path))
                data += ('# %s->%s START\n' %
                         (hosts_type, src)).encode('utf-8')
                data += self._get_local_hosts(src_path)
                data += ('\n# %s->%s END\n\n' %
                         (hosts_type, src)).encode('utf-8')
            elif hosts_type == 'remote_hosts':
                src_link = Configure.remote_hosts.get(src)
                if not src_link:
                    raise Exception('action (%s,%s) can not found' %
                                    (hosts_type, src))
                print('%s:%s downloading...' % (hosts_type, src))
                data += ('# %s->%s START\n' %
                         (hosts_type, src)).encode('utf-8')
                data += self._get_remote_hosts(src_link)
                data += ('\n# %s->%s END\n\n' %
                         (hosts_type, src)).encode('utf-8')
            else:
                raise Exception('action source hosts type error')
        sys_hosts = open(HOSTS_PATH, mode='wb+')
        sys_hosts.write(data)
        sys_hosts.close()
        if os.name == 'nt':
            os.system('ipconfig /flushdns')
        print('finish hosts update')

    @staticmethod
    def clear():
        sys_hosts = open(HOSTS_PATH, mode='w')
        sys_hosts.close()
        print("finish clear hosts")
        return

    @staticmethod
    def backup(path=None, name=None):
        '''backup system hosts to path'''
        import shutil
        import time
        if not path:
            path = Configure.backup_path if hasattr(
                Configure, 'backup_path') else ''
        if not name:
            name = "hosts" + \
                time.strftime(" %Y-%m-%d %H-%M-%S", time.localtime())
        backup_path = os.path.join(path, name)
        shutil.copyfile(HOSTS_PATH, backup_path)
        print('hosts backup: ' + backup_path)

    @staticmethod
    def is_action(obj):
        '''determine object is Action'''
        import inspect
        try:
            if inspect.isclass(obj) and \
               BaseAction in inspect.getmro(obj) and \
               obj != BaseAction:
                return True
            return False
        except:
            return False
