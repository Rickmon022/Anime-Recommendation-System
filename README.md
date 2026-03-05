# Anime Recommendation System

A content-based recommendation engine built with Python that suggests similar anime based on shared genres, media types, and episode counts. The system uses **Natural Language Processing (NLP)** techniques to quantify anime metadata and **Cosine Similarity** to measure the distance between different titles.

---

## 🚀 Features
* **Content-Based Filtering:** Recommends anime by analyzing metadata tags rather than user ratings.
* **Text Vectorization:** Implements `CountVectorizer` to transform categorical data into numerical vectors.
* **Interactive UI:** A clean, user-friendly interface built with **Streamlit**.
* **Automated Data Fetching:** Integrated with `kagglehub` to pull the latest dataset directly.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
* **Web Framework:** Streamlit
* **Deployment/Storage:** Pickle (for model serialization)

---

## 📂 Project Structure
* `app.py`: The Streamlit web application.
* `anime_recommendation_content_based.ipynb`: Notebook for data cleaning, EDA, and model building.
* `animes.pkl`: Serialized DataFrame containing processed anime titles and tags.
* `simil.pkl`: The pre-calculated Cosine Similarity matrix.

---

## 📊 How It Works



1.  **Data Preprocessing:** Genres, types, and episode counts are cleaned and merged into a single `tag` column.
2.  **Vectorization:** The `tag` strings are converted into a 1000-dimensional vector space using Bag of Words.
3.  **Similarity Matrix:** We calculate the cosine of the angle between vectors. A value closer to **1** indicates high similarity.
4.  **Retrieval:** When a user selects an anime, the system sorts the similarity scores and returns the top 5 closest matches.


---

## 🔧 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/anime-recommender.git](https://github.com/your-username/anime-recommender.git)
    cd anime-recommender
    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit pandas numpy scikit-learn kagglehub
    ```

3.  **Generate the Models:**
    Run all cells in the `.ipynb` file to download the dataset and create the `animes.pkl` and `simil.pkl` files.

4.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

---

## 📝 Dataset
The project utilizes the **Anime Recommendations Database** from Kaggle, featuring over 12,000 anime titles.

---

## 🤝 Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
