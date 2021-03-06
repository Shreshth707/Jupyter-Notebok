from operations import Operations

path1 = '/home/shreshth/Desktop/Jupyter-Notebook/Sem 6/Image Processing/Practical 5: Arthematic & Logical Operations/hero.png'
path2 = '/home/shreshth/Desktop/Jupyter-Notebook/Sem 6/Image Processing/Practical 5: Arthematic & Logical Operations/humanoid.png'

operations = Operations(path1,path2)

img1,img2 = operations.adjust__dimensions_of_images(*operations.load_images())

# Addition
operations.add_images(img1,img2)
# Subtraction
operations.subtract_images(img1,img2)
# Multiplication
operations.multiply_images(img1,img2)
# Not Image
operations.not_image(img1)
# And Image
operations.and_images(img1,img2)
# Or Image
operations.or_images(img1,img2)
# Xor Image
operations.xor_images(img1,img2)
