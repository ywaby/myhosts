import platform
import os
from urllib import request as urlrequest
from .configure import Configure

class ActionBase():
    '''action base class'''
    def get_local_hosts(self, src):
        f = open(src, mode='rb')
        data=f.read()
        f.close()
        return data

    def get_remote_hosts(self, src):
        req = urlrequest.Request(src)
        if hasattr(Configure,'proxy'):
            if src.startswith('https://') and Configure.proxy.get('https'):
                req.set_proxy(Configure.proxy['https'], 'https')
                req.set_proxy(Configure.proxy['https'], 'https')
            elif src.startswith('http://')and Configure.proxy.get('https'):
                req.set_proxy(Configure.proxy['http'], 'http')
                req.set_proxy(Configure.proxy['http'], 'http')
        response = urlrequest.urlopen(req, timeout=20)
        data = response.read()
        return data

    def update(self, *sources):
        '''update system hosts from sources'''
        data=b''
        for type,src in sources:
            if type == 'local_hosts':
                src_path = Configure.local_hosts.get(src)
                if not src_path:
                    raise Exception('action (%s,%s) can not found'%(type, src))
                if not os.path.isfile(src_path):
                    raise Exception('file(%s) can not found'%(src_path))
                data += ('\n%s->%s START\n'%(type, src)).encode('utf-8')
                data += self.get_local_hosts(src_path)
                data += ('\n%s->%s END\n'%(type, src)).encode('utf-8')
            elif type == 'remote_hosts':
                src_link = Configure.remote_hosts.get(src)
                if not src_link:
                    raise Exception('action (%s,%s) can not found'%(type, src))
                print('%s->%s downloading...'%(type,src))
                data += ('\n%s->%s START\n'%(type, src)).encode('utf-8')
                data += self.get_remote_hosts(src_link)
                data += ('\n%s->%s END\n'%(type, src)).encode('utf-8')
            else:
                raise Exception('action source type error')

        if platform.system() == 'Windows':
            sys_root_path = os.getenv("SystemRoot")
            sys_hosts_path = os.path.join(sys_root_path, "System32\drivers\etc\hosts")
            sys_hosts = open(sys_hosts_path, mode='wb+')
            sys_hosts.write(data)
            sys_hosts.close()
            os.system('ipconfig /flushdns')
        elif platform.system() == "Linux":
            sys_hosts_path = '/etc/hosts'
            sys_hosts = open(sys_hosts_path, mode='wb')
            sys_hosts.write(data)
            sys_hosts.close()
            os.system('rcnscd restart')
        else:
            raise Exception('unsupport system')
        print('finish hosts update')

    def backup(self, path=None, name=None):
        '''backup system hosts to path'''
        import shutil
        import time
        if not path:
            path = Configure.backup_path if hasattr(Configure, 'backup_path') else ''
        if not name:
            name = "hosts" + time.strftime(" %Y-%m-%d %H-%M-%S", time.localtime())
        backup_path = os.path.join(path, name)
        if platform.system() == 'Windows':
            sys_root_path = os.getenv("SystemRoot")
            sys_hosts_path = os.path.join(sys_root_path, "System32\drivers\etc\hosts")
            shutil.copyfile(sys_hosts_path, backup_path)
        elif platform.system() == "Linux":
            sys_hosts_path = '/etc/hosts'
            shutil.copyfile(sys_hosts_path, backup_path)
        else:
            raise Exception('unsupport system')
        print('hosts backup:'+backup_path)
