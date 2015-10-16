import png
import sys
import array

def main():
    if len(sys.argv) < 3:
        print("Usage: python mistify.py [in_file] [out_file]")
        sys.exit(-1)

    inFile = sys.argv[1]
    outFile = sys.argv[2]

    image = png.Reader(inFile)
    data = image.read()

    # put the pixel data in a flat array
    pixels = [list(row) for row in list(data[2])]
    pixels = [pixel for row in pixels for pixel in row]

    output = open(outFile, 'wb')
    # write the pixel data array as bytes to the output file
    output.write(array.array('B', pixels))
    output.close()

if __name__ == "__main__":
    main()