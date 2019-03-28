import cv2
import threading
import time


class Eye:
    """Provides vision using a camera."""

    def __init__(self, id):
        """Initialize a new eye object."""
        self.id = id
        self.stream = cv2.VideoCapture(id)
        self.signals = {"shutdown": False, "grabbed": False}

    def capture(self):
        """Start capturing the stream for the current eye."""
        # Read a frame from the stream
        self.signals["grabbed"], self.frame = self.stream.read()
        # Run the program until it is told to shut down
        while not self.signals["shutdown"]:
            # Ensure that the frame is grabbed from the stream
            if not self.signals["grabbed"]:
                # Stop the capture
                self.stop()
            else:
                # Set the last frame captured equal to the previous frame.
                prev_frame = self.frame
                # Read a frame fromt the stream.
                self.signals["grabbed"], self.frame = self.stream.read()
                # Show the stream
                cv2.imshow("Video" + str(self.id), self.frame)
                # Stop the program when there is a shutoff signal
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.stop()
                    break

    def start(self):
        """Create a new thread for capturing the stream."""
        # Make a new thread for capturing the video
        self.t1 = threading.Thread(target=self.capture, args=())
        # Start the thread.
        self.t1.start()

    def stop(self):
        """Ends the thread for eye."""
        self.signals["shutdown"] = True



def setup(id):
    """Setup a new eye using a camera id."""
    return Eye(id)
