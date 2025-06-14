import math
from itertools import permutations, combinations

def calculate_distance(city1: tuple[int, int], city2: tuple[int, int]) -> float:
    """
    Calculate the Euclidean distance between two cities.
    """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(path: list[tuple[int, int]]) -> float:
    """
    Calculate the total distance of a path.
    """
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += calculate_distance(path[i], path[i + 1])
    return total_distance

def routes_to_cities(path: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Determine the order of cities in a path.
    """
    routes = {"permutation" : permutations(path), 
              "combination" : combinations(path, 2)}
    return routes
        
    