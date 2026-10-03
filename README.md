# 🎬 Movie Recommendation System

A simple content-based movie recommendation system built with Python, Pandas, Scikit-learn, and Streamlit.

The application recommends movies that are similar to a movie selected by the user based on movie genres.

## 🚀 Features

* Select a movie from the available dataset
* Find movies with similar genres
* Generate 5 movie recommendations
* Simple and interactive Streamlit interface
* Uses TF-IDF and cosine similarity for recommendations

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* MovieLens Dataset

## 🧠 How It Works

1. The MovieLens movie dataset is loaded using Pandas.
2. Movie genres are converted into numerical TF-IDF vectors.
3. Cosine similarity is used to compare the selected movie with other movies.
4. The system identifies the most similar movies.
5. The top 5 recommendations are displayed in the Streamlit application.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── dataset/
│   ├── movies.csv
│   └── ratings.csv
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Go into the project folder:

```bash
cd Movie-Recommendation-System
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

This project uses the MovieLens dataset provided by GroupLens.

The application uses the `movies.csv` and `ratings.csv` files.

## 🎯 Project Objective

The objective of this project is to demonstrate how a basic recommendation system can use movie metadata and similarity techniques to provide personalized movie suggestions.

## 👨‍💻 Author

Tanmay Malewar
