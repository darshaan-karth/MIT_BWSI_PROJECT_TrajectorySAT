"""
Setup - Raspberry Pi 4B
=======================

1. Enter "hciconfig -a" into the command line and COPY the address
2. Type "sudo bluetoothctl"
3. Enter these values into the "[bluetooth]#" prompt
    -> discoverable on
    -> pairable on
    -> agent on
    -> default-agent
    -> scan on

Connecting From Computer
========================
1. Copy the Physical Address from the cmd using "ipconfig /all" and search Physical Address under Ethernet adapter Bluetooth Network Connection 

Pairing
=======
1. In the bluetooth prompt in Raspberry Pi enter:
    -> pair <PHYSICAL_ADDRESS OF THE COMPUTER>
    -> yes

RSSI Measurment Raspi Command
=============================
"sudo btmgmt find|grep <MAC ADDRESS>"
"""