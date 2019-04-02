import cv2
import math


class Vision:
    """Provides a type of vision (Original, Peripheral, Parafoveal, Foveal)."""

    def __init__(self, ratio, size):
        """Initialize a new vision."""
        self.params = {"ratio": ratio, "size": (size, size)}
        self.images = {}

    def update_curr(self, image):
        """Update the current image (frame)."""
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
        """Update the previous image (frame)."""
        self.images["prev"] = self.images["gray"]

    def get_diff(self):
        """Get the difference between the current and previous image."""
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
        """Get the edges in the current image."""
        self.images["edge"] = cv2.Canny(
            self.images["curr"],
            100,
            200
        )

    def get_face(self):
        """Get the faces in the current image."""
        pass

    def crop_image(self, image):
        """Crop image to desired size."""
        size = image.shape[1]
        crop = math.floor(size * self.params["ratio"])
        move = (size - crop) // 2
        self.images["curr"] = image[move:(size - move), move:(size - move)]


def setup(ratio, pixels):
    """Setup a new vision with a ratio and pixel count."""
    return Vision(ratio, pixels)
