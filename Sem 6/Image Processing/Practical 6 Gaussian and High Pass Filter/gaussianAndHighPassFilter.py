import numpy as np
import cv2


def add_filter(image,filter):
    new_image=cv2.filter2D(image,-1,filter)
    cv2.imshow("original image", image)
    cv2.imshow("filtered image", new_image)
    cv2.imwrite("./output.png",new_image)      
    
    
image=cv2.imread("./sample.jpg")
cv2.imshow("sample image",image)
gaussian_filter=(1/4.8976)*np.matrix([
                                    [0.3679,0.6065,0.3679],
                                    [0.6065,1,0.6065],
                                    [0.3679,0.6065,0.3679]
                                ])

add_filter(image,gaussian_filter)
cv2.waitKey(0)  
cv2.destroyAllWindows()