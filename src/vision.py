import cv2
import math


class Vision:
    """Provides a type of vision (Original, Peripheral, Parafoveal, Foveal)."""

    def __init__(self, frame, percent, pixels):
        self.zoom(frame, percent)
        self.frame = cv2.resize(self.frame, (pixels, pixels))
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

    def zoom(self, frame, percent):
        """Zoom in on an image."""
        size = frame.shape[1]
        print(size)
        new_size = math.floor(size * percent)
        move = (size - new_size) // 2
        self.frame = frame[move:(size - move), move:(size - move)]

    def get_difference(self, prev_frame):
        """Get the difference between two frames"""
        self.diff = cv2.absdiff(self.gray, prev_frame)
        self.thresh = cv2.threshold(self.diff, 30, 255, cv2.THRESH_BINARY)[1]

    def get_edge(self):
        """Get the edges in the frame."""
        self.edge = cv2.Canny(self.frame, 100, 200)

    def get_faces(self, face_cascade):
        """Get the faces in the frame"""
        pass


def setup(frame, percent, pixels):
    """Setup a new type of vision."""
    return Vision(frame, percent, pixels)


# def foveal(frame):
#     """Preset size for foveal vision."""
#     width, height = frame.shape[:2]
#     print(width, height)
#     return Vision(frame, 64)
