import os
from tqdm import tqdm
# from langchain.document_loaders import PyPuPDFLoader
from PyPDF2 import PdfReader

def read_pdf_file(file):
    reader = PdfReader(os.path.join(data_path, file_name))
    text_list = []
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        text_list.append(text)

    return text_list

data_path = "./data"
pdf_file_names = [i for i in os.listdir(data_path) if ".pdf" in i]
print(pdf_file_names)

file_contents = {}
for file_name in tqdm(pdf_file_names):
    file_contents[file_name] = read_pdf_file(os.path.join(data_path, file_name))

print(file_name)
print(len(file_contents[file_name]))

