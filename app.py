from helper import load_files, document_similarity

data_path = "./data"

if __name__ == "__main__":
    file_contents_dict = load_files(data_path)
    print(file_contents_dict.keys())

    similarity_dict = {}
    for file_name in file_contents_dict:
        similarity_dict[file_name] = []
        similarity_scores = []
        for file2 in file_contents_dict:
            if file_name!=file2:
                score_matrix = document_similarity(file_contents_dict[file_name], file_contents_dict[file2])
                similarity_scores.append(score_matrix[0][1])
        similarity_dict[file_name] = similarity_scores

    print(similarity_dict)

