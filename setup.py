from setuptools import setup

setup(
    name='snmp-simulator',
    description='A simple SNMP Simulator driven by agent\'s snmpwalk',
    version='0.6.0',
    author='Dmitry Korobitsin',
    author_email='korobicin@gmail.com',
    url='https://github.com/xeemetric/snmp-simulator',
    packages=['snmp_simulator', 'snmp_simulator.packages'],
    install_requires=['pysnmp==4.4.12'],
    entry_points={
        'console_scripts': [
            'snmp-simulator = snmp_simulator.simulator:main',
        ],
    },
    platforms=['Any'],
    license='BSD',
    zip_safe=False,
)
