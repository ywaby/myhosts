import sys
import platform
import os
import urllib.request
'''
backup hosts current path 'host time'
'''
v6host_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
v4host_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
def update_host():
    try:
        import time
        import shutil
        response = urllib.request.urlopen(v4host_url)
        hosts_data = response.read()        
        print('hosts download success!')
        if platform.system() == 'Windows':
            path_systemroot = os.getenv("SystemRoot")
            path_host = os.path.join(path_systemroot, "System32\drivers\etc\hosts")
            path_host_bak = "host "+ time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            shutil.copyfile(path_host, path_host_bak)
            fhosts = open(path_host, mode='wb+')
            fhosts.write(hosts_data)
            fhosts.close()
            os.system('ipconfig /flushdns')
        elif platform.system() == "Linux":
            os.system('cp /etc/hosts.txt /etc/hosts_bak')
            os.system('mv ./hosts /etc/hosts')
            os.system('sudo /etc/init.d/networking restart ')
    except Exception as e:
        print(e)
    print('finish update')
    return

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='myhosts',
                                        description='update hosts from github',
                                        epilog="project at: www.github.ywaby.pytk.com")
    parser.add_argument('-v', "--version", help="print version", action='version', version='%(prog)s 0.0.1')
    args = parser.parse_args()
    update_host()
    os.system('pause')
