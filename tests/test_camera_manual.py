import cv2

from drowsyguard.camera import Camera


camera = None

try:
    camera = Camera()

    print("Camera started.")
    print("Press Q to quit.")

    while True:
        frame = camera.read()

        cv2.imshow("DrowsyGuard Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except RuntimeError as error:
    print(f"Camera error: {error}")

finally:
    if camera is not None:
        camera.release()

print("Camera stopped.")