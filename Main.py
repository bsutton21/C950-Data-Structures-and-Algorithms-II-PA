# Blake Sutton  -- Student ID: 001109490 

from ReadCSVData import get_hashtable
import datetime
from Packages import total_distance

class Main:
    # This is the main UI that displays to users to navigate and search
    print('Welcome to the WGUPS package tracking system!')
    print('All packages delivered in', "{0:.2f}".format(total_distance(), 2), 'miles.')
    start = input("To begin, please type 'lookup' to search for an individual package or "
                  "type 'timestamp' to view delivery status at a given time.  Type 'exit' to exit the program. ")
    # the programs continues to listen for input until the user enters 'exit'
    # total complexity: O(N)
    while start is not 'exit':
        # if user types 'timestamp' then the the program asks for a time to display.  
        # The program then displays all remaining packages as of that time.
        # runtime is O(N)
        if start == 'timestamp':
            try:
                user_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = user_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # O(N)
                for count in range(1, 41):
                    try:
                        departure_time = get_hashtable().get(str(count))[9]
                        delivery_time = get_hashtable().get(str(count))[10]
                        (h, m, s) = departure_time.split(':')
                        convert_departure_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = delivery_time.split(':')
                        convert_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                    # First checks all packages against the entered time to determine if there is enough time for delivery
                    if convert_departure_time >= convert_user_time:
                        temp_delivery_status = 'At Hub'
                        truck_status = departure_time
                        print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                              get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                              get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                              '  Required delivery time:', get_hashtable().get(str(count))[6],
                              '  Package weight:', get_hashtable().get(str(count))[7], '  Truck status: Leaves at ',
                              str(truck_status), '  Delivery status:',
                              temp_delivery_status)
                    elif convert_departure_time <= convert_user_time:
                        # Then checks to see which packages have left the hub but have not been delivered yet
                        if convert_user_time < convert_delivery_time:
                            temp_delivery_status = 'In transit'
                            truck_status = departure_time
                            print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                                  get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                                  get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                                  '  Required delivery time:', get_hashtable().get(str(count))[6],
                                  '  Package weight:', get_hashtable().get(str(count))[7], '  Truck status: Left at ',
                                  get_hashtable().get(str(count))[9], '  Delivery status:',
                                  temp_delivery_status)
                        # Finally checks all packages that have already been delivered and displays the delivered time
                        else:
                            temp_delivery_status = 'Delivered'
                            truck_status = departure_time
                            print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                                  get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                                  get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                                  '  Required delivery time:', get_hashtable().get(str(count))[6],
                                  '  Package weight:', get_hashtable().get(str(count))[7],'  Truck status: Left at ',
                                  get_hashtable().get(str(count))[9],'  Delivery status: ',
                                  temp_delivery_status, ' at ', get_hashtable().get(str(count))[10])

            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid Entry!')
                exit()
        # If 'lookup' is entered then the user is prompted for a package ID followed by a timestamp.
        # The program then displays all relevant information for that package at that time.
        elif start == 'lookup':
            try:
                count = input('Please type the package ID that you would like to lookup?: ')
                departure_time = get_hashtable().get(str(count))[9]
                delivery_time = get_hashtable().get(str(count))[10]
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = departure_time.split(':')
                convert_departure_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = delivery_time.split(':')
                convert_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # First checks if the package has left the hub yet
                if convert_departure_time >= convert_user_time:
                    temp_delivery_status = 'At Hub'
                    truck_status = departure_time
                    print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                        get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                        get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                        '  Required delivery time:', get_hashtable().get(str(count))[6],
                        '  Package weight:', get_hashtable().get(str(count))[7], '  Truck status: Leaves at ',
                        get_hashtable().get(str(count))[9], '  Delivery status:',
                        temp_delivery_status)
                elif convert_departure_time <= convert_user_time:
                    # Then checks if the package has left the hub but has not been delivered yet
                    if convert_user_time < convert_delivery_time:
                        temp_delivery_status = 'In transit'
                        truck_status = departure_time
                        print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                            get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                            get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                            '  Required delivery time:', get_hashtable().get(str(count))[6],
                            '  Package weight:', get_hashtable().get(str(count))[7], '  Truck status: Left at ',
                            get_hashtable().get(str(count))[9], '  Delivery status:',
                            temp_delivery_status)
                    # If the package has already been delivered than it displays the time
                    else:
                        temp_delivery_status = 'Delivered'
                        truck_status = departure_time
                        print('Package ID:', get_hashtable().get(str(count))[0], '   Street address:',
                            get_hashtable().get(str(count))[2], get_hashtable().get(str(count))[3],
                            get_hashtable().get(str(count))[4], get_hashtable().get(str(count))[5],
                            '  Required delivery time:', get_hashtable().get(str(count))[6],
                            '  Package weight:', get_hashtable().get(str(count))[7], '  Truck status: Left at ',
                            get_hashtable().get(str(count))[9], '  Delivery status:',
                            temp_delivery_status, ' at ', get_hashtable().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()

        elif start == 'exit':
            exit()
        else:
            print('Invalid entry!')
            exit()