#this script reads a .pdf file and prints it to the screen

#this script works

import PyPDF2

pdf_file = "txttopdf.pdf"

pdf_read = PyPDF2.PdfFileReader(pdf_file)
page = pdf_read.getPage(0)
page_content = page.extractText()
print(page_content)
