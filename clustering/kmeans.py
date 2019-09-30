from collections import defaultdict
from math import inf, sqrt
import random
import csv

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    new_center[]
    dimension = len(points[0])
    points_num = len(points)
    for d in range(dimension)
        sum = 0
        for n in range(point_num)
            sum += points[n][d]
        new_center.append(sum / float(points_num))
    return new_center
    # raise NotImplementedError()


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    new_centers = []
    assignment_dict = defaultdict(list)
    for assignment, point in zip(assignments, data_set):
        assignment_dict[assignment].append(point)
        
    for c in assignment_dict:
        new_centers.append(point_avg(assignment_dict[c]))

    return new_centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    dist = 0
    for i in range(len(a)):
        dist += (a[i] - b[i]) ** 2
    return sqrt(dist)
    # raise NotImplementedError()


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set

    the generated center is not necessarily one of the
    instance from data_set, but within the extent of the data_set 
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for dot in data_set:
        for i in range(dimensions):
            val = dot[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for c in range(k):
        center = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]
            center.append(uniform(min_val, max_val))
        centers.append(center)
        
    return centers
    # raise NotImplementedError()


def get_list_from_dataset_file(dataset_file):
    dataset = []
    with open(dataset_file) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            point = []
            dimension = len(row)
            for d in range(dimension):
                point.append(int(row[d]))
            dataset.append(point)
    return dataset



def cost_function(clustering):
    raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering



