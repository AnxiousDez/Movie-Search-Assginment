# Movie Semantic Search Assignment

This repository contains my solution for the **semantic search on movie plots assignment**.  
The project implements a semantic search engine that uses embeddings to find the most relevant movies based on a text query.

---

## Project Overview
- Loads a dataset (`movies.csv`) containing movie titles and plots.  
- Generates embeddings using **`all-MiniLM-L6-v2`** from `sentence-transformers`.  
- Implements a function `search_movies(query, top_n)` that returns the most relevant movies using **cosine similarity**.  
- Includes unit tests to validate functionality.  

---

## Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/AnxiousDez/movie-search-assignment.git
   cd movie-search-assignment
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```


---

## Testing

Run unit tests to ensure everything works correctly:

```bash
python -m unittest tests/test_movie_search.py -v
```
output: 
test_search_movies_output_format (tests.test_movie_search.TestMovieSearch.test_search_movies_output_format)
Test if search_movies returns a DataFrame with correct columns. ... ok
test_search_movies_relevance (tests.test_movie_search.TestMovieSearch.test_search_movies_relevance)        
Test if returned movies are relevant to the query. ... ok
test_search_movies_similarity_range (tests.test_movie_search.TestMovieSearch.test_search_movies_similarity_range)
Test if similarity scores are between 0 and 1. ... ok
test_search_movies_top_n (tests.test_movie_search.TestMovieSearch.test_search_movies_top_n)
Test if search_movies returns the correct number of results. ... ok

----------------------------------------------------------------------
Ran 4 tests in 3.348s 
OK
---

## Usage Example

Inside the notebook or a Python script:

```python
from movie_search_solution import search_movies

results = search_movies("spy thriller in Paris", top_n=5)
print(results)

 output:

              title                                               plot  similarity
0         Spy Movie  A spy navigates intrigue in Paris to stop a te...    0.769684
1  Romance in Paris  A couple falls in love in Paris under romantic...    0.388030
2      Action Flick  A high-octane chase through New York with expl...    0.256777
```




