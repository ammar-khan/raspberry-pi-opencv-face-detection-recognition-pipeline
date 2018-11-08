##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import datetime
import uuid
from src.common.package.config import application as config_app


##
# Handler class
# This class will handle file operations.
##
class Handler:

    def __init__(self):
        return None

    ##
    # Static method file_name()
    # Method to generate file name
    #
    # @return file name string
    ##
    @staticmethod
    def file_name():
        return str(uuid.uuid4()) + config_app.FILE_EXTENSION

    ##
    # Static method folder_name()
    # Method to generate folder name
    #
    # @param unique_id - unique id
    #
    # @return folder name string
    ##
    @staticmethod
    def folder_name(unique_id):
        name = '_'.join([config_app.UNKNOWN_PREFIX, str(unique_id), datetime.date.today().strftime('%d-%m-%Y')])
        return '/'.join([config_app.STORAGE_DIRECTORY, name]) + '/'


