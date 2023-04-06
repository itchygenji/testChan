#chanConvexFinalFinal.py
import sys
import math
from functools import cmp_to_key

# Define the Point class
class Point:
    # Initialize the Point object with x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define how the Point object should be represented as a string
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
        
    def __hash__(self):
        return hash((self.x, self.y))

# Define the PointList class for managing a list of points
class PointList:
    # Initialize the PointList object with an optional list of points
    def __init__(self, points=None):
        self.points = points or []

    # Add a point to the PointList object
    def add_point(self, x, y):
        self.points.append(Point(x, y))

    # Remove a point from the PointList object by its index
    def remove_point(self, index):
        self.points.pop(index)

    # Define how the PointList object should be represented as a string
    def __repr__(self):
        return str(self.points)

# Define the cross product function for three points
def cross_product(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

# Define a comparison function for two points
"""
def compare(p1, p2):
    if p1.x != p2.x:
        #return p1.x - p2.x
    return p1.y - p2.y
"""

def polar_angle(p1, p2):
    return math.atan2(p2.y - p1.y, p2.x - p1.x)

"""
def compare(p1, p2):
    angle1 = polar_angle(pivot, p1)
    angle2 = polar_angle(pivot, p2)
    if angle1 < angle2:
        return -1
    if angle1 > angle2:
        return 1
    return 0

"""

def compare(p1, p2):
    angle1 = polar_angle(pivot, p1)
    angle2 = polar_angle(pivot, p2)
    if angle1 < angle2:
        return -1
    if angle1 > angle2:
        return 1
    d1 = math.sqrt((p1.x - pivot.x) ** 2 + (p1.y - pivot.y) ** 2)
    d2 = math.sqrt((p2.x - pivot.x) ** 2 + (p2.y - pivot.y) ** 2)
    return int(d1 - d2)
# Define the Graham's scan algorithm
"""
def graham_scan(points):
    # Sort the points by their x and y coordinates
    points = sorted(points, key=cmp_to_key(compare))
    # Initialize an empty list for the convex hull
    hull = []
    # Iterate through the sorted points
    for p in points:
        # Remove points from the hull while the last three points form a non-left turn
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        # Add the current point to the hull
        hull.append(p)
    return hull
"""

def graham_scan(points):
    global pivot
    pivot = min(points, key=lambda p: (p.y, p.x))
    points = sorted(points, key=cmp_to_key(compare))
    
    hull = []
    for p in points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull



# Define the Jarvis march algorithm
def jarvis_march(points):
    # Initialize an empty list for the convex hull
    hull = []
    # Find the leftmost point among the points
    left_most = min(points, key=lambda p: p.x)
    # Set the current point as the leftmost point
    p = left_most
    # Continue until the algorithm reaches the starting point again
    while True:
        # Add the current point to the hull
        hull.append(p)
        # Set the next point as the point following the current point
        q = points[(points.index(p) + 1) % len(points)]
        # Iterate through the points to find the next point on the hull
        for r in points:
            if cross_product(p, r, q) > 0:
                q = r
        # Update the current point
        p = q
        # Break the loop if the current point is the starting point
        if p == left_most:
            break
    return hull

# Define Chan's algorithm
def chans_algorithm(point_list):
    # Retrieve the list of points from the point_list object
    points = point_list.points
    # Initialize the value of m, which determines the number of subsets
    m = 1
    # Sort the points by their x and y coordinates
    points = sorted(points, key=lambda p: (p.x, p.y))
    # Calculate the number of points
    n = len(points)
    # Initialize an empty list for the convex hull
    hull = []

    # Continue the loop until the convex hull is found
    while True:
        # Create subsets of points with size m
        subsets = [points[i:i+m] for i in range(0, n, m)]
        # Reset the hull for each iteration
        hull = []
        # Iterate through the subsets
        for subset in subsets:
            # If the size of the subset is less than or equal to m // 2, use Jarvis march
            if len(subset) <= m // 2:
                hull.extend(jarvis_march(subset))
            # Otherwise, use Graham's scan
            else:
                hull.extend(graham_scan(subset))

        # Use Jarvis march to combine the hulls from the subsets
        hull = jarvis_march(hull)
        # If the size of the hull doesn't change after another Jarvis march, the convex hull is found
        if len(hull) == len(jarvis_march(hull)):
            break
        # If the convex hull is not found, double the value of m and try again
        m *= 2

    # Return the final convex hull
    return hull

# Create a list of points
point_list = PointList([
    Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
    Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)
])

# Create another list of points
point_list2 = PointList([Point(0, 3), Point(1, 1), Point(2, 2), Point(2, 1),
    Point(3, 0), Point(0, 0), Point(3, 3)])

# Calculate the initial convex hull for point_list
convex_hull = chans_algorithm(point_list)
print(convex_hull)  # Output: [(0, 0), (0, 3), (3, 1), (4, 4)]

# Print the points in point_list
print(point_list.points)

# Remove a point and recalculate the hull for point_list
point_list.remove_point(2)

# Print the updated points in point_list
print(point_list.points)
convex_hull = chans_algorithm(point_list)
print(convex_hull)  # Output will depend on the updated point list

# Calculate the convex hull for point_list2
convex_hull = chans_algorithm(point_list2)
print(convex_hull)  # Output: [(0, 0), (3, 0), (3, 3), (0, 3)]