#this script takes a textfile named "test.txt" and converts it to a .pdf file called "txttopdf.pdf"
#the textfile must not have more than 35 lines

from reportlab.pdfgen import canvas

file_name = "txttopdf.pdf"

document_title = "txttopdf"

title = "txttopdf"

pdf = canvas.Canvas(file_name)

pdf.setTitle(document_title)

#now read the text file (in this case "test.txt" and save as list)
with open("test.txt", "r") as file:
    list = []
    for line in file:
        list += [line.strip()]  #das .strip() entfernt "\n"


print(list)

y = 700

for line in list:
    y = y - 20
    pdf.drawString(100, y, line)

pdf.save()
