import cv2;
import numpy as np;

class Operations():

    def __init__(self,path1,path2):
        self.path1 = path1
        self.path2 = path2

    def load_images(self):    
        img1 = cv2.imread(self.path1)
        img2 = cv2.imread(self.path2)
        return img1,img2

    def adjust__dimensions_of_images(self,img1,img2):
        x = abs(img1.shape[0] - img2.shape[0])
        y = abs(img1.shape[1] - img2.shape[1])
        z = abs(img1.shape[2] - img2.shape[2])
        
        if img1.shape[0]>img2.shape[0]:
            img2 = np.concatenate((img2,np.zeros((x,img2.shape[1],img2.shape[2]))),axis=0)
        elif img1.shape[0]<img2.shape[0]:
            img1 = np.concatenate((img1,np.zeros((x,img1.shape[1],img1.shape[2]))),axis=0)
        if img1.shape[1]>img2.shape[1]:
            img2 = np.concatenate((img2,np.zeros((img2.shape[0],y,img2.shape[2]))),axis=1)
        elif img1.shape[1]<img2.shape[1]:
            img1 = np.concatenate((img1,np.zeros((img1.shape[0],y,img1.shape[2]))),axis=1)
        if img1.shape[2]>img2.shape[2]:
            img2 = np.concatenate((img2,np.zeros((img2.shape[0],img2.shape[1],z))),axis=2)
        elif img1.shape[2]<img2.shape[2]:
            img1 = np.concatenate((img1,np.zeros((img1.shape[0],img1.shape[1],z))),axis=2)
        
        cv2.imshow("Image1",img1)
        cv2.imshow("Image2",img2)
        cv2.waitKey(0);
        cv2.destroyAllWindows()
        return img1,img2

    def add_images(self,img1,img2):
        res_img = img1 + img2
        cv2.imwrite('./addition_image.png',res_img)
        cv2.imshow('Addition',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img

    def subtract_images(self,img1,img2):
        res_img = abs(img1 - img2)
        cv2.imwrite('./subtraction_image.png',res_img)
        cv2.imshow('Subtraction',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img
        
    def multiply_images(self,img1,img2):
        res_img = img1 * img2
        cv2.imwrite('./multipy_image.png',res_img)
        cv2.imshow('Multiplication',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img

    def not_image(self,img):
        res_img = cv2.bitwise_not(img)
        cv2.imwrite('./not_image.png',res_img)
        cv2.imshow('Not Image',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img

    def and_images(self,img1,img2):
        res_img = img1 & img2
        cv2.imwrite('./and_image.png',res_img)
        cv2.imshow('And Image',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img

    def or_images(self,img1,img2):
        res_img = img1 | img2
        cv2.imwrite('./or_image.png',res_img)
        cv2.imshow('Or Image',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img

    def xor_images(self,img1,img2):
        res_img = img1 ^ img2
        cv2.imwrite('./xor_image.png',res_img)
        cv2.imshow('Xor Image',res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return res_img

