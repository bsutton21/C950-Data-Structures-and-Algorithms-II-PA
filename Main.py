# Blake Sutton  -- Student ID: 001109490 

from read_csv import *
import sys
from distance import Distance
import datetime

package_table = read_packages
distance_table = read_distances

class Main:
    # This displays when the programs is started
    print('Welcome to the WGUPS package tracking system!')
    print('Current route was completed in', "{0:.2f}".format(total_distance(), 2), 'miles.')
    start = input("To begin, please type 'lookup' to search for an individual package or "
                  "type 'timestamp' to view delivery status at a given time.  Type 'exit' to exit the program.")

    while start is not 'exit':
        # if user types 'timestamp' then the the program asks for a time to display.  The program then all remaining packages as of that time.
        # runtime is O(N)
        if start == 'timestamp':
            try:
                user_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = user_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # O(N^2)
                for count in range(1, 41):
                    try:
                        first_time = get_hashtable().get(str(count))[9]
                        second_time = get_hashtable().get(str(count))[10]
                        (h, m, s) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                    # First checks all packages against the entered time to determine if there is enough time for delivery
                    if convert_first_time >= convert_user_time:
                        get_hashtable().get(str(count))[10] = 'At Hub'
                        get_hashtable().get(str(count))[9] = 'Leaves at ' + first_time
                        print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                              get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                              get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                              '  Required delivery time:', get_hashtable().get(str(count))[6],
                              ' Package weight:', get_hashtable().get(str(count))[7], '  Truck status:',
                              get_hashtable().get(str(count))[9], '  Delivery status:',
                              get_hashtable().get(str(count))[10])
                    elif convert_first_time <= convert_user_time:
                        # Then checks to see which packages have left the hub but have not been delivered yet
                        if convert_user_time < convert_second_time:
                            get_hashtable().get(str(count))[10] = 'In transit'
                            get_hashtable().get(str(count))[9] = 'Left at ' + first_time
                            print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                                  get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                                  get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                                  '  Required delivery time:', get_hashtable().get(str(count))[6],
                                  ' Package weight:', get_hashtable().get(str(count))[7], '  Truck status:',
                                  get_hashtable().get(str(count))[9], '  Delivery status:',
                                  get_hashtable().get(str(count))[10])
                        # Finally checks all packages that have already been delivered and displays the delivered time
                        else:
                            get_hashtable().get(str(count))[10] = 'Delivered at ' + second_time
                            get_hashtable().get(str(count))[9] = 'Left at ' + first_time
                            print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                                  get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                                  get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                                  '  Required delivery time:', get_hashtable().get(str(count))[6],
                                  ' Package weight:', get_hashtable().get(str(count))[7],'  Truck status:',
                                  get_hashtable().get(str(count))[9],'  Delivery status:',
                                  get_hashtable().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid Entry!')
                exit()
        # If 'lookup' is enter then the user is prompted for a package ID followed by a timestamp
        elif start == 'lookup':
            try:
                count = input('Which package would you like to lookup?: ')
                first_time = get_hashtable().get(str(count))[9]
                second_time = get_hashtable().get(str(count))[10]
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # First checks if the package has left the hub yet
                if convert_first_time >= convert_user_time:

                    get_hashtable().get(str(count))[10] = 'At Hub'
                    get_hashtable().get(str(count))[9] = 'Leaves at ' + first_time
                    print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                          get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                          get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                          '  Required delivery time:', get_hashtable().get(str(count))[6],
                          ' Package weight:', get_hashtable().get(str(count))[7], '  Truck status:',
                          get_hashtable().get(str(count))[9], '  Delivery status:',
                          get_hashtable().get(str(count))[10])
                elif convert_first_time <= convert_user_time:
                    # Then checks if the package has left the hub but has not been delivered yet
                    if convert_user_time < convert_second_time:
                        get_hashtable().get(str(count))[10] = 'In transit'
                        get_hashtable().get(str(count))[9] = 'Left at ' + first_time
                        print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                              get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                              get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                              '  Required delivery time:', get_hashtable().get(str(count))[6],
                              ' Package weight:', get_hashtable().get(str(count))[7], '  Truck status:',
                              get_hashtable().get(str(count))[9], '  Delivery status:',
                              get_hashtable().get(str(count))[10])
                    # If the package has already been delivered than it displays the time
                    else:
                        get_hashtable().get(str(count))[10] = 'Delivered at ' + second_time
                        get_hashtable().get(str(count))[9] = 'Left at ' + first_time
                        print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                              get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                              get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                              '  Required delivery time:', get_hashtable().get(str(count))[6],
                              ' Package weight:', get_hashtable().get(str(count))[7], '  Truck status:',
                              get_hashtable().get(str(count))[9], '  Delivery status:',
                              get_hashtable().get(str(count))[10])
            except ValueError:
                print('Invalid entry')
                exit()
        elif start == 'exit':
            exit()
        else:
            print('Invalid entry!')
            exit()
"""

visited_locations = []
def dijkstra_sp(current_location, truckload):
    
    # Arbitrarily initializing the shortest_route variable so that it's longer than the longest possible route.
    # This has the effect of <any> route being shorter, even if there's only one left.
    shortest_route = 100.0
    next_package = None
    next_address = None 
    
    unvisited = []
    for i in truckload:
        i.reset_path()
        unvisited.append(i)
    
    start_dist = 0

    while(len(unvisited) != 0):
        current_loc = unvisited.pop(0)

        for loc in unvisited:
            current_dist = current_loc.get_distance(loc.loc_id)
            alternate_path = current_loc.shortest_known_path + current_dist

            if alternate_path < loc.shortest_known_path:
                loc.shortest_known_path = alternate_path
                loc.previous_location = current_loc

    for pack_num in truckload:
        # Get package object
        package = package_table.get_item(pack_num)



def run_delivery():
    # Sort the packages onto the trucks
    t1, t2, t3 = sort_packages
    # Truck 1 leaves at 8AM
    t1_start_time = 480
    # Truck 2 leaves at 9:06AM after the delayed packages arrive
    t2_start_time = 546
    # t3_start_time = TO_DO

    # t1_distance = 
    # t2_distnace = 
    # t3_distance = 

def deliver_packages(truck, route_time):
    for pack_id in truck:
        package = package_table.get_item(pack_id)
        package.status = "En route"

    # The hub is the starting location of '0'
    num = 0
    total_distance = 0

    # for i in range(len(truck)):

def reset_path(self):  # O(1)
    self.shortest_known_path = sys.maxsize
    self.previous_location = None
"""