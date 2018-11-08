##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##


##
# Object class
# This class will handle tracker object.
##
class Object:

    def __init__(self, coordinates, tracker_id=0):
        self._coordinates = coordinates
        self._id = tracker_id
        self._active = True
        self._intersect = False
        self._distance = None

    # Getter
    @property
    def coordinates(self):
        return self._coordinates

    # Setter
    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    # Getter
    @property
    def id(self):
        return self._id

    # Setter
    @id.setter
    def id(self, value):
        self._id = value

    # Getter
    @property
    def active(self):
        return self._active

    # Setter
    @active.setter
    def active(self, value):
        self._active = value

    # Getter
    @property
    def intersect(self):
        return self._intersect

    # Setter
    @intersect.setter
    def intersect(self, value):
        self._intersect = value

    # Getter
    @property
    def distance(self):
        return self._distance

    # Setter
    @distance.setter
    def distance(self, value):
        self._distance = value
