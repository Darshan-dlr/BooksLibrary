"""
recommender.py
==============

This module provides the `BookRecommender` class, which implements a K-Nearest Neighbors (KNN)
algorithm for recommending books based on genres and average ratings.

The recommender system fetches data from a MongoDB collection and preprocesses it to
train the KNN model. Recommendations can be generated based on:
- Specific genres with a minimum rating threshold.
- A reference book's title.

Classes
-------
- `BookRecommender` : Encapsulates the recommendation logic.

Dependencies
------------
- `sklearn.neighbors` : For the KNN model.
- `sklearn.preprocessing` : For encoding genres.
- `pandas` : For data manipulation.
- `motor` : For asynchronous MongoDB interaction.

Usage
-----
Instantiate the `BookRecommender` class and call the `recommend_books` or `recommend_books_by_title` methods.

Example:
    recommender = BookRecommender()
    recommendations = recommender.recommend_books(['Fantasy'], min_rating=4.0)
"""

import logging
import asyncio
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import NearestNeighbors
from .database import merged_review_collection 

logging.basicConfig(level=logging.INFO)

class BookRecommender:
    def __init__(self):
        """
        Initialize the BookRecommender.
        """
        self.mlb = MultiLabelBinarizer()
        self.knn = NearestNeighbors(n_neighbors=10, metric='cosine')
        self.features = None
        self.df = None  # Initialize df as None initially

    async def load_data(self):
        """
        Load the dataset from MongoDB asynchronously.
        
        Returns:
        pd.DataFrame: DataFrame containing the book data.
        """
        cursor = merged_review_collection.find({})
        books_data = await cursor.to_list(length=None)
        df = pd.DataFrame(books_data)
        return df

    async def prepare_data(self):
        """
        Preprocess the data and train the KNN model asynchronously.
        """
        df = await self.load_data()

        df['genre'] = df['genre'].apply(lambda x: eval(x))  # Use eval to convert string to list

        # Filter out books with empty genres
        df = df[df['genre'].apply(len) > 0]

        df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')
        genres_encoded = self.mlb.fit_transform(df['genre'])
        self.features = np.hstack([genres_encoded, df['average_rating'].values.reshape(-1, 1)])
        self.knn.fit(self.features)

        self.df = df

    async def train_model(self):
        """
        Train the KNN model asynchronously.
        """
        await self.prepare_data()

    async def recommend_books(self, genres, min_rating=4.0, num_recommendations=5):
        """
        Recommend books based on genres and minimum average rating.

        Parameters:
        genres (list of str): List of genres to base recommendations on.
        min_rating (float): Minimum average rating for the recommendations.
        num_recommendations (int): Number of recommendations to return.

        Returns:
        pd.DataFrame: DataFrame containing the recommended books.
        """
        if self.features is None:
            await self.train_model()

        genre_vector = self.mlb.transform([genres])
        avg_rating_vector = np.array([[min_rating]])
        genre_avg_vector = np.hstack([genre_vector, avg_rating_vector])

        distances, indices = self.knn.kneighbors(genre_avg_vector, n_neighbors=len(self.df))

        recommendations = self.df.iloc[indices[0]]
        recommendations = recommendations[recommendations['average_rating'] >= min_rating]
        recommendations['matched_genres'] = recommendations['genre'].apply(lambda x: len(set(genres) & set(x)))
        recommendations = recommendations[recommendations['matched_genres'] > 0]
        recommendations = recommendations.sort_values(by=['matched_genres', 'average_rating'], ascending=[False, False])

        return recommendations.head(num_recommendations)[['title', 'average_rating', 'matched_genres']]

    async def recommend_books_by_title(self, book_title, min_rating=4.0, num_recommendations=5):
        """
        Recommend books based on a book title.

        Parameters:
        book_title (str): The title of the book to base recommendations on.
        min_rating (float): Minimum average rating for the recommendations.
        num_recommendations (int): Number of recommendations to return.

        Returns:
        pd.DataFrame: DataFrame containing the recommended books.
        """
        df = await self.load_data()

        book_row = df[df['title'].str.contains(book_title, case=False, na=False)]

        if book_row.empty:
            return f"No book found with the title '{book_title}'"

        genres = eval(book_row.iloc[0]['genre'])  # Convert genre from string to list

        return await self.recommend_books(genres, min_rating, num_recommendations)
