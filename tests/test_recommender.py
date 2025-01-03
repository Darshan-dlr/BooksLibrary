import pytest
import asyncio
import pandas as pd
from unittest.mock import AsyncMock, patch
from app.recommender import BookRecommender


@pytest.fixture
def mock_books_data():
    """Fixture for mock book data."""
    return [
        {"title": "Book 1", "genre": "['Fantasy', 'Adventure']", "average_rating": 4.5},
        {"title": "Book 2", "genre": "['Science Fiction']", "average_rating": 3.8},
        {"title": "Book 3", "genre": "['Fantasy']", "average_rating": 4.7},
    ]


@pytest.fixture
def recommender():
    """Fixture for the BookRecommender instance."""
    return BookRecommender()


@patch("recommender.merged_review_collection.find")
@pytest.mark.asyncio
async def test_load_data(mock_find, recommender, mock_books_data):
    """Test the load_data method."""
    mock_find.return_value = AsyncMock()
    mock_find.return_value.to_list.return_value = mock_books_data

    df = await recommender.load_data()
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == len(mock_books_data)
    assert list(df.columns) == ["title", "genre", "average_rating"]


@patch.object(BookRecommender, "load_data")
@pytest.mark.asyncio
async def test_prepare_data(mock_load_data, recommender, mock_books_data):
    """Test the prepare_data method."""
    mock_load_data.return_value = pd.DataFrame(mock_books_data)

    await recommender.prepare_data()

    assert recommender.features is not None
    assert recommender.df is not None
    assert recommender.knn is not None


@patch.object(BookRecommender, "prepare_data")
@pytest.mark.asyncio
async def test_recommend_books(mock_prepare_data, recommender, mock_books_data):
    """Test the recommend_books method."""
    mock_prepare_data.return_value = None
    recommender.df = pd.DataFrame(mock_books_data)
    recommender.features = [[1, 4.5], [0, 3.8], [1, 4.7]]

    result = await recommender.recommend_books(["Fantasy"], min_rating=4.0, num_recommendations=2)

    assert not result.empty
    assert "title" in result.columns
    assert len(result) <= 2


@patch.object(BookRecommender, "load_data")
@pytest.mark.asyncio
async def test_recommend_books_by_title(mock_load_data, recommender, mock_books_data):
    """Test the recommend_books_by_title method."""
    mock_load_data.return_value = pd.DataFrame(mock_books_data)

    result = await recommender.recommend_books_by_title("Book 1", min_rating=4.0, num_recommendations=2)

    assert isinstance(result, pd.DataFrame)
    assert "title" in result.columns
