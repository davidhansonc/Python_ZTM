# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-07 16:48:19
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-07 18:01:10
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import sys

input_pdf = sys.argv[1]
watermark = sys.argv[2]

with open(input_pdf, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
    input_object = PdfFileReader(input_file)
    watermark_object = PdfFileReader(watermark_file)
    watermark_stain = watermark_object.getPage(0)

    output_object = PdfFileWriter()
    for i in range(input_object.getNumPages()):
        page = input_object.getPage(i)
        page.mergePage(watermark_stain)
        output_object.addPage(page)

    with open('watered.pdf', 'wb') as output_file:
        output_object.write(output_file)
