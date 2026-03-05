# 🎬 Anime Recommendation System

A content-based recommendation engine built with Python that suggests similar anime based on shared genres, media types, and episode counts. The system uses **Natural Language Processing (NLP)** techniques and **Cosine Similarity** to find the perfect match for your next binge-watch.

---

## 🚀 Live Demo
Check out the live application here:  
👉 **[Anime Recommender App](https://anime-recommendation-system-ris.streamlit.app/)**

---

## ✨ Features
* **Search & Select:** Choose from over 12,000 anime titles.
* **Smart Recommendations:** Returns the top 5 most similar anime based on metadata.
* **"See More" Functionality:** Dynamically load additional recommendations using Streamlit session state.
* **NLP Powered:** Uses `CountVectorizer` (Bag of Words) to process anime tags.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Science:** Pandas, NumPy, Scikit-Learn
* **App Framework:** Streamlit
* **Version Control:** Git LFS (for handling large similarity matrices)

---

## 📂 Project Structure
* `app.py`: The Streamlit web application interface.
* `anime_recommendation_content_based.ipynb`: Data preprocessing and model building notebook.
* `animes.pkl`: Serialized processed anime data.
* `simil.pkl`: The pre-calculated Cosine Similarity matrix (stored via Git LFS).

---

## 📊 How It Works


1.  **Preprocessing:** Genres and types are cleaned and merged into a single `tag` string.
2.  **Vectorization:** Each anime's tags are converted into a numerical vector using a 1000-word vocabulary.
3.  **Similarity:** We calculate the **Cosine Similarity** between vectors. 
    
    $$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

4.  **Ranking:** When you select an anime, the app finds the vectors with the smallest "distance" to your selection and displays them.

---

## 🔧 Local Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/CoderRishik022/Anime-Recommendation-System.git](https://github.com/CoderRishik022/Anime-Recommendation-System.git)
   cd Anime-Recommendation-System

2. **Install Git LFS (Required for the similarity matrix):**
    ```bash
    git lfs install
    git lfs pull

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the App:**
    ```bash
    streamlit run app.py
