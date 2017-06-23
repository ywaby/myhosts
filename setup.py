"""
myhosts is a hosts manager tool write with python.
myhosts can updata hosts from remote & local.
myhosts can be used to switch hosts between diffrent scene.
project at "https://github.com/ywaby/myhosts"
"""
from setuptools import setup

setup(name='myhosts',
      description='myhosts,hosts manager tool',
      version='0.1.1',
      license='LGPL-3.0',
      author='ywaby',
      author_email='ywaby@163.com',
      url='https://github.com/ywaby/myhosts',
      keywords="hosts manager tool",
      packages=['myhosts'],
      entry_points={
          'console_scripts': [
              'myhosts = myhosts.__main__:main'
          ]
      },
      )
