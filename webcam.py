import cv2
from face_detection import anonymise_faces, get_anonymisation_method
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--method', help='Anonymisation method, Blur or Pixelate',
                    choices=["blur", "pixelate"],
                    default="blur")
args = parser.parse_args()
method = get_anonymisation_method(args.method)

WINDOW_NAME = "Webcam"
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
ret, img = cap.read()
cv2.imshow(WINDOW_NAME, img)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow(WINDOW_NAME, anonymise_faces(img, method))

    if cv2.waitKey(1) == 13:
        break

    if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
