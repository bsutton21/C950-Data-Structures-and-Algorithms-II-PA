# Blake Sutton  -- Student ID: 001109490 

from read_csv import *

"""
class Location:
    # Complexity: O(n)
    def __init__(self, loc_id, parent_graph, name, address, zip, distances):
        self.loc_id = loc_id
        self.parent_graph = parent_graph
        self.name = name
        self.address = address
        self.zip = zip
        self.distances = distances
        for distance in distances:
            if distance != '':
                self.distances.append(distance)
            else:
                break
"""

package_table = read_packages
distance_table = read_distances

def next_location(current_location, truckload):
    # Arbitrarily initializing the shortest_route variable so that it's longer than the longest possible route.
    # This has the effect of <any> route being shorter, even if there's only one left.
    shortest_route = 100.0
    next_package = None
    next_address = None

    for pack_num in truckload:

        package = package_table.get_item
        