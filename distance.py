# Blake Sutton  -- Student ID: 001109490 

class Distance:

    def __init__(self, loc_id, parent_graph, name, addr, zip, distances): # O(n)
        self.loc_id = loc_id
        self.parent_graph = parent_graph
        self.name = name
        self.addr = addr
        self.zip = zip
        self.distances = []
        for distance in distances:
            if distance != '':
                self.distances.append(distance)
            else:
                break

    def get_distance(self, curr_id: int, dest_id):
        if curr_id == self.loc_id:
            return 0
        if curr_id < self.loc_id:
            return self.distances[curr_id]
        elif curr_id > self.loc_id:
            return self.parent_graph[curr_id].distances[self.loc_id]