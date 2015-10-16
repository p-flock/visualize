#Visualize

###A simple script that reads any file as binary and outputs it as a png file.
Takes an input file and a name for the output file as command-line arguments.

For example:

`:$python visualize.py testfile.pdf pdftest`

this yields a file 'pdftest.png' which looks something like this:

![example image](/sample\ images/pdftest.png)

When visualized.py is given as the file argument, this image is produced:

![Visualized.py visualized!](/sample\ images/visualize_visualized.png)

This image is scaled to 1000% of the original, as the algorithm produces an image relative to the size of the file - so smaller files can yield very tiny results.

More examples can be found in the 'sample images folder'

##Devisualize

###Simple script to devisualize the image produced by `visualize.py` back to the original file.

Takes an visualized input file and a name for the output file as command-line arguments.

For example:

`:$python mistify.py pdftest.png tesfile.pdf`

This yields the original pdf before it was visualized.