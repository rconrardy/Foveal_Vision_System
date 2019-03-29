import cv2
import threading
import vision


class Eye:
    """Provides vision using a camera."""

    def __init__(self, id):
        """Initialize a new eye object."""
        self.id = id
        self.stream = cv2.VideoCapture(id)
        self.status = {
            "shutdown": False,
            "grabbed": False
        }
        self.vision = {
            "foveal": {
                "ratio": 1/3,
                "pixals": 64,
                "curr": None,
                "prev": None
            },
            "parafoveal": {
                "ratio": 2/3,
                "pixals": 64,
                "curr": None,
                "prev": None
            },
            "Peripheral": {
                "ratio": 3/3,
                "pixals": 64,
                "curr": None,
                "prev": None
            }
        }

    def capture(self):
        """Start capturing the stream for the current eye."""
        self.status["grabbed"], frame = self.stream.read()
        frame = crop_square(frame)
        for type, param in self.vision.items():
            param["curr"] = vision.setup(
                frame,
                param["ratio"],
                param["pixals"]
            )
        while not self.status["shutdown"]:
            if self.status["grabbed"]:
                self.update(frame)
            else:
                self.stop()

    def update(self, frame):
        prev_frame = frame
        for type, param in self.vision.items():
            param["prev"] = param["curr"]
        self.status["grabbed"], frame = self.stream.read()
        frame = crop_square(frame)
        for type, param in self.vision.items():
            param["curr"] = vision.setup(
                frame,
                param["ratio"],
                param["pixals"]
            )
            cv2.imshow(type, param["curr"].frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop()

    def start(self):
        """Create a new thread for capturing the stream."""
        self.t1 = threading.Thread(target=self.capture, args=())
        self.t1.start()

    def stop(self):
        """Ends the thread for eye."""
        self.status["shutdown"] = True


def crop_square(frame):
    """Crop the current frame to a square."""
    width, height = frame.shape[:2]
    if width > height:
        move = (width - height) // 2
        frame = frame[move:(width - move), :]
    elif width < height:
        move = (height - width) // 2
        frame = frame[:, move:(height - move)]
    return frame


def setup(id):
    """Setup a new eye using a camera id."""
    return Eye(id)
