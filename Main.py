# Blake Sutton  -- Student ID: 001109490 

from util import sort_packages
from read_csv import *
import sys
from distance import Distance

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

visited_locations = []
def next_location(current_location, truckload):
    """
    # Arbitrarily initializing the shortest_route variable so that it's longer than the longest possible route.
    # This has the effect of <any> route being shorter, even if there's only one left.
    shortest_route = 100.0
    next_package = None
    next_address = None 
    """
    unvisited = []
    for i in truckload:
        i.reset_path()
        unvisited.append(i)
    
    start_dist = 0

    while(len(unvisited) != 0):
        current_loc = pop.unvisited(0)

        for loc in unvisited:
            current_dist = current_loc.get_distance(loc.loc_id)

    
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