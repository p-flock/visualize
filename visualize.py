import png
import sys
from math import sqrt   # just need sqrt


''' deprecated and made simpler with make_pixel_array()'''
# def grouper(n, iterable, fillvalue=None):
    # "Collect data into fixed-length chunks or blocks"
    # "Used to create triples of bit values to be used as rgb pixels"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    # args = [iter(iterable)] * n
    # return izip_longest(fillvalue=fillvalue, *args)


def make_pixel_array(byte_object):
    '''splits byte object into triples of values 0-255
        corresponding to rgb pixel values
    '''
    pixels = []
    for r, g, b in zip(*[iter(byte_object)]*3):
        pixels.append((r, g, b))
    return pixels

def main():
    inFile = sys.argv[1]
    outFile = sys.argv[2]

    with open(inFile, mode='rb') as file: # import file to read as a binary
        byte_file = file.read()

    pixel_values = make_pixel_array(byte_file)
    image_size = int(sqrt(len(pixel_values)))
    # splits values into arrays of equal size to make the rows/columns of the image
    pixel_array=[pixel_values[x:x+image_size] for x in range(0, len(pixel_values), image_size)]

    # truncates pixel info to ensure a square image
    if len(pixel_array[-1]) != image_size:
        pixel_array = pixel_array[:-1]

    print(pixel_array)
    # creating the pixel array makes saving the image easy, PIL-like
    png.from_array(pixel_array, 'RGB').save(str(outFile) + '.png')

if __name__ == "__main__":
    main()
