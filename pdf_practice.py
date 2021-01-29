import PyPDF2
import sys


pdf_docs = sys.argv[1:]

def pdf_joiner(pdf_files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write('merged_pdf.pdf')


pdf_joiner(pdf_docs)
