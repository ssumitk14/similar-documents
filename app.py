from helper import load_files, get_similarity_scores, save_dict2json, \
    get_one_to_many_similarity_scores
import os
import json
from constant import DATA_PATH, PREPROCESSED_DATA_PTH, TO_COMPARE, COMPARE_WITH


if __name__ == "__main__":
    if not os.path.exists(os.path.join(PREPROCESSED_DATA_PTH, "pdf_text_content.json")):
        file_contents_dict = load_files(DATA_PATH)
        save_dict2json(file_contents_dict, "pdf_text_content.json")
    else:
        file_contents_dict = json.load(open(os.path.join(PREPROCESSED_DATA_PTH, "pdf_text_content.json")))

    # similarity_score_dict = get_similarity_scores(file_contents_dict)
    # print(similarity_score_dict)

    file_to_compare = load_files(TO_COMPARE)
    files_to_compare_with = load_files(COMPARE_WITH)
    score = get_one_to_many_similarity_scores(file_to_compare, files_to_compare_with)
    print(f"Similarity score of {list(file_to_compare.keys())[0]} is {score[1]} with the file {score[0]}")


