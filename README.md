# 🚀 Startups Solution  
*A Company Similarity Finder for Analyzing Startup Data*  

![GitHub stars](https://img.shields.io/github/stars/abhatt13/startups_solution?style=social)
![GitHub forks](https://img.shields.io/github/forks/abhatt13/startups_solution?style=social)
![GitHub issues](https://img.shields.io/github/issues/abhatt13/startups_solution)
![GitHub license](https://img.shields.io/github/license/abhatt13/startups_solution)

## 📌 Overview  
**Startups Solution** is a **Streamlit-based web application** designed to help users find similar companies based on textual descriptions. It leverages **NLP techniques** and **machine learning models** to compute similarity scores using multiple methods like **TF-IDF, spaCy embeddings, and Sentence Transformers**.  

### 🔹 Features  
- Compare company descriptions using **TF-IDF, spaCy, or Sentence Transformers embeddings**  
- Precomputed similarity matrices for efficient retrieval  
- Interactive **Streamlit UI** for user-friendly experience  
- Supports visualization of similarity scores  

---
## 📊 Data Pipeline

### 🔍 Explanation

 The flow includes:

1. **Data Ingestion**  
   - Startup descriptions and metadata are collected from various sources.
   - The data is preprocessed to clean and standardize text fields.

2. **Feature Engineering & Embeddings**  
   - Multiple NLP-based similarity methods are used, including **TF-IDF, spaCy embeddings, and Sentence Transformers**.
   - Precomputed embeddings and similarity matrices improve computational efficiency.

3. **Similarity Computation**  
   - The system compares companies based on textual similarities.
   - **cosine similarity** is used to rank similar startups.

4. **Storage & Optimization**  
   - Processed data is stored in optimized structures for fast retrieval.
   - Pickle files and databases (optional) help cache and manage similarity matrices.

5. **User Interaction via Streamlit**  
   - Users can explore and compare startups through an interactive **Streamlit UI**.
   - The interface supports multiple similarity computation methods.

### 🚀 Future Expansion

The following diagram illustrates the **full data pipeline** for the project:

![Data Pipeline Future Expansion](https://github.com/abhatt13/startups_solution/blob/main/Sprint_Planning-1.png)

This project can be further **expanded and enhanced** by:

- **Integrating a Real-time Database:** Instead of using static precomputed matrices, store and update company descriptions dynamically.
- **Scalability with Cloud Services:** Deploy the solution using **AWS, GCP, or Azure** for enhanced performance.
- **More Advanced NLP Models:** Experiment with **BERT, GPT embeddings, or industry-specific LLMs** to improve similarity accuracy.
- **Multi-Language Support:** Expand to support startup descriptions in multiple languages using **spaCy multilingual models**.
- **API Integration:** Expose similarity computation as a REST API for external applications to consume.

This structured **data pipeline** ensures that the project is **modular, scalable, and efficient** in finding similar companies based on descriptions. 🚀




## 🛠️ Installation  

### **1. Clone the Repository**  
```bash
git clone https://github.com/abhatt13/startups_solution.git
cd startups_solution
```

### **2. Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Download the SpaCy Model**  
```bash
python -m spacy download en_core_web_md
```

## 🚀 Usage  

### **Run the Application**  
```bash
streamlit run app.py
```

### **How It Works**  
- Choose a company from the dropdown menu  
- Select a similarity method (**TF-IDF, spaCy, Sentence Transformers**)  
- Set the number of similar companies to retrieve  
- Click **"Find Similar Companies"** and view results with similarity scores  

### 📂 Project Structure  
```
📦 startups_solution  
 ┣ 📜 app.py                    # Main Streamlit application  
 ┣ 📜 requirements.txt           # List of dependencies  
 ┣ 📜 cleaned_data56k.xlsx       # Dataset with company descriptions  
 ┣ 📜 tfidf_matrix.pkl           # Precomputed TF-IDF similarity matrix  
 ┣ 📜 tfidf_vectorizer.pkl       # TF-IDF vectorizer  
 ┣ 📜 spacy_matrix56k.pkl        # Precomputed spaCy embeddings  
 ┣ 📜 sentence_embeddings56k.pkl # Sentence Transformers embeddings  
 ┗ 📜 README.md                  # Documentation  
```
## 🔬 Technologies and Libraries Used  
- **Python**  
- **Streamlit**  
- **spaCy**  
- **Scikit-learn**  
- **Sentence Transformers**  
- **Pandas**  
- **NumPy**  

## 🏆 Contributing  
Contributions are welcome! To contribute:  

1. **Fork** the repository  
2. **Create a new branch**  
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes**   
   ```bash
   git commit -m "Added a new feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature-branch
   ```
5. **Open a Pull Request**  

## 📜 License  
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

## 📬 Contact  
For any questions or suggestions, feel free to reach out:  

📧 Email: aakashbhatt13@gmail.com   
👔 LinkedIn: [Aakash Bhatt](https://www.linkedin.com/in/aakashpadmanabhbhatt/)  

Happy Coding! 🚀  
    
