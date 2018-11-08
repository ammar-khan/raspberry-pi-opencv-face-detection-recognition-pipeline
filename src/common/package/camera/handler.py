##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

from imutils.video import VideoStream
from src.common.package.config import default as config_default
from src.common.package.config import application as config_app


##
# Handler class
# This class will handle operations of camera.
# It supports USB web camera and Pi camera both
# If using Pi Camera then set USE_PI_CAMERA to True in config.application.py
##
class Handler:

    def __init__(self,
                 src=config_app.CAPTURING_DEVICE,
                 use_pi_camera=False,
                 resolution=config_default.RESOLUTION,
                 frame_rate=config_default.FRAME_RATE):

        self.capture = VideoStream(src=src,
                                   usePiCamera=use_pi_camera,
                                   resolution=resolution,
                                   framerate=frame_rate).start()

    def read(self):
        return self.capture.read()
