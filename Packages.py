# Blake Sutton  -- Student ID: 001109490 

from Distances import *
from ReadCSVData import *

import datetime

# class Package(object):
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
    print("Package ID: %i" % self.package_id)
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

# Updates the delivery status of all packages in the first truck when it leaves the station
i = 0
# O(N)
for value in first_truck_status():
    first_truck_status()[i][9] = first_time
    first_delivery.append(first_truck_status()[i])
    i+=1

# Compares the addresses on the first truck to the main address list and adds the address index to the list
# O(N^2)
try:
    first_count = 0
    for j in first_delivery:
        for k in check_address():
            if k[2] == j[2]:
                first_truck.append(j[0])
                first_delivery[first_count][1] = j[0]
        first_count += 1
except IndexError:
    pass

calc_short_dist(first_delivery, 1, 0)
first_truck_dist = 0

# This for loops uses the greedy sorting algorithm in Distance.py to determine the best route and calculates the distance
# O(N)
first_truck_pack_id = 0
for index in range(len(first_opt_ind())):
    try:
        # Calculate the total distance of the truck
        first_truck_dist = calc_short_dist(int(first_opt_ind()[index]), int(first_opt_ind()[index + 1]), first_truck_dist)
        # Calculate the distance of each pacakage along the route
        package_delivery = calc_short_dist(current_distance(int(first_opt_ind()[index]), int(first_opt_ind()[index + 1])))
        first_optimized_truck()[first_truck_pack_id][10] = (str(package_delivery))
        get_hashtable.update(int(first_optimized_truck()[first_truck_pack_id][10]), first_delivery)
        first_truck_pack_id += 1
    except IndexError:
        pass

# Updates the delivery status of all packages in the second truck when it leaves the station
i = 0
# O(N)
for value in second_truck_status():
    second_truck_status()[i][9] = second_time
    second_delivery.append(second_truck_status()[i])
    i+=1

# Compares the addresses on the second truck to the main address list and adds the address index to the list
# O(N^2)
try:
    second_count = 0
    for j in second_delivery:
        for k in check_address():
            if k[2] == j[2]:
                second_truck.append(j[0])
                second_delivery[second_count][1] = j[0]
        second_count += 1
except IndexError:
    pass

calc_short_dist(second_delivery, 1, 0)
second_truck_dist = 0

# Same as with the first truck
# This for loops uses the greedy sorting algorithm in Distance.py to determine the best route and calculates the distance
# O(N)
second_truck_pack_id = 0
for index in range(len(second_opt_ind())):
    try:
        # Calculate the total distance of the truck
        second_truck_dist = calc_short_dist(int(second_opt_ind()[index]), int(second_opt_ind()[index + 1]), second_truck_dist)
        # Calculate the distance of each pacakage along the route
        package_delivery = calc_short_dist(current_distance(int(second_opt_ind()[index]), int(second_opt_ind()[index + 1])))
        second_optimized_truck()[second_truck_pack_id][10] = (str(package_delivery))
        get_hashtable.update(int(second_optimized_truck()[second_truck_pack_id][10]), second_delivery)
        second_truck_pack_id += 1
    except IndexError:
        pass

# Updates the delivery status of all packages in the third truck when it leaves the station
i = 0
# O(N)
for value in third_truck_status():
    third_truck_status()[i][9] = third_time
    third_delivery.append(third_truck_status()[i])
    i+=1

# Compares the addresses on the third truck to the main address list and adds the address index to the list
# O(N^2)
try:
    third_count = 0
    for j in third_delivery:
        for k in check_address():
            if k[2] == j[2]:
                third_truck.append(j[0])
                third_delivery[third_count][1] = j[0]
        third_count += 1
except IndexError:
    pass

calc_short_dist(third_delivery, 1, 0)
third_truck_dist = 0

# Same as with the first two trucks
# This for loops uses the greedy sorting algorithm in Distance.py to determine the best route and calculates the distance
# O(N)
third_truck_pack_id = 0
for index in range(len(third_opt_ind())):
    try:
        # Calculate the total distance of the truck
        third_truck_dist = calc_short_dist(int(third_opt_ind()[index]), int(third_opt_ind()[index + 1]), third_truck_dist)
        # Calculate the distance of each pacakage along the route
        package_delivery = calc_short_dist(current_distance(int(third_opt_ind()[index]), int(third_opt_ind()[index + 1])))
        third_optimized_truck()[third_truck_pack_id][10] = (str(package_delivery))
        get_hashtable.update(int(third_optimized_truck()[third_truck_pack_id][10]), third_delivery)
        third_truck_pack_id += 1
    except IndexError:
        pass

# Calculates the total distance traveled by all three trucks
# O(1)
def total_distance():
    total_distance = first_truck_dist + second_truck_dist + third_truck_dist
    return total_distance