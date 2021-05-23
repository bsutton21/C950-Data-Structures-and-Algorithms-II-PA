import csv
import datetime

# Reads in the distances between each of the locations
with open('Distances.csv') as csvfile:
    distance_csv = csv.reader(csvfile, delimiter=',')
    distance_csv = list(distance_csv)

# Reads in the names of all of the possible delivery locations
with open('Packages.csv') as csvfile:
    packages_csv = csv.reader(csvfile, delimiter=',')
    packages_csv = list(packages_csv)

def check_distance(rowval, columnval, sum):
    distance = distance_csv[rowval][columnval]
    if distance is '':
        distance = distance_csv[rowval][columnval]
    
    sum += float(distance)
    return sum

