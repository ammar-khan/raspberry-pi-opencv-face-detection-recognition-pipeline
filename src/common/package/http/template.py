##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

from src.common.package.config import application as config_app
from src.common.package.io.handler import Handler as io


##
# Template class
# This class provides utility methods for template
##
class Template(object):

    def __init__(self):
        return None

    ##
    # Static method load()
    # Method to load template
    #
    # @param file_name - template file name with extension
    #
    # @return template contents
    ##
    @staticmethod
    def load(file_name):
        return io.read_file(directory=config_app.HTML_TEMPLATE_PATH, file_name=file_name)
