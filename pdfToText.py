from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

# converts pdf and returns its original as string


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close()
        return text


def convertMultiple(pdfDir, txtDir):
    for pdf in os.listdir(pdfDir):
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir+pdf
            text = convert(pdfFilename)
            textFilename = txtDir+pdf.split(".")[0]+".txt"
            textFile = open(textFilename, "w")
            textFile.write(text)


# dir where pdf/pdfs are located
pdfDir = r"C:/Users/sarjaisw/Desktop/python/pdfEditor/pdfIn/"
# dir where we are supposed to save text file/files
txtDir = r"C:/Users/sarjaisw/Desktop/python/pdfEditor/textIn/"
convertMultiple(pdfDir, txtDir)
