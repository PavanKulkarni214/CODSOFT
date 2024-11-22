import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load data
data = pd.read_csv("data.csv", encoding='latin-1')

# Process genres
data['genre'] = data['genre'].fillna('')
count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'), token_pattern=None)
genre_matrix = count_vectorizer.fit_transform(data['genre'])

# Compute similarity
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Recommend items by rating
def recommend_items_by_rating(filter_type=None, n_recommendations=5):
    filtered_data = data.copy()
    if filter_type:
        filtered_data = filtered_data[filtered_data['type'] == filter_type]
    top_items = filtered_data.sort_values(by='rating', ascending=False).drop_duplicates(subset='title').head(n_recommendations)
    return top_items[['title', 'rating']]

# Interactive recommendation
def interactive_recommendation():
    print("Welcome to the Recommendation System!")
    print("\nWhat type of recommendations would you like?")
    print("1. Movies\n2. Books\n3. Both")
    choice = input("Enter your choice (1/2/3): ").strip()
    
    filter_type = "Movie" if choice == "1" else "Book" if choice == "2" else None
    try:
        n_recommendations = int(input("\nHow many recommendations would you like? ").strip())
    except ValueError:
        print("\nInvalid number. Defaulting to 5 recommendations.")
        n_recommendations = 5
    
    recommendations = recommend_items_by_rating(filter_type, n_recommendations)
    print("\nHere are your recommendations:")
    if not recommendations.empty:
        for _, row in recommendations.iterrows():
            print(f"- {row['title']} (Rating: {row['rating']})")
    else:
        print("No recommendations available for the selected category.")

# Run
interactive_recommendation()
