
import PyPDF2
import os

pdfFileObj = open('judgement.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

texts = ''

for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText()
    texts += text

texts = texts.replace('\n','')

with open('acts.txt', 'r') as f:
    acts_data = f.read()

all_acts = acts_data.split('\n')

for act in all_acts:
    if act in texts:
        print(act)



