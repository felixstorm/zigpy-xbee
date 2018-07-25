"""Setup module for zigbpy-xbee"""

from setuptools import find_packages, setup

setup(
    name="zigpy-xbee",
    version="0.1.1.devfstorm0",
    description="A library which communicates with XBee radios for zigpy",
    url="http://github.com/zigpy/zigpy-xbee",
    author="Russell Cloran",
    author_email="rcloran@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude=['*.tests']),
    install_requires=[
        'pyserial-asyncio',
        'zigpy',
    ],
    dependency_links=[
        'https://github.com/felixstorm/zigpy/archive/master.zip#zigpy==0.1.0.devfstorm0',
    ],
    tests_require=[
        'pytest',
    ],
)
