##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import cv2
import dlib
from src.common.package.config import default as config_default
from src.dlib.package.config import application as config_dlib
from src.common.package.io.handler import Handler as io_handler
from src.common.package.frame.handler import Handler as frame_handler
from imutils.face_utils import FaceAligner as face_aligner


##
# Handler class
##
class Handler:

    def __init__(self):
        predictor = dlib.shape_predictor(io_handler.absolute_path(config_dlib.PREDICTOR_PATH))
        self.face_aligner = face_aligner(predictor, desiredFaceWidth=config_default.THUMBNAIL_WIDTH)

        return None

    ##
    # Method align()
    # Method to align face
    #
    # @param frame - image frame
    # @param coordinates - detection coordinates
    #
    # @return aligned face
    ##
    def align(self, frame, coordinates):
        frame = frame_handler.scale(frame=frame, scale=0.5)
        detection = dlib.rectangle(int(coordinates['left'] / 2),
                                   int(coordinates['top'] / 2),
                                   int(coordinates['right'] / 2),
                                   int(coordinates['bottom'] / 2))

        aligned_image = self.face_aligner.align(image=frame,
                                                gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY),
                                                rect=detection)

        return frame_handler.scale(frame=aligned_image, scale=2)
