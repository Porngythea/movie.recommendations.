print("🎬 Welcome to the AI Movie Recommendation System!")
print("Find a movie that matches your mood!")

movies = [
    {
        "title": "Frozen",
        "genre": "animation",
        "mood": "happy",
        "rating": 7.4,
        "overview": "A magical and heartwarming adventure about two sisters."
    },
    {
        "title": "Inside Out",
        "genre": "animation",
        "mood": "happy",
        "rating": 8.1,
        "overview": "A wonderful story about emotions and friendship."
    },
    {
        "title": "Harry Potter",
        "genre": "fantasy",
        "mood": "excited",
        "rating": 7.9,
        "overview": "A magical adventure filled with friendship and courage."
    },
    {
        "title": "Finding Nemo",
        "genre": "adventure",
        "mood": "happy",
        "rating": 8.2,
        "overview": "An exciting journey about family and love."
    },
    {
        "title": "The Lion King",
        "genre": "adventure",
        "mood": "emotional",
        "rating": 8.5,
        "overview": "A beautiful story about courage, family and responsibility."
    },
    {
        "title": "Cinderella",
        "genre": "romance",
        "mood": "romantic",
        "rating": 7.3,
        "overview": "A heartwarming fairy tale about hope and love."
    }
]

# Get user preferences
genre = input("\nChoose a genre (animation, fantasy, adventure, romance): ").lower()

mood = input("Choose your mood (happy, excited, emotional, romantic): ").lower()

min_rating = float(input("Enter your minimum IMDb rating (0-10): "))

# Find matching movies
recommendations = []

for movie in movies:
    if (movie["genre"] == genre
        and movie["mood"] == mood
        and movie["rating"] >= min_rating):
        recommendations.append(movie)

# Display recommendations
print("\n🎥 Your Movie Recommendations:")

if recommendations:
    for movie in recommendations:
        print("\n----------------------------")
        print("Title:", movie["title"])
        print("Genre:", movie["genre"])
        print("IMDb Rating:", movie["rating"])
        print("Overview:", movie["overview"])

        # Simple sentiment analysis
        positive_words = ["wonderful", "magical", "heartwarming",
                          "friendship", "love", "courage", "beautiful"]

        score = sum(
            word in movie["overview"].lower()
            for word in positive_words
        )

        if score >= 2:
            print("Sentiment: Positive 😊")
        else:
            print("Sentiment: Neutral 😐")

else:
    print("Sorry! No matching movies found.")
    print("Try changing your preferences!")

print("\nThank you for using our Movie Recommendation System! 🍿")