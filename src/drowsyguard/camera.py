import cv2


class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(camera_index)

        if not self.capture.isOpened():
            raise RuntimeError(
                f"Unable to open camera with index {camera_index}"
            )

    def is_opened(self):
        return self.capture.isOpened()

    def read(self):
        success, frame = self.capture.read()

        if not success:
            raise RuntimeError("Unable to read frame from camera")

        return frame

    def release(self):
        if self.capture.isOpened():
            self.capture.release()

        cv2.destroyAllWindows()