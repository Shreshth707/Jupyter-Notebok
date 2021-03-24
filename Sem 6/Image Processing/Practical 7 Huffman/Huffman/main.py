import cv2 as cv
import huffman

img = cv.imread('sample.jpg', 0)
img_flattened = img.flatten()

img_encoded = huffman.encode(img_flattened)

img_encoded_path = "encoded.txt"

with open(img_encoded_path, "w") as f:
    f.write(img_encoded)

print(f"The encoded image is stored in:\n{img_encoded_path}")
