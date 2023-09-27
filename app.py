from helper import load_files, get_similarity_scores, save_dict2json
import os
import json
from constant import DATA_PATH, PREPROCESSED_DATA_PTH

if __name__ == "__main__":
    if not os.path.exists(os.path.join(PREPROCESSED_DATA_PTH, "pdf_text_content.json")):
        file_contents_dict = load_files(DATA_PATH)
        save_dict2json(file_contents_dict, "pdf_text_content.json")
    else:
        file_contents_dict = json.load(open(os.path.join(PREPROCESSED_DATA_PTH, "pdf_text_content.json")))

    similarity_score_dict = get_similarity_scores(file_contents_dict)
    print(similarity_score_dict)


