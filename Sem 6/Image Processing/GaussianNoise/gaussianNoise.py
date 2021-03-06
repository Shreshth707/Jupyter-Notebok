import numpy as np
from cv2 import cv2

def gaussian(image):
   mean = 0
   var = 20
   sigma = var ** 0.9
   gauss = np.random.normal(mean, sigma, image.shape)
   gauss = gauss.reshape(image.shape)
   noisy = image + gauss
   return noisy

image = cv2.imread('sampleImage.jpg', 0)
noise_img = gaussian(image)
cv2.imwrite('./gaussianNoiseImage.jpg', noise_img)

