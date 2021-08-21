# Blake Sutton  -- Student ID: 001109490 

import csv
from Hashtable import HashTable

create_hash_table = HashTable()  # Calls the Hashtable class to create an object of Hashtable

first_truck = [] # list to represent the first truck delivery
second_truck = [] # list to represent the second truck delivery
third_truck = [] # list to represent the third truck delivery

# Reads in the names of all of the possible delivery locations
# O(1)
with open('Packages.csv') as csvfile:
    packages_csv = csv.reader(csvfile, delimiter=',')
    packages_csv = list(packages_csv)

# O(N)
with open('Full Package Data.csv') as csvfile:
    full_package_csv = csv.reader(csvfile, delimiter=',')

    for row in full_package_csv:
        package_ID_value = row[0]
        address_value = row[1]
        city_value = row[2]
        state_value = row[3]
        zip_value = row[4]
        delivery_value = row[5]
        size_value = row[6]
        note_value = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'
        iterate_value = [package_ID_value, address_location, address_value, city_value, state_value,
                            zip_value, delivery_value, size_value, note_value, delivery_start,
                            delivery_status]

        key = package_ID_value
        value = iterate_value

        # I manually sorted the packages on the trucks since for a shipping company of this size,
        # it's reasonable to think that management could still do this manually

        # Rules followed while sorting:
        # Truck 1: Earliest times, co-delivery requirements, ZIP code proximity
        # Truck 2: Packages delayed until 9:05 with deadline by 10:30, some packages required to be on truck 2, ZIP code proximity
        # Truck 3: Remaining packages
        truck1_id_list = [1, 4, 7, 13, 14, 15, 16, 19, 20, 21, 29, 34, 39, 40] # 14 packages
        truck2_id_list = [3, 5, 6, 8, 10, 18, 22, 25, 26, 30, 31, 32, 36, 37, 38] # 15 packages
        truck3_id_list = [2, 9, 11, 12, 17, 23, 24, 27, 28, 33, 35] # 11 packages

        if int(package_ID_value) in truck1_id_list:
            if package_ID_value == '15':
                first_truck.insert(0, value)
                create_hash_table.add(key, value) 
            if not first_truck: # base case appends if empty set
                first_truck.append(value)
                create_hash_table.add(key, value) 
            else:
                for count, first_values in enumerate(first_truck):
                    if value in first_truck:
                        break
                    if value[2] == first_values[2]:
                        first_truck.insert((count), value)
                        create_hash_table.add(key, value) 
                        break
                if value not in first_truck:
                    first_truck.append(value)
                    create_hash_table.add(key, value)

        elif int(package_ID_value) in truck2_id_list:
            if not second_truck: # base case appends if empty set
                second_truck.append(value)
                create_hash_table.add(key, value) 
            else:
                for count, second_values in enumerate(second_truck):
                    if value in second_truck:
                        break
                    if value[2] == second_values[2]:
                        second_truck.insert((count), value)
                        create_hash_table.add(key, value)
                        break
                if value not in second_truck:
                    second_truck.append(value)
                    create_hash_table.add(key, value)

        elif int(package_ID_value) in truck3_id_list:
            if not third_truck: # base case appends if empty set
                third_truck.append(value)
                create_hash_table.add(key, value) 
            else:
                for count, third_values in enumerate(third_truck):
                    if value in third_truck:
                        break
                    if value[2] == third_values[2]:
                        third_truck.insert((count), value)
                        create_hash_table.add(key, value)
                        break
                if value not in third_truck:
                    third_truck.append(value)
                    create_hash_table.add(key, value)

# Create object of hash table
# O(1)
def get_hashtable():
    return create_hash_table

# Create object of the first truck
# O(1)
def first_truck_status():
    return first_truck

# Create object of the second truck
# O(1)
def second_truck_status():
    return second_truck

# Create object of the third truck
# O(1)
def third_truck_status():
    return third_truck