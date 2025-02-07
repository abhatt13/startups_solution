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
## 📊 Pipeline Overview
![Data Pipeline Diagram](TBD)


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
    
