#Visualize

###A simple script that reads any file as binary and outputs it as a png file.
takes input file and a name for the output file as command-line arguments.
For example:
`visualize.py testfile.pdf pdftest`

this yields a file 'pdf_bit_image.png' which looks something like this:

![example image](/sample\ images/pdftest.png)

When visualized.py is given as the file argument, this image is produced:

![Visualized.py visualized!](/visualize_visualized.png)

This image is scaled to 1000% of the original, as the algorithm produces an image relative to the size of the file - so smaller files can yield very tiny results.

More examples can be found in the 'sample images folder'
