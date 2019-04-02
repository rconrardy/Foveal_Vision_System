# Foveal Vision System
> Combining computer vision & machine learning to create an artifical intelligence system that replicates human vision.
## FINISHED
### Eye
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
### Vision
* vision.py, Vision.__init__: Initialize a new vision.
* vision.py, Vision.update\_curr: update the current image (frame).
* vision.py, Vision.update\_prev: update the previous image (frame).
* vision.py, Vision.get\_diff: get the difference between the current and previous image.
* vision.py, Vision.get\_edge: get the edges in the current image.
* vision.py, Vision.crop\_image: crop image to desired size.
* vision.py, setup: setup a new vision with a ratio and pixel count.

## TODO
### Eye
### Vision
* vision.py, Vision.get\_face: get the faces in the current image.
### Camera
* Camera and mount selection.
* Camera calibration.
