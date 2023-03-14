import random
import math

'''

        The Unit circle inscribed within the square
        Points are randomly placed within the square
        pi is approximately equal to 4 times the ratio of points in the circle and points outside the circle

       1 
        +---------------+
        |   _________   |
        |  /      1  \  |
        |  |    +____|  |
        |  |         |  |
        |  \_________/  |
        +---------------+
       -1                1
'''

def monte_pi(points: int) -> float:
    ''' Approximates Pi by randomly placing points in a unit square with a circle of radius 1 inscribed within it
        and taking the ratio of points which lie inside the circle and those which do not  
    '''
    in_circle = 0

    for _ in range(points):
        # Randomly sample a point within the square
        point_x, point_y = random.uniform(-1, 1), random.uniform(-1, 1)
        # get the distance from the point to the origin
        dist = math.sqrt((point_x * point_x) + (point_y * point_y))
        # check if the point lies within the unit circle (radius of 1)
        in_circle += (dist < 1)

    # multiply by 4 because the raio of the area of the circle and the area of the square is 𝝅/4
    pi = 4 * (in_circle / points)

    return pi

