import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dataset
movies = pd.read_csv('movies.csv')

# Fill missing values
movies = movies.fillna('')

# Create lowercase title column 
movies['title_lower'] = movies['title'].str.lower()

# Combine features
movies['combined'] = (
    movies['genres'] + ' ' +
    movies['keywords'] + ' ' +
    movies['overview']
)

# Convert text to vectors
vectorizer = CountVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(movies['combined'])

# Similarity matrix
similarity = cosine_similarity(vectors)

def recommend(movie_title):

    # Convert input to lowercase for case-insensitive matching
    movie_title = movie_title.lower()

     # Partial matching movie
    matching_movies = movies[
        movies['title_lower'].str.contains(movie_title)
    ]

    # If movie is not found, return a message
    if matching_movies.empty:
        return ["Movie not found. "]
    
    # Get first matching movie  
    movie_index = matching_movies.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )
        

    return recommendations

     