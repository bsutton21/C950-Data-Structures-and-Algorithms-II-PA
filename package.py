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
    first_truck_dist_list = []
    second_truck_dist_list = []
    third_truck_dist_list = []
    # the times below represent the times that each truck leaves the hub
    first_time = '8:00:00'
    second_time = '9:10:00'
    third_time = '11:00:00'

    