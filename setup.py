"""
myhosts is a hosts manager tool write with python.
myhosts can updata hosts from remote & local.
myhosts can be used to switch hosts between diffrent scene.
project at "https://github.com/ywaby/myhosts"
"""
from setuptools import setup
from os.path import expanduser

setup(
    name='myhosts',
    description='hosts manager tool',
    version='0.2.0',
    license='MIT',
    author='ywaby',
    author_email='ywabygl@gmail.com',
    url='https://github.com/ywaby/myhosts',
    keywords="hosts manager tool",
    py_modules=['myhosts'],
    entry_points={'console_scripts': ['myhosts = myhosts:main']},
    classifiers=[
        'Development Status :: 3 - Apah',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: hosts manager',
    ],
    data_files=[
        (expanduser('~/.config/myhosts'), ['config/myhosts/config.json']),
        (expanduser('~/.config/myhosts'), ['config/myhosts/extra_hosts'])
        # (expanduser('~/.config/myhosts'), ['config/myhosts/backup'])
    ]
)
