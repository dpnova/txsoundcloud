import re

from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

version = None
for line in open('./txsoundcloud/__init__.py'):
    m = re.search('__version__\s*=\s*(.*)', line)
    if m:
        version = m.group(1).strip()[1:-1]  # quotes
        break
assert version

setup(
    name='txsoundcloud',
    version=version,
    description='A friendly wrapper library for the Soundcloud API',
    author='Paul Osman',
    author_email='osman@soundcloud.com',
    url='https://github.com/dpnova/txsoundcloud',
    license='BSD',
    packages=['txsoundcloud'],
    include_package_data=True,
    use_2to3=True,
    package_data={
        '': ['README.rst']
    },
    install_requires=[
        'fudge==1.0.3',
        'klein>=0.2.3',
        'treq>=0.2.1'
        'simplejson>=2.0',
    ],
    tests_require=[
        'nose>=1.1.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
