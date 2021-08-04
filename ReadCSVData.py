# Blake Sutton  -- Student ID: 001109490 

import csv
import datetime
from Hashtable import HashTable

create_hash_table = HashTable()  # Calls the Hashtable class to create an object of Hashtable

first_truck = []  # list to represent the first truck delivery
second_truck = [] # list to represent the second truck delivery
third_truck = [] # list to represent the third truck delivery

# Reads in the names of all of the possible delivery locations
def read_packages():
    with open('Packages.csv') as csvfile:
        packages_csv = csv.reader(csvfile, delimiter=',')
        packages_csv = list(packages_csv)

def read_full_address_data():
    with open('Full Package Data.csv') as csvfile:
        full_package_csv = csv.reader(csvfile, delimiter=',')

        for row in full_package_csv:
            package_ID_row_value = row[0]
            address_row_value = row[1]
            city_row_value = row[2]
            state_row_value = row[3]
            zip_row_value = row[4]
            delivery_row_value = row[5]
            size_row_value = row[6]
            note_row_value = row[7]
            delivery_start = ''
            address_location = ''
            delivery_status = 'At hub'
            iterate_value = [package_ID_row_value, address_location, address_row_value, city_row_value, state_row_value,
                             zip_row_value, delivery_row_value, size_row_value, note_row_value, delivery_start,
                             delivery_status]

            key = package_ID_row_value
            value = iterate_value

            # I manually sorted the packages on the trucks since for a shipping company of this size,
            # it's reasonable to think that management cound still do this manually

            # Rules followed while sorting:
            # Truck 1: Earliest times, co-delivery requirements, ZIP code proximity
            # Truck 2: Packages delayed until 9:05 with deadline by 10:30, some packages required to be on truck 2, ZIP code proximity
            # Truck 3: Remaining packages
            truck1_id_list = [1,4,13,14,15,16,19,20,21,24,34,39,40]
            truck2_id_list = [3,5,6,7,18,22,25,26,28,29,31,32,36,37,38]
            truck3_id_list = [2,8,9,10,11,12,17,23,27,30,33,35]

            if package_ID_row_value in truck1_id_list:
                first_truck.append(value)

            elif package_ID_row_value in truck2_id_list:
                second_truck.append(value)

            elif package_ID_row_value in truck3_id_list:
                third_truck.append(value)

            create_hash_table.add(key, value)

def get_hashtable():
    return create_hash_table

def sort_packages():
    truck1 = [1,4,13,14,15,16,19,20,21,24,34,39,40]
    truck2 = [3,5,6,7,18,22,25,26,28,29,31,32,36,37,38]
    truck3 = [2,8,9,10,11,12,17,23,27,30,33,35]
    return truck1, truck2, truck3

def first_truck_status():
    return first_truck
    
def second_truck_status():
    return second_truck

def third_truck_status():
    return third_truck