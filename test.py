import cv2
import eye


def main():
    """For testing the FVS library."""
    right = eye.setup(0)
    left = eye.setup(1)
    right.start()
    left.start()



if __name__ == '__main__':
    main()
