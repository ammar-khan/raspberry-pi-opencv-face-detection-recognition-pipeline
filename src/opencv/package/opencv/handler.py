##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import cv2
from src.opencv.package.config import application as config_opencv
from src.common.package.io.handler import Handler as io_handler


##
# Handler class
# This class is a wrapper for Open Source Computer Vision (OpenCV)
#
# @see: https://opencv.org/
##
class Handler:

    def __init__(self):
        print('[INFO] OpenCV - Initialising...')

        # Haarcascades
        haarcascade_frontalface_default_path = \
            io_handler.absolute_path(config_opencv.HAARCASCADE_FRONTALFACE_DEFAULT_PATH)


        # Caffe models
        self.model_face = config_opencv.CAFFE_MODELS['face_net']
        self.model_age = config_opencv.CAFFE_MODELS['age_net']
        self.model_gender = config_opencv.CAFFE_MODELS['gender_net']

        self._haarcascade_frontalface_default = cv2.CascadeClassifier(haarcascade_frontalface_default_path)

        self._face_net = cv2.dnn.readNetFromCaffe(io_handler.absolute_path(self.model_face[0]),
                                                  io_handler.absolute_path(self.model_face[1]))

        self._age_net = cv2.dnn.readNetFromCaffe(io_handler.absolute_path(self.model_age[0]),
                                                 io_handler.absolute_path(self.model_age[1]))

        self._gender_net = cv2.dnn.readNetFromCaffe(io_handler.absolute_path(self.model_gender[0]),
                                                    io_handler.absolute_path(self.model_gender[1]))

        # Multi trackers
        self.multi_tracker = cv2.MultiTracker_create()

    ##
    # Method haarcascade_frontalface_default_detector()
    # Method to return OpenCV haarcascade_frontalface_default_detector
    #
    # @param frame - image frame
    # @param scale_factor - reduce image
    # @param min_neighbours - min neighbours for detections
    # @param min_size - min size of object to detect
    #
    # @return Array of detection(s)
    ##
    def haarcascade_frontalface_default_detector(self,
                                                 frame,
                                                 scale_factor=1.1,
                                                 min_neighbours=5,
                                                 min_size=(30, 30)):

        return self._haarcascade_frontalface_default.detectMultiScale(image=frame,
                                                                      scaleFactor=scale_factor,
                                                                      minNeighbors=min_neighbours,
                                                                      minSize=min_size)

    ##
    # Method dnn_face_detector()
    # Method to return OpenCV dnn_face_detector
    #
    # @param frame - image frame
    # @param scale_factor - reduce image
    # @param swap_rb - swap channel
    #
    # @return Array of detection(s)
    ##
    def dnn_face_detector(self,
                          frame,
                          scale_factor=1.0,
                          swap_rb=True):

        size = self.model_face[2]
        mean = self.model_face[3]

        # Convert frame to a blob
        blob = cv2.dnn.blobFromImage(image=cv2.resize(frame, size),
                                     scalefactor=scale_factor,
                                     size=size,
                                     mean=mean)

        # Pass the blob through the network and obtain the detections and predictions
        self._face_net.setInput(blob)
        return self._face_net.forward()

    ##
    # Method dnn_age_detector()
    # Method to return OpenCV dnn_age_detector
    #
    # @param frame - image frame
    # @param scale_factor - reduce image
    # @param swap_rb - swap channel
    #
    # @return prediction
    ##
    def dnn_age_detector(self,
                         frame,
                         scale_factor=1.0,
                         swap_rb=True):

        size = self.model_age[2]
        mean = self.model_age[3]
        age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']

        # Convert frame to a blob
        blob = cv2.dnn.blobFromImage(image=cv2.resize(frame, size),
                                     scalefactor=scale_factor,
                                     size=size,
                                     mean=mean)

        # Pass the blob through the network and obtain the detections and predictions
        self._age_net.setInput(blob)
        predictions = self._age_net.forward()

        return age_list[predictions[0].argmax()]

    ##
    # Method dnn_gender_detector()
    # Method to return OpenCV dnn_gender_detector
    #
    # @param frame - image frame
    # @param scale_factor - reduce image
    # @param swap_rb - swap channel
    #
    # @return prediction
    ##
    def dnn_gender_detector(self,
                            frame,
                            scale_factor=1.0,
                            swap_rb=True):

        size = self.model_gender[2]
        mean = self.model_gender[3]
        gender_list = ['Male', 'Female']

        # Convert frame to a blob
        blob = cv2.dnn.blobFromImage(image=cv2.resize(frame, size),
                                     scalefactor=scale_factor,
                                     size=size,
                                     mean=mean)

        # Pass the blob through the network and obtain the detections and predictions
        self._gender_net.setInput(blob)
        predictions = self._gender_net.forward()

        return gender_list[predictions[0].argmax()]

    ##
    # Method start_tracker()
    # Method to start object tracking
    #
    # @param frame - image frame
    # @param coordinates - coordinates to track
    #
    # @return trackers
    ##
    def start_tracker(self, frame, coordinates):
        # Create a new object tracker for the coordinates
        tracker = config_opencv.OBJECT_TRACKERS[config_opencv.DEFAULT_TRACKER]()
        self.multi_tracker.add(tracker, frame, coordinates)

        return self.multi_tracker

    ##
    # Method update_tracker()
    # Method to update object tracking
    #
    # @param trackers - trackers
    # @param frame - image frame
    #
    # @return object - (success, coordinates)
    ##
    @staticmethod
    def update_tracker(multi_tracker, frame):
        return multi_tracker.update(frame)
