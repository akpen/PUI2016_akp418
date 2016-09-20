import sys
import pylab as pl
import json
import urllib as ulr
import os
import csv

dev_key = sys.argv[1]
bus_line = sys.argv[2]

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + str(dev_key) + \
'&VehicleMonitoringDetailLevel=calls&LineRef=' + str(bus_line)

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

f = open(sys.argv[3], 'wb')
writer = csv.writer(f, delimiter= ',')
writer.writerow(['Latitude','Latitude', 'Stop Name', 'Stop Status'])

count = 0

data_srt = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

csv_doc = []

for i in data_srt:
    count = count + 1
    
    latitude = str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    longitude = str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        
    if (data_srt[0]['MonitoredVehicleJourney']['OnwardCalls'] == {}):
            stop_name = 'NA'
            bus_status = 'NA'
    
    else: 
        stop_name = str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        bus_status = str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    
    writer.writerow([latitude,longitude,stop_name,bus_status])
