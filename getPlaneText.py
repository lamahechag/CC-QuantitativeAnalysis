from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file("CONSTITUCION-Interiores.pdf", "rb"))

# print the title of document1.pdf
print "title = %s" % (input1.getDocumentInfo())
print "title = %s" % (input1.getPage(0).extractText())
for i in range(5):
        print "title = %s" % (input1.getPage(i).extractText())


