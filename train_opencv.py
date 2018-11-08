##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import numpy as np
from PIL import Image
import os
from src.common.package.config import application as config_app
from src.opencv.package.config import application as config_opencv
from src.common.package.io.handler import Handler as io_handler
from src.common.package.progress.handler import progress as progress_bar
from src.common.package.database.handler import Handler as Database

# Constant
database = Database()


##
# Training class
##
class Training:
    def __init__(self):
        # Create database connection
        database.create_connection()
        print('[INFO] Connected with database successfully...')

        # Create table
        database.create_table()
        print('[INFO] Database table created successfully...')

        # Grab the paths to the input images in data set
        print('[INFO] Quantifying dataset...')
        self.image_paths = list(io_handler.files(directory=config_app.STORAGE_DIRECTORY,
                                                 match='*' + config_app.FILE_EXTENSION))

        # Initialise list
        self.detections = []
        self.labels = []
        self.descriptions = []

        # Initialise face recogniser
        self.recognizer = config_opencv.FACE_RECOGNIZERS[config_opencv.DEFAULT_FACE_RECOGNIZER]()

        return None

    ##
    # Static method get_description()
    # Method to extract description from directory name
    #
    # @param path - path
    #
    # @return string description
    ##
    @staticmethod
    def get_description(path):
        return path.split(os.path.sep)[-2].replace('_', ' ').title()

    ##
    # Static method get_id()
    # Method to get id from database table
    #
    # @param description - description
    #
    # @return string id
    ##
    @staticmethod
    def get_id(description):
        # Search id in database table
        database_cursor = database.execute_query(sql_query='SELECT id FROM detections WHERE desc = ?;',
                                                 parameters=(description,))
        result = database_cursor.fetchone()

        # If description does not exist in table then create new id else return existing id
        if result is None:
            # Add new record
            database_cursor = database.execute_query(sql_query='INSERT INTO detections (desc) VALUES (?);',
                                                     parameters=(description,))
            # Return recently added row id
            return database_cursor.lastrowid
        else:
            # Return existing id
            return result[0]

    ##
    # Method pre_processing()
    # Method to prepared data to train model
    #
    # @return detection labels, detections
    ##
    def pre_processing(self):
        print('[INFO] Processing {} images...'.format(len(self.image_paths)))
        for (idx, image_path) in enumerate(self.image_paths):
            try:
                # Progress bar
                progress_bar(idx + 1, len(self.image_paths), status='Completed')

                # Get description and description id
                description = self.get_description(path=image_path)
                description_id = self.get_id(description)

                # Convert image to gray scale and to numpy array
                image = Image.open(image_path).convert('L')
                image = np.array(image, 'uint8')

                # Insert images and description id to list
                self.detections.append(image)
                self.labels.append(description_id)

            except Exception as e:
                print('[ERROR] Exception %s' % str(e))
                continue

        # Need to print carriage return because of progress bar
        print('\r')
        return np.array(self.labels), self.detections

    ##
    # Method train()
    # Method to train model
    ##
    def train(self):
        # Make directory to store model
        io_handler.make_dir(directory=config_opencv.TRAINED_MODEL_DIRECTORY)

        # Pre-process dataset to make it ready to train model
        idx, detections = self.pre_processing()

        # Train model
        print('[INFO] Training model...')
        self.recognizer.train(detections, idx)

        # Save trained model
        trained_model = config_opencv.TRAINED_MODEL_DIRECTORY + config_opencv.TRAINED_MODEL_FILE
        print('[INFO] Trained model saved to: ', trained_model)
        self.recognizer.save(trained_model)


##
# Method main()
##
def main():
    try:
        print('[INFO] Initialising OpenCV training...')
        training = Training()
        training.train()

    except Exception as e:
        print('[ERROR] Exception: %s' % str(e))
        database.close_connection()


if __name__ == '__main__':
    main()
