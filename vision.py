import cv2
import math


class Vision:
    """Provides a type of vision (Original, Peripheral, Parafoveal, Foveal)."""

    def __init__(self, ratio, size):
        """Initialize a new vision."""
        self.params = {"ratio": ratio, "size": (size, size)}
        self.images = {}

    def update_curr(self, image):
        self.crop_image(image)
        self.images["curr"] = cv2.resize(
            self.images["curr"],
            self.params["size"]
        )
        self.images["gray"] = cv2.cvtColor(
            self.images["curr"],
            cv2.COLOR_BGR2GRAY
        )

    def update_prev(self):
        self.images["prev"] = self.images["gray"]

    def get_diff(self):
        self.images["diff"] = cv2.absdiff(
            self.images["prev"],
            self.images["gray"]
        )
        self.images["diff"] = cv2.threshold(
            self.images["diff"],
            30,
            255,
            cv2.THRESH_BINARY
        )[1]

    def get_edge(self):
        self.images["edge"] = cv2.Canny(
            self.images["curr"],
            100,
            200
        )

    def crop_image(self, image):
        size = image.shape[1]
        crop = math.floor(size * self.params["ratio"])
        move = (size - crop) // 2
        self.images["curr"] = image[move:(size - move), move:(size - move)]

    # def captur(self, frame):
    #     self.crop(frame, self.params["ratio"])
    #
    #     self.im = cv2.resize(self.im, (pixels, pixels))
    #     self.gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
    #
    # def crop(self, frame, ratio):
    #     """Crop around center."""
    #     size = frame.shape[1]
    #     new_size = math.floor(size * ratio)
    #     move = (size - new_size) // 2
    #     self.im = frame[move:(size - move), move:(size - move)]
    #
    # def get_difference(self, prev_frame):
    #     """Difference between frames"""
    #     self.diff = cv2.absdiff(self.gray, prev_frame)
    #     self.thresh = cv2.threshold(self.diff, 30, 255, cv2.THRESH_BINARY)[1]
    #
    # def get_edge(self):
    #     """Edges in frame."""
    #     self.edge = cv2.Canny(self.im, 100, 200)
    #
    # def get_faces(self, face_cascade):
    #     """Faces in frame"""
    #     pass


def setup(ratio, pixels):
    """Setup a new vision."""
    return Vision(ratio, pixels)
