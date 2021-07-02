# Blake Sutton  -- Student ID: 001109490 

import csv
import datetime
from hashtable import HashTable

# Reads in the distances between each of the locations
def read_distances():
    with open('Distances.csv') as csvfile:
        distance_csv = csv.reader(csvfile, delimiter=',')
        distance_csv = list(distance_csv)

# Reads in the names of all of the possible delivery locations
def read_packages():
    with open('Packages.csv') as csvfile:
        packages_csv = csv.reader(csvfile, delimiter=',')
        packages_csv = list(packages_csv)

# This calculates the distance between two locations
# Complexity is O(1)
def check_distance(rowval, columnval, sum):
    distance = distance_csv[rowval][columnval]
    if distance is '':
        distance = distance_csv[rowval][columnval]

    sum += float(distance)
    return sum

# This is similar to the function above but instead just returns the current distance
# Complexity is O(1)
def current_distance(rowval, columnval):
    distance = distance_csv[rowval][columnval]
    if distance is'':
        distance = distance_csv[rowval][columnval]

    return float(distance)

first_truck = ['8:00:00']
second_truck = ['9:10:00']
third_truck = ['11:00:00']

# this function takes a distance then divides it by 18. It then uses divmod to display a time and appends 00
# this string that is a timestamp is then split and turned into a datetime timedelta object, 
# which is then added to the sum, which is represents the total distance for a particular truck
# Complexity is O(N)
def check_first_truck_time(distance):
    new_time = distance/18
    dist_in_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = dist_in_min + ':00'
    first_truck.append(final_time)
    sum = datetime.timedelta()
    for i in first_truck:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum

# same but for second truck
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

# same but for third truck
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

    