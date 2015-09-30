xee-snmp-simulator
==================

XeeMetric SNMP Simuslator is a simple tool to simulate an SNMP agent based on its SNMP walk file.

Docker Deployment
=================

Assuming you are running Docker on Linux/x86-64.
Please note that you need to mention UDP in Docker's port mapper (by default it's TCP).

````
$ docker run -p 161:161/udp xeemetric/xee-snmp-simulator
````

Conventional Deployment
=======================

Assuming you are running Ubuntu 15.04.
Note that you need root to run on udp/161.

````
$ sudo apt-get update && apt-get install python-pip
$ sudo pip install xee-snmp-simulator
$ sudo simulator -s --walk_file <walk_file>
````

Using custom walk file
======================

Assuming you are running Ubuntu 15.04 and have simulator installed.

````
$ sudo apt-get update && apt-get install snmp
$ snmpbulkwalk -v2c -Oen -c <community> <host> 1.3.6 > mydevice.conf
$ simulator --walk_file mydevice.conf &
$ snmpget -v 2c -c public 127.0.0.1 1.3.6.1.2.1.1.1.0
````

Author
======

Developed and maintained by [Dmitry Korobitsin](https://github.com/korobitsin).

Sponsored by [XeeMetric, Inc](http://xeemetric.com)
