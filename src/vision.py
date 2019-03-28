import cv2


class Vision:
    """Provides a type of vision (Original, Peripheral, Parafoveal, Foveal)."""

    def __init__(self, view, size):
        self.size = (size, size)
        self.view = cv2.resize(view, self.size)
        self.gray = cv2.cvtColor(self.view, cv2.COLOR_BGR2GRAY)

    def get_difference(self, prev_view):
        """Get the difference between two views"""
        self.diff = cv2.absdiff(self.gray, prev_view)
        self.thresh = cv2.threshold(self.diff, 30, 255, cv2.THRESH_BINARY)[1]

    def get_edge(self):
        """Get the edges in the view."""
        self.edge = cv2.Canny(self.view, 100, 200)

    def get_faces(self, face_cascade):
        """Get the faces in the view"""
        pass


def custom_vision(view, size):
    """Setup vision using a view and size."""
    return Vision(view, size)


def foveal_vision(view):
    """Preset size for foveal vision."""
    return Vision()
