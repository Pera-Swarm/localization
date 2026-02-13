import time

import cv2

try:
    import picamera
    from picamera.array import PiRGBAnalysis
except ImportError as exc:
    raise RuntimeError(
        "Missing dependency 'picamera'. Install on Raspberry Pi and run with a Pi camera enabled."
    ) from exc


class PreviewAnalyzer(PiRGBAnalysis):
    def __init__(self, camera):
        super().__init__(camera)
        self.should_stop = False

    def analyze(self, frame):
        cv2.imshow("PiCamera Preview", frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            self.should_stop = True


def configure_camera(camera):
    camera.shutter_speed = 35000
    camera.iso = 400

    time.sleep(2)

    camera.exposure_mode = 'off'

    time.sleep(2)


def main():
    with picamera.PiCamera(resolution=(1024, 768), framerate=25) as camera:
        configure_camera(camera)

        detector = PreviewAnalyzer(camera)
        camera.start_recording(detector, format='rgb')
        try:
            while not detector.should_stop:
                camera.wait_recording(0.1)
        finally:
            camera.stop_recording()
            detector.close()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
