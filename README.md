# Scripts
A collection of short Python scripts I use.

## Working with PDFs

- __crop.py__: Clips the content of a PDF files to a rectangle object.
  - args:
    - "-in": Input,file to crop name.
    - "-out": Output,cropped file name.
    - "-l": Left margin value (integer).
    - "-b": Bottom margin value (integer).
    - "-height": Height of the cropped file (integer).
    - "-width": Width of the cropped file (integer).
  - Exple:
    - python crop.py -in fileToCrop.pdf -out croppedFile.pdf -b 150 -l 150 -height 600 -width 450
- __extract.py__: Extracts pages from a PDF  and combines them into one file.
    - args;
      - "-in": Input file to extract pages from.
      - "-out": Output file name to combine the extracted pages into.
      - "-p": a list the pages' numbers, comma separated. For example (-p 1-5,12,13,15-20,25) would print the pages (1, 2, 3, 4, 5, 12, 13, 15, 16, 17, 18, 19, 20, 25)
    - Exple:
      - python extract.py -in fileToExtractFrom.pdf -out extractedPages.pdf -p 1-5,12,13,15-20,25
- __multiExtract.py__:
- __combine.py__:
- __split.py__:
