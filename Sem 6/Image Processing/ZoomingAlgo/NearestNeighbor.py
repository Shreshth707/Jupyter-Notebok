import matplotlib.image as img
import numpy as npy
from statistics import mean

def nearestNeighbourInterpolation(og_img, factor):

    w, h = og_img.shape[:2]

    xNew = int(w * factor)
    yNew = int(h * factor)

    xScale = xNew/(w-1)
    yScale = yNew/(h-1)

    newImage = npy.zeros([xNew, yNew, 4])

    for i in range(xNew-1):
        for j in range(yNew-1):
            newImage[i + 1, j + 1] = og_img[1 +
                                            int(i / xScale), 1 + int(j / yScale)]

    img.imsave('image processing\\nearestNeighbour.png', newImage)


def bilinearInterpolation(og_img):
    w, h = og_img.shape[:2]

    xNew = int(2 * w - 1)
    yNew = int(2 * h - 1)

    newImage = npy.zeros([xNew, yNew, 4])

    for i in range(0, xNew-1, 2):
        for j in range(yNew-1):
            if j % 2 == 0:
                newImage[i, j] = og_img[int(i/2), int(j/2)]
            else:
                newImage[i, j] = (og_img[int(i/2), int((j-1)/2)] +
                                  og_img[int(i/2), int((j+1)/2)])/2

    for i in range(1, xNew-2, 2):
        for j in range(yNew-1):
            newImage[i, j] = (newImage[i-1, j]+newImage[i+1, j])/2

    img.imsave('image processing\\bilinear.png', newImage)


def kTimesInterpolation(og_img, k):
    w, h = og_img.shape[:2]
    gray_img = toGrayscale(og_img)

    xNew = int(k * (w-1) + 1)
    yNew = int(k * (h-1) + 1)

    newImage = npy.zeros([xNew, yNew, 4])

    for i in range(0, xNew-1, k):
        for j in range(0, yNew-1, k):
            newImage[i, j] = gray_img[int(i/k), int(j/k)]

    for i in range(xNew-1):
        if i % k == 0:
            for j in range(yNew-1):
                if j % k == 0:
                    newImage[i, j] = gray_img[int(i/k), int(j/k)]
                else:
                    x = min(gray_img[int(i/k), int(j/k)][0],
                            gray_img[int(i/k), int(j/k+1)][0])
                    d = abs(gray_img[int(i/k), int((j/k))][0] -
                            gray_img[int(i/k), int((j/k+1))][0])/k
                    val = x+(j % k)*d
                    newImage[i][j][0] = val
                    newImage[i][j][1] = val
                    newImage[i][j][2] = val
                    newImage[i][j][3] = 1

    for i in range(xNew-1):
        if i % k != 0:
            for j in range(yNew-1):
                x = min(newImage[(int(i/k)*k), j][0],
                        newImage[int(i/k)*k+k, j][0])
                d = abs(newImage[(int(i/k)*k), j][0] -
                        newImage[int(i/k)*k+k, j][0])/k
                val = x+(i % k)*d
                newImage[i][j][0] = val
                newImage[i][j][1] = val
                newImage[i][j][2] = val
                newImage[i][j][3] = 1

    img.imsave('image processing\\ktimes.png', newImage)


def toGrayscale(og_img):
    w, h = og_img.shape[:2]

    newImage = npy.zeros([w, h, 4])

    for i in range(w):
        for j in range(h):
            lst = [float(og_img[i][j][0]), float(
                og_img[i][j][1]), float(og_img[i][j][2])]
            avg = float(mean(lst))
            newImage[i][j][0] = avg
            newImage[i][j][1] = avg
            newImage[i][j][2] = avg
            newImage[i][j][3] = 1

    return newImage


m = img.imread("image processing\\image.png")
nearestNeighbourInterpolation(m, 10)
bilinearInterpolation(m)
kTimesInterpolation(m, 3)