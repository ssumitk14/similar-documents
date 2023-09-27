import os
from tqdm import tqdm
# from langchain.document_loaders import PyPuPDFLoader
from PyPDF2 import PdfReader
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_pdf_file(data_path, file):
    reader = PdfReader(os.path.join(data_path, file))
    text_list = []
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        text_list.append(text)

    return "\n\n".join(text_list)

def load_files(data_path):
    pdf_file_names = [i for i in os.listdir(data_path) if ".pdf" in i]
    file_contents_dict = {}
    for file_name in tqdm(pdf_file_names[:2]):
        file_contents_dict[file_name] = read_pdf_file(data_path, file_name)

    return file_contents_dict

def document_similarity(doc1, doc2):
    # vectorizer =
    vectors = TfidfVectorizer().fit_transform([doc1, doc2])

    similarity = cosine_similarity(vectors)
    return similarity
