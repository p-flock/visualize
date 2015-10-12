import png
import sys

def make_pixel_array(byte_object):
    '''splits byte object into triples of values 0-255
        corresponding to rgb pixel values
    '''
    return list(zip(*[iter(byte_object)]*3))

def main():
    if len(sys.argv) < 3:
        print("Usage: python visualize.py [in_file] [out_file]")
        sys.exit(-1)

    inFile = sys.argv[1]
    outFile = sys.argv[2]

    with open(inFile, mode='rb') as file: # import file to read as a binary
        byte_file = file.read()

    pixel_values = make_pixel_array(byte_file)
    image_size = int(len(pixel_values) ** 0.5)
    # splits values into arrays of equal size to make the rows/columns of the image
    pixel_array=[pixel_values[x:x+image_size] for x in range(0, len(pixel_values), image_size)]

    # truncates pixel info to ensure a square image
    if len(pixel_array[-1]) != image_size:
        pixel_array = pixel_array[:-1]

    if (outFile[-4:]) != ".png":
        outFile += ".png"
    
    #print(pixel_array) #if you want to see individual pixel values, uncomment
    # creating the pixel array makes saving the image easy, PIL-like
    png.from_array(pixel_array, 'RGB').save(str(outFile))

if __name__ == "__main__":
    main()
