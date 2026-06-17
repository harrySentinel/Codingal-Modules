print("What is a Recommendation Engine?")
print("A recommendation engine suggests items to users based on their preferences.")
print()
print("Real-world Examples:")
print("  Netflix  -> Suggests movies based on what you watched")
print("  Amazon   -> 'Customers who bought this also bought...'")
print("  Spotify  -> Suggests songs based on your playlist")
print("  YouTube  -> Recommends videos based on watch history")
print("  Codingal -> Suggests next lessons based on progress")
print()
print("Types of Recommendation Systems:")
print("  1. Content-Based Filtering  - Recommends similar items")
print("  2. Collaborative Filtering  - Recommends based on similar users")
print("  3. Hybrid                   - Combines both approaches")
print()

movies = {
    "Aditya":  ["Inception", "Interstellar", "The Dark Knight"],
    "Riya":    ["Inception", "Titanic", "The Notebook"],
    "Aman":    ["Interstellar", "The Dark Knight", "Avengers"],
    "Neha":    ["Titanic", "The Notebook", "La La Land"]
}

user = "Aditya"
user_movies = set(movies[user])

print(f"Movies watched by {user}: {list(user_movies)}")
print()

recommendations = set()
for other_user, watched in movies.items():
    if other_user != user:
        for movie in watched:
            if movie not in user_movies:
                recommendations.add(movie)

print("Recommended movies for", user, ":", list(recommendations))
