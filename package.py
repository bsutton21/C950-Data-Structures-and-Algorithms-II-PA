# Blake Sutton  -- Student ID: 001109490 

from distance import *
from read_csv import *

import datetime

class Package(object):
    def __init__(self, plist):
        self.package_id = int(plist[0])
        self.address = plist[1]
        self.city = plist[2]
        self.state = plist[3]
        self.zip = plist[4]
        self.deadline = plist[5]
        self.weight = plist[6]
        self.notes = plist[7]
        self.delivery_time = "00:00"
        self.delivery_status = "At hub"
    
    def print_package(self):
        Print("Package ID: %i" % self.package_id)
        print("Address:  %s" % self.address)
        print("City: %s" % self.city)
        print("State: %s" % self.state)
        print("Zip: %s" % self.zip)
        print("Deadline: %s" % self.deadline)
        print("Weight: %s" % self.weight)
        print("Notes: %s" % self.notes)
        print("Delivery Time: %s" % self.delivery_time)
        print("Status: %s" % self.delivery_status)

    first_delivery = []
    second_delivery = []
    third_delivery = []
    first_truck = []
    second_truck = []
    third_truck = []
    # the times below represent the times that each truck leaves the hub
    first_time = '8:00:00'
    second_time = '9:10:00'
    third_time = '11:00:00'

    # Convert string datetime into datetime.timedelta
    (h, m, s) = first_time.split(':')
    convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    (h, m, s) = second_time.split(':')
    convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    (h, m, s) = third_time.split(':')
    convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    # Updates the delivery status of all packages in truck 1 when it leaves the station
    i = 0
    # O(N)
    for value in first_truck_status():
        first_truck_staus()[i][9] = first_time
        first_delivery.append(first_truck_status()[i])
        i+=1