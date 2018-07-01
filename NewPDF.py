from pyPdf import PdfFileReader, PdfFileWriter
# Program to Read File
input =PdfFileReader(file('text-as-data.pdf','rb'))#Change with your Filename
output=PdfFileWriter()
n=int(input.getNumPages())
#print n
###############################################

#Logic to create page print order
seed=[1,8,4,5,7,2,6,3]
order=[]

for k in range(0,(n/8)+1):
    for x in range (0,len(seed)):
        y=(seed[x]+8*k)
        if (y<=n):
            order.append(y)
#print order
#print max(order)
###############################################

#Program to make the above changes to PDF
for p in order:
    if p%8==1:
        output.addPage(input.getPage(p-1).rotateClockwise(180))
    elif p%8==2:
        output.addPage(input.getPage(p-1).rotateClockwise(180))
    elif p%8==7:
        output.addPage(input.getPage(p-1).rotateClockwise(180))
    elif p%8==0:
        output.addPage(input.getPage(p-1).rotateClockwise(180))
    else:
        output.addPage(input.getPage(p-1))

##############################################

#Program to Save Edited File
outputStream = file("text-as-data-print.pdf", "wb")#Change with your Filename
output.write(outputStream)
outputStream.close()
