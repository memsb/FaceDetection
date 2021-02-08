import cv2
import numpy as np


def anonymise_faces(image, method):
    for (x, y, w, h) in detect_faces(image):
        face = image[y:y + h, x:x + w].copy()
        face = anonymise_face(face, method)
        image[y:y + h, x:x + w] = face

    return image


def detect_faces(image):
    cascade_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the image
    return face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )


def anonymise_face(face_img, method):
    (h, w) = face_img.shape[:2]
    centre = (int(h / 2), int(w / 2))
    radius = int(w / 2)

    # Create background and foreground masks
    fg_mask = np.full((face_img.shape[0], face_img.shape[1]), 0, dtype=np.uint8)
    cv2.circle(fg_mask, centre, radius, (255, 255, 255), -1)
    bg_mask = cv2.bitwise_not(fg_mask)

    obscured = method(face_img)

    fg = cv2.bitwise_or(obscured, obscured, mask=fg_mask)
    bk = cv2.bitwise_or(face_img, face_img, mask=bg_mask)

    return cv2.bitwise_or(bk, fg)


def pixelate_circle(original):
    pixelated = original.copy()
    (h, w) = original.shape[:2]
    blocks = 15
    x_steps = np.linspace(0, w, blocks + 1, dtype="int")
    y_steps = np.linspace(0, h, blocks + 1, dtype="int")
    # switch to iterator
    for i in range(1, len(y_steps)):
        for j in range(1, len(x_steps)):
            start_x = x_steps[j - 1]
            start_y = y_steps[i - 1]
            end_x = x_steps[j]
            end_y = y_steps[i]
            roi = original[start_y:end_y, start_x:end_x]
            (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
            cv2.rectangle(pixelated, (start_x, start_y), (end_x, end_y), (B, G, R), -1)

    return pixelated


def blur_circle(original):
    (h, w) = original.shape[:2]
    blurred = original.copy()
    blur_amount = h * 10
    blur_width = int(h / 8)
    blurred = cv2.blur(blurred, (blur_width, blur_width), blur_amount)

    return blurred


def get_anonymisation_method(method_name):
    methods = {"blur": blur_circle, "pixelate": pixelate_circle}

    return methods.get(method_name)
