##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import os
import cv2
import fnmatch
from pathlib import Path


##
# Handler class
##
class Handler:

    def __init__(self):
        return None

    ##
    # Static method absolute_path()
    # Method to return absolute path
    #
    # @param path - virtual path
    #
    # @return string absolute path
    ##
    @staticmethod
    def absolute_path(path):
        return str(Path(path).resolve())

    ##
    # Static method dir_exist()
    # Method to check if directory exist
    #
    # @param path - virtual path
    #
    # @return boolean
    ##
    @staticmethod
    def dir_exist(path):
        return os.path.exists(str(Path(path)))

    ##
    # Static method file_exist()
    # Method to check if file exist
    #
    # @param path - virtual path
    #
    # @return boolean
    ##
    @staticmethod
    def file_exist(path):
        return os.path.isfile(str(Path(path)))

    ##
    # Class method files()
    # Generator Method to read file(s) from given directory as per matcher
    #
    # @param directory - storage directory
    # @param match - pattern
    #
    # @return generator(iterator)
    ##
    @classmethod
    def files(cls, directory, match='*'):
        for root, dirs, files in os.walk(cls.absolute_path(directory)):
            for file_name in fnmatch.filter(files, match):
                yield os.path.join(root, file_name).replace(' ', '\\ ')

    ##
    # Class method read_file()
    # Method to read file contents
    #
    # @param directory - storage directory
    # @param file_name - file name
    #
    # @return file contents
    ##
    @classmethod
    def read_file(cls, directory, file_name):
        file_path = os.path.join(cls.absolute_path(directory), file_name)

        with open(str(file_path), 'r') as _file:
            file_contents = _file.read().replace('\n', '')
            _file.close()

        return file_contents

    ##
    # Static method save_file()
    # Method to save image as a file
    #
    # @param image - image to store
    # @param filename - filename
    # @param directory - storage directory
    #
    # @return retval
    ##
    @classmethod
    def save_file(cls, image, filename, directory):
        filename = os.path.join(cls.absolute_path(directory), filename)
        return cv2.imwrite(filename, image)

    ##
    # Class method make_dir()
    # Method to create a folder
    #
    # @param image - image to store
    # @param filename - filename
    # @param directory - storage directory
    ##
    @classmethod
    def make_dir(cls, directory):
        if not cls.dir_exist(directory):
            os.makedirs(str(Path(directory)))
