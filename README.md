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
### Camera

## TODO
### Eye
### Vision
* vision.py, Vision.get\_face: get the faces in the current image.
### Camera & Mount
* Camera and mount selection.
* Camera calibration.

## IDEAS
### Eye
### Vision
### Camera & Mount
* Looking for a programmable pan and tilt camera mount that is cheap and reliable.
  * [Lynxmotion Pan and Tilt Kit / Aluminium](https://www.robotshop.com/en/lynxmotion-pan-and-tilt-kit-aluminium2.html)
  * [DF05BB Tilt / Pan Kit](https://www.robotshop.com/en/df05bb-tilt-pan-kit.html)
  * [JSumo Robopan Micro Pan/Tilt](https://www.robotshop.com/en/jsumo-robopan-micro-pan-tilt.html)
  * [Pan / Tilt bracket Kit (Single Attachment)](https://www.robotshop.com/en/pan-tilt-bracket-kit-single-attachment.html)
  * [CMOS Camera for FPV w/ Pan / Tilt - 720x480 pixels](https://www.robotshop.com/en/cmos-camera-fpv-pan-tilt-720x480-pixels.html)
