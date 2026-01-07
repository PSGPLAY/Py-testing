import PyPDF2
import os
import sys

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
   if file.endswith('.pdf'):
      merger.append(file)

   merger.write('merged.pdf')