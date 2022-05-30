# Meraki

An example of how to use Ansible and Python.

Usage:

API key is stored in a env variable

$sudo nano ~/.bashrc

$[sudo] password for yourmachine:

variable name="key"

mysecretcode="ITSASECRET"

Inventory is stored in the hosts.yml, with the following structure

sitename:

  devices:
  
    deviceName: serial number


For ansible Job run the script from main.yml

For testing run the script from main.py
