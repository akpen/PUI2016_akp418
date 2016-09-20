import sys
import pylab as pl
import json
import urllib as ulr
import os

dev_key = sys.argv[1]
bus_line = sys.argv[2]
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + str(dev_key) + '&VehicleMonitoringDetailLevel=calls&LineRef=' + str(bus_line)

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


bus_count = 0
count = 0

print 'Bus Line: ' + str(bus_line)

for i in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    bus_count = bus_count + 1

print "No: of Buses: " + str(bus_count)

for i in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    count = count + 1
    print 'Bus '+ str(count) + ' is at ' + 'latitude ' + str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + ' and' + ' longitude ' + str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])