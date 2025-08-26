import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# (b) Load movies.csv into a pandas DataFrame
# Ensure movies.csv is in the same directory
movies_df = pd.read_csv("C:/Users/Aksha/Desktop/Movie-Search-Assginment-main/Movie-Search-Assginment-main/Assignment-1/movies.csv")

# Quick check of the dataset
print(movies_df.head())

# (c) Create embeddings using all-MiniLM-L6-v2
# Load the pretrained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings for movie plots/descriptions
movies_df['embedding'] = movies_df['plot'].apply(lambda x: model.encode(x))

# (d) Implement search_movies(query, top_n)
def search_movies(query, top_n=5):
    """
    Returns top_n most similar movies to the query based on cosine similarity of embeddings.
    Args:
        query (str): Search query text
        top_n (int): Number of top movies to return
    Returns:
        DataFrame: Top_n matching movies with similarity score
    """
    # Encode query
    query_embedding = model.encode([query])
    
    # Extract embeddings from dataframe
    embeddings = list(movies_df['embedding'])
    
    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    
    # Add similarity scores to DataFrame
    movies_df['similarity'] = similarities
    
    # Return top_n sorted by similarity
    return movies_df[['title', 'plot', 'similarity']].sort_values(by='similarity', ascending=False).head(top_n)

# (e) Test with query "spy thriller in Paris"
results = search_movies("spy thriller in Paris", top_n=5)
print(results)
