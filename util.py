# I manually sorted the packages on the trucks since for a shipping company of this size,
# it's reasonable to think that management cound still do this manually

# Rules followed while sorting:
# Truck 1: Earliest times, co-delivery requirements, ZIP code proximity
# Truck 2: Packages delayed until 9:05 with deadline by 10:30, some packages required to be on truck 2, ZIP code proximity
# Truck 3: Remaining packages

def sort_packages():
    truck1 = [1,4,12,13,14,15,16,19,20,21,24,34,39,40]
    truck2 = [3,5,6,7,18,22,25,26,28,29,31,32,36,37,38]
    truck3 = [2,8,9,10,11,17,23,27,30,33,35]
    return truck1, truck2, truck3

