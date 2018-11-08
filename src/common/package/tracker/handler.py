##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

from src.common.package.geometry.rectangle import Rectangle as rectangle
from src.common.package.tracker.object import Object as object
from src.common.package.config import default as config_default


##
# Handler class
# This class will handle tracker operations.
##
class Handler:

    def __init__(self):
        self._trackers = list()
        self._tracker_id = None

    # Getter
    @property
    def trackers(self):
        return self._trackers

    ##
    # Method add_tracker()
    # Method to add tracker
    ##
    def add_tracker(self, coordinates):
        if self._tracker_id is None:
            self._tracker_id = 1
        else:
            self._tracker_id += 1

        tracker_object = object(coordinates=coordinates, tracker_id=self._tracker_id)
        self.trackers.append(tracker_object)

        return self._tracker_id

    ##
    # Method remove_trackers()
    # Method to remove all inactive trackers
    ##
    def remove_trackers(self):
        for tracker in self.trackers:
            if not tracker.active:
                self.trackers.remove(tracker)

    ##
    # Method track()
    # Method to handle tracker
    #
    # @return tracker id
    ##
    def track(self, coordinates):

        track_id = None

        # If tracker is not set then
        # add new tracker and return its id
        if not self.trackers:
            track_id = self.add_tracker(coordinates=coordinates)
        # If tracker is set
        else:
            # Check if current tracker intersects with any previously stored tracker
            for idx, tracker in enumerate(self.trackers):
                (width, height), tracker.intersect = rectangle().intersects(coordinates, tracker.coordinates)

            # Calculate the distance of current tracker with all previous trackers
            for idx, tracker in enumerate(self.trackers):
                tracker.distance = rectangle().distance_between_centroids(coordinates, tracker.coordinates)

            # Get the closest previous tracker from current tracker
            (distance, idx) = min((tracker.distance, idx) for idx, tracker in enumerate(self.trackers)
                                  if tracker.distance is not None)

            # Check if tracker distance is within allowed distance, then
            # update closest tracker with current tracker and
            # mark it active and return its id
            if distance < config_default.MAX_TRACKER_DISTANCE:
                self.trackers[idx].active = True
                self.trackers[idx].coordinates = coordinates
                track_id = self.trackers[idx].id

            # If none of previous tracker matches then
            # add new tracker and returns its id
            if track_id is None:
                track_id = self.add_tracker(coordinates=coordinates)

        return track_id

    ##
    # Method reset_trackers()
    # Method to reset all trackers
    ##
    def reset_trackers(self):
        for idx, tracker in enumerate(self.trackers):
            tracker.active = False
            tracker.intersect = False
            tracker.distance = None
