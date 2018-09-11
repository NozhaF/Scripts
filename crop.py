import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def crop(args):
    fileToCrop = PdfFileReader(args.input, "rb")
    writer = PdfFileWriter()
    for i in range(fileToCrop.getNumPages()):
        page = fileToCrop.getPage(i)
        page.cropBox.setLowerLeft((args.left, args.bottom))
        page.cropBox.setUpperLeft((args.left, args.height))
        page.cropBox.setUpperRight((args.width, args.height))
        page.cropBox.setLowerRight((args.width, args.bottom))
        writer.addPage(page)
    finalFile = open(args.output, "wb")
    writer.write(finalFile)
    finalFile.close()


def main():
    parser = argparse.ArgumentParser(description="Crops the file pages")
    parser.add_argument("-in", help="File to crop", dest="input", type=str, required=True)
    parser.add_argument("-out", help="Cropped file", dest="output", type=str, required=True)
    parser.add_argument("-b", help="Bottom margin", dest="bottom", type=int, default=100)
    parser.add_argument("-l", help="Left margin", dest="left", type=int, default=100)
    parser.add_argument("-height", help="Height", dest="height", type=int, default=700)
    parser.add_argument("-width", help="Width", dest="width", type=int, default=500)
    parser.set_defaults(func=crop)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
