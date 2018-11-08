##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##
import cv2

# OpenCV configuration

# Haar cascade
HAARCASCADE_FRONTALFACE_DEFAULT_PATH = './src/opencv/cascade/haarcascade_frontalface_default.xml'
HAARCASCADE_EYE_DEFAULT_PATH = './src/opencv/cascade/haarcascade_eye.xml'

# Caffe models configurations
CAFFE_MODELS = {
    # face_net.caffemodel is actually res10_300x300_ssd_iter_140000.caffemodel
    'face_net': ['./src/opencv/dnn/prototxt/deploy_face.prototxt.txt',
                 './src/opencv/dnn/model/face_net.caffemodel',
                 (300, 300),
                 (104.0, 177.0, 123.0)],
    'age_net': ['./src/opencv/dnn/prototxt/deploy_age.prototxt.txt',
                './src/opencv/dnn/model/age_net.caffemodel',
                (227, 227),
                (78.4263377603, 87.7689143744, 114.895847746)],
    'gender_net': ['./src/opencv/dnn/prototxt/deploy_gender.prototxt.txt',
                   './src/opencv/dnn/model/gender_net.caffemodel',
                   (227, 227),
                   (78.4263377603, 87.7689143744, 114.895847746)]

}
# Default Caffe models confidence
CONFIDENCE = 0.3

# Object tracker configuration
OBJECT_TRACKERS = {
    'csrt': cv2.TrackerCSRT_create,
    'kcf': cv2.TrackerKCF_create,
    'boosting': cv2.TrackerBoosting_create,
    'mil': cv2.TrackerMIL_create,
    'tld': cv2.TrackerTLD_create,
    'medianflow': cv2.TrackerMedianFlow_create,
    'mosse': cv2.TrackerMOSSE_create
}
DEFAULT_TRACKER = 'kcf'

# Face recognizer configuration
FACE_RECOGNIZERS = {
    'eigen': cv2.face.EigenFaceRecognizer_create,
    'fisher': cv2.face.FisherFaceRecognizer_create,
    'lbph': cv2.face.LBPHFaceRecognizer_create
}
DEFAULT_FACE_RECOGNIZER = 'lbph'

# Trained model configuration
TRAINED_MODEL_DIRECTORY = './trained_model/'
TRAINED_MODEL_FILE = 'model.yml'

