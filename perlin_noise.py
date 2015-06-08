import math
import random
from math import pi


# returns the unit vector of angle
def unitVector(angle):
    return (math.cos(angle), math.sin(angle))


# needs to be extended for any size vector
def dotProduct(point1, point2):
    return point1[0] * point2[0] + point1[1] * point2[1]


# interp uses a cubic function to perform a weighted average of a0 and a1
def interp(a0,  a1,  w):
    weight = 3*math.pow(w, 2) - 2*math.pow(w, 3)
    return a0*(1-weight) + a1*weight


# angles provides the four gradient angles for the grid in a tuple
# starting from top left then going clockwise
# coords provides the (x, y) coordinates on the grid,  assuming top left is (0, 0)
def perlinNoise(coords, gridSize, angles):
    topLeftGradient = unitVector(angles[0])
    topRightGradient = unitVector(angles[1])
    bottomRightGradient = unitVector(angles[2])
    bottomLeftGradient = unitVector(angles[3])
    coords = (((coords[0] + 1) * 1000) % gridSize,
              ((coords[1] + 1) * 1000) % gridSize)
    topLeftVector = coords
    topRightVector = (gridSize - coords[0], coords[1])
    bottomRightVector = (gridSize - coords[0],  gridSize - coords[1])
    bottomLeftVector = (coords[0], gridSize - coords[1])
    topLeft = dotProduct(topLeftGradient, topLeftVector)
    topRight = dotProduct(topRightGradient, topRightVector)
    bottomRight = dotProduct(bottomRightGradient, bottomRightVector)
    bottomLeft = dotProduct(bottomLeftGradient, bottomLeftVector)
    topAverage = interp(topLeft, topRight, coords[0]/gridSize)
    bottomAverage = interp(bottomLeft, bottomRight, coords[0]/gridSize)
    average = interp(topAverage, bottomAverage, coords[1]/gridSize)
    return average/gridSize


if __name__ == "__main__":
    print(perlinNoise((.002, .235), 350, (random.uniform(0, 2*pi),
          random.uniform(0, 2*pi), random.uniform(0, 2*pi),
          random.uniform(0, 2*pi))))
