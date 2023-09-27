import os
from tqdm import tqdm
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from constant import PREPROCESSED_DATA_PTH

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
    for file_name in tqdm(pdf_file_names):
        file_contents_dict[file_name] = read_pdf_file(data_path, file_name)
    return file_contents_dict

def cosine_document_similarity(doc1, doc2):
    vectors = TfidfVectorizer().fit_transform([doc1, doc2])
    similarity = cosine_similarity(vectors)
    return similarity

def get_similarity_scores(file_contents_dict):
    similarity_dict = {}
    for file_name in file_contents_dict:
        similarity_dict[file_name] = []
        similarity_scores = []
        for file2 in file_contents_dict:
            if file_name != file2:
                score_matrix = cosine_document_similarity(file_contents_dict[file_name], file_contents_dict[file2])
                similarity_scores.append({file2: score_matrix[0][1]})
        similarity_dict[file_name] = similarity_scores

    return similarity_dict

def save_dict2json(dictionary, file_name = "file.json"):
    file_path = os.path.join(PREPROCESSED_DATA_PTH, file_name)
    with open(file_path, "w") as outfile:
        json.dump(dictionary, outfile)
