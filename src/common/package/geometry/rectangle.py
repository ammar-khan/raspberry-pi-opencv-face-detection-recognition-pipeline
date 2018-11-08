##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

from scipy.spatial import distance


##
# Rectangle class
##
class Rectangle:

    def __init__(self):
        return None

    ##
    # Static method centroid()
    # Method to return centroid of given rectangle
    #
    # @param coordinates - rectangle coordinates
    #
    # @return (centroid)
    ##
    @staticmethod
    def centroid(coordinates):
        coord_x = (coordinates['left'] + coordinates['right']) / 2
        coord_y = (coordinates['top'] + coordinates['bottom']) / 2

        return coord_x, coord_y

    ##
    # Static method intersect_dimensions()
    # Method to return intersects dimensions of given rectangle
    #
    # @param coordinates_1 - rectangle 1 coordinates
    # @param coordinates_2 - rectangle 2 coordinates
    #
    # @return intersection (width, height) dimensions or (None, None)
    ##
    @staticmethod
    def intersect_dimensions(coordinates_1, coordinates_2):
        #
        # width = min(r1.xmax, r2.xmax) - max(r1.xmin, r2.xmin)
        # height = min(r1.ymax, r2.ymax) - max(1.ymin, r2.ymin)
        # area = width * height
        #
        # Note: xmin = left, ymin = top, xmax = right, ymax = bottom
        #
        width = min(coordinates_1['right'], coordinates_2['right']) - max(coordinates_1['left'], coordinates_2['left'])
        height = min(coordinates_1['bottom'], coordinates_2['bottom']) - max(coordinates_1['top'], coordinates_2['top'])
        if (width >= 0) and (height >= 0):
            return width, height
        else:
            return None, None

    ##
    # Class method intersects()
    # Method to check if two rectangles intersects
    #
    # @param coordinates_1 - rectangle 1 coordinates
    # @param coordinates_2 - rectangle 2 coordinates
    #
    # @return (intersection dimensions, boolean)
    ##
    @classmethod
    def intersects(cls, coordinates_1, coordinates_2):
        width, height = cls.intersect_dimensions(coordinates_1, coordinates_2)
        return (width, height), True if (width, height) else False

    ##
    # Class method distance_between_centroids()
    # Method to return distance between centroids
    #
    # @param coordinates_1 - rectangle 1 coordinates
    # @param coordinates_2 - rectangle 2 coordinates
    #
    # @return distance
    ##
    @classmethod
    def distance_between_centroids(cls, coordinates_1, coordinates_2):
        return distance.euclidean(cls.centroid(coordinates_1), cls.centroid(coordinates_2))
