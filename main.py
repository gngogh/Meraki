import meraki
import os
import config as CFG

hosts = CFG.conf('hosts.yml')
hosts.data()

API_KEY = os.environ['API_KEY']

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

for n, s in hosts.data()['lvl73']['devices'].items():
    reboot = dashboard.devices.rebootDevice(serial=s)
