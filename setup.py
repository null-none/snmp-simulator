from setuptools import setup

setup(
    name='xee-snmp-simulator',
    description='XeeMetric SNMP Simulator',
    version='0.5.2',
    author='Dmitry Korobitsin',
    author_email='korobicin@gmail.com',
    url='https://github.com/xeemetric/xee-snmp-simulator',
    packages=['xee_snmp_simulator', 'xee_snmp_simulator.packages'],
    install_requires=['pysnmp==4.2.5'],
    entry_points={
        'console_scripts': [
            'simulator = xee_snmp_simulator.simulator:main',
        ],
    },
    platforms=['Any'],
    license='BSD',
    zip_safe=False,
)
