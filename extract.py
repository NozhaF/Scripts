from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse


def extract(args):
    pages_list = args.pagesNumber.split(",")
    pages = []
    for i in pages_list:
        try:
            m = int(i)
            pages.append(m)
        except ValueError:
            subpages = i.split("-")
            subpages = list(range(int(subpages[0]), int(subpages[1]) + 1))
            for p in subpages:
                pages.append(p)

    fileToExtractFrom = PdfFileReader(args.input, "rb")
    writer = PdfFileWriter()
    for p in pages:
        page = fileToExtractFrom.getPage(p)
        writer.addPage(page)
    finalFile = open(args.output, "wb")
    writer.write(finalFile)
    finalFile.close()


def main():
    parser = argparse.ArgumentParser(description="Extracts pages from a PDF  and combines them into one file.")
    parser.add_argument("-in", help="Input file name", dest="input", type=str, required=True)
    parser.add_argument("-out", help="Output filename", dest="output", type=str, required=True)
    parser.add_argument("-p", help="list the pages numbers, comma separated", dest="pagesNumber", type=str, default="I")
    parser.set_defaults(func=extract)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
