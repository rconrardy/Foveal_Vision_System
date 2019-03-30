import cv2
import threading
import vision


class Eye:
    """Provides vision using a camera."""

    def __init__(self, id):
        """Initialize a new eye."""
        self.stream = cv2.VideoCapture(id)
        self.status = {}
        self.vision = {}
        self.images = {}
        self.cam_id = id

    def capture(self):
        """Capture video stream."""
        self.setup_vision()
        self.update_curr()
        while not self.status["shutdown"]:
            self.update_prev()
            self.update_curr()
            self.vision["parafoveal"].get_edge()
            self.vision["peripheral"].get_diff()
            self.check_stop()
            cv2.imshow(
                "Original" + str(self.cam_id),
                cv2.resize(self.images["curr"], (400, 400))
            )
            cv2.imshow(
                "Foveal" + str(self.cam_id),
                cv2.resize(self.vision["mainfoveal"].images["curr"], (400, 400))
            )
            cv2.imshow(
                "Parafoveal" + str(self.cam_id),
                cv2.resize(self.vision["parafoveal"].images["curr"], (400, 400))
            )
            cv2.imshow(
                "Peripheral" + str(self.cam_id),
                cv2.resize(self.vision["peripheral"].images["curr"], (400, 400))
            )
            cv2.imshow(
                "Edge" + str(self.cam_id),
                cv2.resize(self.vision["parafoveal"].images["edge"], (400, 400))
            )
            cv2.imshow(
                "Difference" + str(self.cam_id),
                cv2.resize(self.vision["peripheral"].images["diff"], (400, 400))
            )


    def setup_vision(self):
        self.vision["mainfoveal"] = vision.setup(1/3, 64)
        self.vision["parafoveal"] = vision.setup(2/3, 64)
        self.vision["peripheral"] = vision.setup(3/3, 64)

    def update_curr(self):
        """Check if stream was read."""
        self.status["caught"], self.images["curr"] = self.stream.read()
        self.crop_image()
        if not self.status["caught"]:
            self.stop()
        self.vision["mainfoveal"].update_curr(self.images["curr"])
        self.vision["parafoveal"].update_curr(self.images["curr"])
        self.vision["peripheral"].update_curr(self.images["curr"])

    def update_prev(self):
        """Update """
        self.images["prev"] = self.images["curr"]
        self.vision["mainfoveal"].update_prev()
        self.vision["parafoveal"].update_prev()
        self.vision["peripheral"].update_prev()

    def check_stop(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop()

    def start(self):
        """Start recording."""
        self.status["shutdown"] = False

        self.t1 = threading.Thread(target=self.capture, args=())
        self.t1.start()

    def stop(self):
        """End recording."""
        self.status["shutdown"] = True

    def crop_image(self):
        """Crop image to quare."""
        width, height = self.images["curr"].shape[:2]
        if width > height:
            move = (width - height) // 2
            self.images["curr"] = self.images["curr"][move:(width - move), :]
        elif width < height:
            move = (height - width) // 2
            self.images["curr"] = self.images["curr"][:, move:(height - move)]


def setup(id):
    """Setup a new eye using a camera id."""
    return Eye(id)
