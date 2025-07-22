# Topic Modeling using LDA on 20 Newsgroups Dataset

This project demonstrates how to apply **Latent Dirichlet Allocation (LDA)** to perform **topic modeling** on the popular **20 Newsgroups** dataset. It uses `scikit-learn`, `NLTK`, and `pyLDAvis` for interactive topic visualization.

---

## Objective

Group similar documents together to uncover latent topics from a large corpus of unstructured text using **LDA**. Visualize and interpret the topic distributions, and predict the most probable topic for new documents.

---

## Features

- Load and preprocess real-world text data from `sklearn.datasets`.
- Tokenization, stopword removal, and lemmatization using `NLTK`.
- Convert documents into document-term matrix with `CountVectorizer`.
- Fit an **LDA model** using `scikit-learn`.
- Explore dominant words per topic.
- Interactive topic visualization using `pyLDAvis`.
- Predict topics for new/unseen text documents.

---

## Dependencies

- Python 3.7+
- scikit-learn
- numpy
- pandas
- matplotlib
- seaborn
- nltk
- pyLDAvis

---

## Concepts Used

- LDA (Latent Dirichlet Allocation)
- Bag of Words & Count Vectorizer
- Text preprocessing (lemmatization, stopword removal)Topic prediction on new/unseen documents
- pyLDAvis visualization
  
---

## Installation

Clone the repository and install the dependencies:

```
git clone https://github.com/your-username/document-clustering-for-topic-modeling.git
cd document-clustering-for-topic-modeling
pip install -r requirements.txt
```

Make sure to also download the required NLTK resources:

```
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
```
---

## How to Run
Run the notebook in Jupyter or JupyterLab:

```
jupyter notebook Document-Clustering-for-Topic-Modeling.ipynb
```
Or, if you convert it into a Python script:
```
python Document-Clustering-for-Topic-Modeling.py
```
