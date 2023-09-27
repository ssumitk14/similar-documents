from faker import Faker
from constant import NOISE_FILE_PATH, TO_COMPARE
from helper import load_files, load_text_files, get_one_to_many_similarity_scores
import os
from tqdm import tqdm
from PyPDF2 import PdfReader

fake = Faker()

random_text_list = [fake.text() for i in range(50)]
random_text = "\n\n".join(random_text_list)


def add_noise(data_path, file, noise_at_page=1):
    reader = PdfReader(os.path.join(data_path, file))
    text_list = []
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        text_list.append(text)

    text_list.insert(noise_at_page-1, random_text)
    text_file = os.path.join(NOISE_FILE_PATH, file + str(noise_at_page) + '.txt')
    with open(text_file, 'w', encoding="utf-8") as f:
        f.write(str("\n\n".join(text_list)))

    return "\n\n".join(text_list)


pdf_file_names = [i for i in os.listdir(TO_COMPARE) if ".pdf" in i]
file_contents_dict = {}
for file_name in tqdm(pdf_file_names):
    noise_contents = add_noise(TO_COMPARE, file_name)

file_to_compare = load_files(TO_COMPARE)
files_to_compare_with = load_text_files(NOISE_FILE_PATH)
score = get_one_to_many_similarity_scores(file_to_compare, files_to_compare_with)
print(f"Similarity score of {list(file_to_compare.keys())[0]} is {score[1]} with the file {score[0]}")