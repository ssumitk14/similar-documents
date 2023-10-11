
# Calculating Similarity Between Multiple Documents

This program calculates the similarity between multiple documents using the cosine similarity metric. The cosine similarity metric is a measure of how similar two vectors are. It is calculated by taking the dot product of the two vectors and dividing by the product of their magnitudes.

The program takes a list of documents as input and returns a list of similarity scores for each pair of documents. The similarity scores are between 0 and 1, with 1 being the most similar and 0 being the least similar.

#### Usage
* Put target file to  ```data/to_compare``` folder 
* Put Files with which you want to compare the target file to this folder ```data/compare_with```

##### To install the requirements, use the below command
```
pip install -r requirements.txt
```

##### To use the program, simply run the following command:
```
python app.py
```
