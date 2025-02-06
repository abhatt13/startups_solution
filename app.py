import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import spacy

# Load dataset
data = pd.read_excel("cleaned_data56k.xlsx")
data_cleaned = data.drop_duplicates()
# data_cleaned['Description_cleaned'] = data_cleaned['Description'].apply(lambda x: str(x).lower())

# Load spaCy model and sentence transformer model
nlp = spacy.load("en_core_web_md")
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load precomputed matrices and vectorizer

with open("tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vectorizer = pickle.load(f)

with open("spacy_matrix56k.pkl", "rb") as f:
    spacy_matrix = pickle.load(f)

with open("sentence_embeddings56k.pkl", "rb") as f:
    sentence_embeddings = pickle.load(f)

   
def get_spacy_vector(text):
    doc = nlp(text)
    return doc.vector 


# Define a function to get top similar companies
def get_top_similar_companies(company_name, method='sentence', top_n=10):
    company_description = data_cleaned[data_cleaned['Name'] == company_name]['Description_cleaned'].values[0]
    
    if method == 'tfidf':
        # Use the loaded tfidf_vectorizer instead of initializing a new one
        company_vec = tfidf_vectorizer.transform([company_description])
        similarity_scores = cosine_similarity(company_vec, tfidf_matrix)
    elif method == 'spacy':
        company_vec = get_spacy_vector(company_description).reshape(1, -1)
        similarity_scores = cosine_similarity(company_vec, spacy_matrix)
    elif method == 'sentence':
        company_vec = sentence_model.encode([company_description])
        similarity_scores = cosine_similarity(company_vec, sentence_embeddings)

    top_indices = similarity_scores[0].argsort()[-top_n-1:][::-1][1:]
    similar_companies = data_cleaned.iloc[top_indices]
    similar_companies['Similarity Score'] = similarity_scores[0][top_indices]
    
    return similar_companies[['Name', 'Description', 'Similarity Score']]

# Streamlit UI
st.title("Company Similarity Finder")
st.sidebar.header("Select Options")
selected_company = st.sidebar.selectbox("Choose a Company", data_cleaned['Name'].unique())
similarity_method = st.sidebar.selectbox("Select Similarity Method", ('tfidf', 'spacy', 'sentence'))
top_n = st.sidebar.slider("Number of Similar Companies", min_value=1, max_value=20, value=10)

if st.sidebar.button("Find Similar Companies"):
    with st.spinner("Calculating..."):
        results = get_top_similar_companies(selected_company, method=similarity_method, top_n=top_n)
    
    st.subheader(f"Top {top_n} companies similar to {selected_company}")
    st.write(results[['Name', 'Description', 'Similarity Score']])

    # Optional: Plot similarity scores
    st.bar_chart(results[['Similarity Score']].set_index(results['Name']))
