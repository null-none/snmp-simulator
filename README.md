# xee-snmp-simulator

SNMP Simulator is a simple tool to simulate an SNMP agent based on its SNMP walk file.


## Docker deployment

> You need to mention `udp` in Docker's port mapper

Assuming you are running Docker on Linux/x86-64.

    $ docker run -p 161:161/udp xeemetric/xee-snmp-simulator

With custom walk file:

    $ docker run -p 161:161/udp -v /custom.walk:/cisco_2801.walk xeemetric/xee-snmp-simulator


## Conventional deployment

> You need root to use the default `udp/161`

Assuming you are running Ubuntu 15.04.

    $ sudo apt-get update && apt-get install python-pip
    $ sudo pip install xee-snmp-simulator
    $ sudo simulator -s --walk_file <walk_file>


## Creating a walk file

> *Timeout: No Response* reported by `snmpbulkwalk` might related to too big response PDU. This can be avoided by setting `max-repeaters` to a smaller value using `-Cr<max-repeaters>` flag

Assuming you have [Net-SNMP](http://www.net-snmp.org) CLI tools installed.

    $ snmpbulkwalk -v2c -Oen -Cr5 -r3 -t3 -c <community> <host> 1.3.6 > custom.walk


## Playing with Simulator

    $ snmpget -v2c -c public 127.0.0.1 sysDescr.0


## Author

Developed and maintained by [Dmitry Korobitsin](https://github.com/korobitsin).

Sponsored by [XeeMetric, Inc](http://xeemetric.com)
