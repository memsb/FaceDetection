import cv2
from face_detection import anonymise_faces, get_anonymisation_method
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', help='Input filename', required=True)
parser.add_argument('--output', help='Output filename', required=True)
parser.add_argument('--method', help='Anonymisation method, Blur or Pixelate',
                    choices=["blur", "pixelate"],
                    default="blur")

args = parser.parse_args()

input_path = args.input
output_path = args.output
method = get_anonymisation_method(args.method)

img = cv2.imread(input_path)
anonymise_faces(img, method)
cv2.imwrite(output_path, img)
