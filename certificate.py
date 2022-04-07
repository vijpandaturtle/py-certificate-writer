import io
import os
import pandas as pd 

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

csv_file_path = "Webinar_participants.csv"
original_certificate_path = "certificate.pdf"

#Enter your CSV filename
data = pd.read_csv(csv_file_path)
#Make a destination directory
os.mkdir('certificates/')
#Loop over all fields
for i in range(len(data)):
    name = data.iloc[i][0]
    institution = data.iloc[i][1]
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('Helvetica', 14)
    can.drawString(400, 365, name)
    can.drawString(330, 330, institution)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # Specify path to the original certificate pdf
    existing_pdf = PdfFileReader(open(original_certificate_path, "rb"))
    output = PdfFileWriter()
    # Add the new pdf to the existing pdf page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to the target file
    destination_file = "certificates/certificate_{}.pdf".format(name)
    outputStream = open(destination_file, "wb")
    output.write(outputStream)
    outputStream.close()