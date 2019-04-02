# Foveal Vision System
> Combining computer vision & machine learning to create an artifical intelligence system that replicates human vision.
## FINISHED
* eye.py, Eye.__init__: initialize a new eye.
* eye.py, Eye.capture: capture video stream.
* eye.py, Eye.setup\_vision: setup vision types that will be used.
  * Eye.vision["Mainfoveal"]: high resolution low coverage.
  * Eye.vision["Parafoveal"]: mid resolution mid coverage.
  * Eye.vision["Peripheral"]: low resolution high coverage.
* eye.py, Eye.update\_curr: update the current image (frame).
* eye.py, Eye.update\_prev: update the current image (frame).
* eye.py, Eye.check\_stop: check to see if a stop signal was sent.
* eye.py, Eye.start: start recording.
* eye.py, Eye.stop: end recording.
* eye.py, Eye.crop\_image: crop image to a square.
* eye.py, setup: setup a new eye using a camera id.

## TODO
* Camera and mount selection.
* Camera calibration.
