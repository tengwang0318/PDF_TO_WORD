import win32com.client
import os

word = win32com.client.Dispatch("word.Application")
word.visible = 0

doc_pdf = ""
input_file = os.path.abspath(doc_pdf)
print(input_file)

wb = word.Documents.Open(input_file)
output_file = os.path.abspath(doc_pdf[0:-4]+"docx".format())
wb.SaveAs2(output_file,FileFormat=16)
print("Pdf to DOCx is completed")
wb.Close()
word.Quit()