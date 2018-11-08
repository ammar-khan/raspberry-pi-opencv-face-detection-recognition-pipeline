##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

# Application configuration
APPLICATION_NAME = ''
APPLICATION_VERSION = '1.0.1'

# HTTP Port for web streaming
HTTP_PORT = 8000
# HTTP page template path
HTML_TEMPLATE_PATH = './src/common/package/http/template'

# Capturing device index (used for web camera)
CAPTURING_DEVICE = 0
# To user Pi Camera
USE_PI_CAMERA = True

# Capture configuration
WIDTH = 640
HEIGHT = 480
RESOLUTION = [WIDTH, HEIGHT]
FRAME_RATE = 24

# Storage configuration
DATABASE_NAME = 'database.db'
STORAGE_DIRECTORY = './dataset/'
UNKNOWN_PREFIX = 'unknown'
FILE_EXTENSION = '.pgm'
