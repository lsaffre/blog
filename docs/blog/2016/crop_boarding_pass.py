from __future__ import print_function

from PyPDF2 import PdfFileWriter, PdfFileReader
from argh import dispatch_command, arg, CommandError


@dispatch_command
@arg('filenames', help="The pdf files to crop.")
@arg('--bottom',
     default=None,
     help='Height of bottom area to crop. Default is half of page.')
def main(bottom=None, *filenames):
    output = PdfFileWriter()
    for filename in filenames:
        pdfin = PdfFileReader(open(filename, "rb"))

        # print how many pages pdfin has:
        print("{} has {} pages.".format(filename, pdfin.getNumPages()))
        for p in pdfin.pages:
            mb = p.mediaBox
            # print(mb)
            b = bottom or (mb.getUpperRight_y() / 2)
            # p.mediaBox.upperRight = (
            mb.lowerRight = (mb.getLowerRight_x(), b)
            mb.lowerLeft = (mb.getLowerLeft_x(), b)
            output.addPage(p)
    output.write(file("output.pdf", "wb"))
