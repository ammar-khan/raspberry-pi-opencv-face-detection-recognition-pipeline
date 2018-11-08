##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
from src.common.package.config import default as config_default
from src.common.package.geometry.rectangle import Rectangle as rectangle

# Constant
FONT = ImageFont.truetype(config_default.FONT_NAME, config_default.FONT_SIZE)


##
# Handler class
##
class Handler:

    def __init__(self):
        return None

    ##
    # Static method scale()
    # Method to scale image using aspect ratio
    #
    # @param frame - image frame
    # @param scale - aspect ratio
    #
    # @return frame
    ##
    @staticmethod
    def scale(frame, scale):
        return cv2.resize(frame, (0, 0), fx=scale, fy=scale)

    ##
    # Static method image_to_array()
    # Method to convert image into numpy array (frame)
    #
    # @param image - image
    #
    # @return frame
    ##
    @staticmethod
    def image_to_array(image):
        return np.array(image)

    ##
    # Static method crop()
    # Method to crop image
    #
    # @param image - numpy image array (frame)
    # @param coordinates - coordinates to crop image
    #
    # @return cropped and re-sized frame
    ##
    @staticmethod
    def crop(image, coordinates):
        centroid_x, centroid_y = rectangle.centroid(coordinates)
        left = centroid_x - config_default.THUMBNAIL_WIDTH
        top = centroid_y - config_default.THUMBNAIL_HEIGHT
        right = centroid_x + config_default.THUMBNAIL_WIDTH
        bottom = centroid_y + config_default.THUMBNAIL_HEIGHT

        cropped_image = image[int(top):int(bottom), int(left):int(right)]

        return cropped_image

    ##
    # Static method text()
    # Method to write text on frame
    #
    # @param frame - image frame
    # @param coordinates - left and top coordinates
    # @param text - text to write
    # @param font_color - font colour
    # @param font - font
    #
    # @return frame
    ##
    @staticmethod
    def text(frame,
             coordinates,
             text,
             font_color=config_default.FONT_COLOR,
             font=FONT):

        # Convert frame into image and make it ready to draw
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        # Draw
        draw.text((coordinates['left'], coordinates['top']),
                  text,
                  font=font,
                  fill=font_color)

        # Clear
        del draw

        # Convert image to numpy array (frame) and return
        return Handler.image_to_array(image)

    ##
    # Static method rectangle()
    # Method to write text on frame
    #
    # @param frame - image frame
    # @param coordinates - left, top, right, bottom coordinates
    # @param text - text to write
    # @param text_solid_background - boolean value to make solid text box (default False)
    # @param solid_background - boolean value to make solid box (default False)
    # @param box_color - box colour
    # @param font_color - font colour
    # @param font - font
    #
    # @return frame
    ##
    @staticmethod
    def rectangle(frame,
                  coordinates,
                  text='',
                  text_solid_background=False,
                  solid_background=False,
                  box_color=config_default.BACKGROUND_COLOR,
                  font_color=config_default.FONT_COLOR,
                  font=FONT):

        # Convert frame into image and make it ready to draw
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        if solid_background:
            # Draw solid_background
            draw.rectangle(((coordinates['left'], coordinates['top']),
                            (coordinates['right'], coordinates['bottom'])),
                           fill=box_color,
                           outline=box_color)
        else:
            # Draw hollow
            draw.rectangle(((coordinates['left'], coordinates['top']),
                            (coordinates['right'], coordinates['bottom'])),
                           outline=box_color)

        if text:
            text_width, text_height = draw.textsize(text)
            text_x = coordinates['left'] + 5
            text_y = coordinates['bottom'] + 5

            if text_solid_background:
                # Draw solid box
                draw.rectangle(((coordinates['left'], coordinates['bottom']),
                                (coordinates['right'], coordinates['bottom'] + text_height + 10)),
                               fill=box_color,
                               outline=box_color)
            else:
                font_color = config_default.BACKGROUND_COLOR

            # Draw center aligned text
            draw.text((text_x, text_y),
                      text,
                      font=font,
                      fill=font_color)

        # Clear
        del draw

        # Convert image to numpy array (frame) and return
        return Handler.image_to_array(image)

    ##
    # Static method circle()
    # Method to draw circle on frame
    #
    # @param frame - image frame
    # @param coordinates - left and top coordinates
    # @param radius - radius
    # @param color - background color
    #
    # @return frame
    ##
    @staticmethod
    def circle(frame,
               coordinates,
               radius,
               color=config_default.BACKGROUND_COLOR):

        # Convert frame into image and make it ready to draw
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        # Draw
        draw.ellipse((coordinates['left'] - radius, coordinates['top'] - radius,
                      coordinates['left'] + radius, coordinates['top'] + radius),
                     fill=color)
        # Clear
        del draw

        # Convert image to numpy array (frame) and return
        return Handler.image_to_array(image)

    ##
    # Static method normalize()
    # Normalizes a given array in X to a value between low and high.
    # Adapted from python OpenCV face recognition example at:
    # https://github.com/Itseez/opencv/blob/2.4/samples/python2/facerec_demo.py
    #
    # @param array_x - array to normalise
    # @param low - low value
    # @param high - high value
    # @param dtype - type
    #
    # @return normalised frame
    ##
    @staticmethod
    def normalize(array_x, low, high, dtype=None):
        array_x = np.asarray(array_x)
        min_x, max_x = np.min(array_x), np.max(array_x)

        # Normalize to [0...1].
        array_x = array_x - float(min_x)
        array_x = array_x / float((max_x - min_x))

        # Scale to [low...high].
        array_x = array_x * (high - low)
        array_x = array_x + low

        if dtype is None:
            return np.asarray(array_x)

        return np.asarray(array_x, dtype=dtype)
