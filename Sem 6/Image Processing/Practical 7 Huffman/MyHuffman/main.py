
from PIL import ImageChops
from PIL import Image
from compression import compress_image
from decompression import decompress_image

def raw_size(width, height):
    header_size = 2 * 16 # height and width as 16 bit values
    pixels_size = 3 * 8 * width * height # 3 channels, 8 bits per channel
    return (header_size + pixels_size) / 8

def images_equal(file_name_a, file_name_b):
    image_a = Image.open(file_name_a)
    image_b = Image.open(file_name_b)

    diff = ImageChops.difference(image_a, image_b)

    return diff.getbbox() is None

if __name__ == '__main__':
    # start = time.time()
    
    compress_image('sample.png', 'answer.txt')

    print('-' * 40)

    decompress_image('answer.txt', '1_out.png')

    # stop = time.time()
    # times = (stop - start) * 1000

    print('-' * 40)

    # print('Run time takes %d miliseconds' % times)
    print('Images equal = %s' % images_equal('1.png', '1_out.png'))