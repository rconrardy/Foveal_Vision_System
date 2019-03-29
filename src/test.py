import cv2
import eye


def main():
    """For testing the FVS library."""
    capture = eye.setup(0)
    capture.start()


if __name__ == '__main__':
    main()
