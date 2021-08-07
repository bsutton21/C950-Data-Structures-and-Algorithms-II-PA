# Blake Sutton  -- Student ID: 001109490 

import datetime
from ReadCSVData import *
import csv

# class Distance(object):

first_opt_truck = []
first_opt_truck_ind = []
second_opt_truck = []
second_opt_truck_ind = []
third_opt_truck = []
third_opt_truck_ind =[]

# Reads in the addresses for each location/stop
# def read_addresses():
with open('Addresses.csv') as csvfile:
    addresses_csv = csv.reader(csvfile, delimiter=',')
    addresses_csv = list(addresses_csv)

# Reads in the distances between each of the locations
# def read_distances():
    # Reads in the distances between each of the locations
with open('Distances.csv') as csvfile:
    distances_csv = csv.reader(csvfile, delimiter=',')
    distances_csv = list(distances_csv)

# Complexity is O(1)
def get_distance(self, curr_id: int, dest_id):
    if curr_id == self.loc_id:
        return 0
    if curr_id < self.loc_id:
        return self.distances[curr_id]
    elif curr_id > self.loc_id:
        return self.parent_graph[curr_id].distances[self.loc_id]

# This calculates the distance between two locations
# Complexity is O(1)
def check_distance(rowval, columnval, sum):
    distance = addresses_csv[rowval][columnval]
    if distance is '':
        distance = addresses_csv[rowval][columnval]

    sum += float(distance)
    return sum

# This is similar to the function above but instead just returns the current distance
# Complexity is O(1)
def current_distance(rowval, columnval):
    distance = addresses_csv[rowval][columnval]
    if distance is'':
        distance = addresses_csv[rowval][columnval]

    return float(distance)

first_truck = ['8:00:00']
second_truck = ['9:10:00']
third_truck = ['11:00:00']

# This function takes a distance then divides it by 18. It then uses divmod to display a time and appends 00
# The resulting timestamp string is then split and turned into a datetime timedelta object, 
# which is then added to the sum that represents the total distance for a particular truck
# O(N)
def check_first_truck_time(distance):
    new_time = distance/18
    dist_in_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = dist_in_min + ':00'
    first_truck_status.append(final_time)
    sum = datetime.timedelta()
    for i in first_truck:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum

# Same but for second truck 
# O(N)
def check_second_truck_time(distance):
    new_time = distance/18
    dist_in_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = dist_in_min + ':00'
    second_truck.append(final_time)
    sum = datetime.timedelta()
    for i in second_truck:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum

# Same but for third truck 
# O(N)
def check_third_truck_time(distance):
    new_time = distance/18
    dist_in_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = dist_in_min + ':00'
    third_truck.append(final_time)
    sum = datetime.timedelta()
    for i in third_truck:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum

# O(1)
def check_address():
    return distances_csv

"""
This is my sorting algorithm.  I chose a greedy algorithm to handle this task.
This function takes three parameters:  1) a list of packages that hasn't been optimized, 2) a truck number, 
3) and the current locations that is updated each time the truck moves.

The base case is in the initial statement and will break recursion once the input size equals 0.
The lowest value is initialized to 100, which is greater than any actual delivery route, 
then it iterates through each possible delivery location to find the actual lowest value.
It uses this search to create a new list for each truck--first_opt_truck, second_opt_truck, third_opt_truck.
Each time that these lists are updated, the selected value is removed from the original list
Each truck is optimized using recursive functions.

The complexity is O(N^2) due to 2 for loops.
"""

def calc_short_dist(truck_dist_list, truck_num, curr_loc):
    if len(truck_dist_list) == 0:
        return truck_dist_list
    else:
        try:
            low_val = 100.0
            new_loc = 0
            for index in truck_dist_list:
                if current_distance(curr_loc, int(index[1])) <= low_val:
                    low_val = current_distance(curr_loc, int(index[1]))
                    new_loc = int(index[1])
            for index in truck_dist_list:
                if current_distance(curr_loc, int(index[1])) == low_val:
                    if truck_num == 1:
                        first_opt_truck.append(index)
                        first_opt_truck_ind.append(index[1])
                        pop_value = truck_dist_list.index(index)
                        truck_dist_list.pop(pop_value)
                        current_loc = new_loc
                        calc_short_dist(truck_dist_list, 1, current_loc)
                    elif truck_num == 2:
                        second_opt_truck.append(index)
                        second_opt_truck_ind.append(index[1])
                        pop_value = truck_dist_list.index(index)
                        truck_dist_list.pop(pop_value)
                        current_loc = new_loc
                        calc_short_dist(truck_dist_list, 2, current_loc)
                    elif truck_num == 3:
                        third_opt_truck.append(index)
                        third_opt_truck_ind.append(index[1])
                        pop_value = truck_dist_list.index(index)
                        truck_dist_list.pop(pop_value)
                        current_loc = new_loc
                        calc_short_dist(truck_dist_list, 3, current_loc)
        except IndexError:
            pass

# O(1)
def first_optimized_truck():
    return first_opt_truck

# O(1)
def first_opt_ind():
    return first_opt_truck_ind

# O(1)
def second_optimized_truck():
    return second_opt_truck

# O(1)
def second_opt_ind():
    return second_opt_truck_ind

# O(1)
def third_optimized_truck():
    return third_opt_truck

# O(1)
def third_opt_ind():
    return third_opt_truck_ind