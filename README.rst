==================================================================
OpenCV Face Detection and Recognition Pipeline
==================================================================

Prerequisite(s):
----------------

- python 3.5>
- pip
- numpy
- opencv
- opencv contribute
- imutils
- sqlite3
- scipy
- PIL

.. _Prerequisites Installation Guide: https://github.com/ammar-khan/raspberry-pi-3-model-b-plus

`Prerequisites Installation Guide`_

Introduction:
-------------
This is an example of OpenCV face detection and recognition pipeline on Raspberry Pi 3 Model B+.

Configuration:
--------------
Refer to:

``src/common/package/config``

``src/opencv/package/config``


Structure of dataset:
---------------------

.. list-table::
 :header-rows: 1

 * - Storage Directory (do not change)
   - Description Directory (david_john)
   - Images

 * - dataset
   -
   -
 * -
   - detection_1
   -
 * -
   -
   - filename.pgm
 * -
   - detection_2
   -
 * -
   -
   - filename1.pgm
 * -
   -
   - filename2.pgm
 * -
   -
   - filename3.pgm

To Train:
---------
>>> python3.5 train_opencv.py

To Recognise/Steaming:
----------------------
>>> python3.5 main_opencv.py

Streaming:
----------
Open ``http://localhost:8000`` in browser

Copyright & License
-------------------

- Copyright (c) 2018, Ammar Ali Khan
- License: MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
