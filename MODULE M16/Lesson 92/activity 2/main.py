import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Movie": ["Inception", "The Dark Knight", "Interstellar", "Avengers", "Joker", "Parasite"],
    "Genre": ["Sci-Fi", "Action", "Sci-Fi", "Action", "Drama", "Drama"],
    "Rating": [8.8, 9.0, 8.6, 8.4, 8.5, 8.6],
    "Votes_million": [2.3, 2.5, 2.0, 1.1, 1.4, 0.8]
}

df = pd.DataFrame(data)

print("IMDB Movie Ratings:")
print(df)
print()
print("Average Rating:", round(df["Rating"].mean(), 2))
print("Highest Rated:", df.loc[df["Rating"].idxmax(), "Movie"])
print()
print("Average Rating by Genre:")
print(df.groupby("Genre")["Rating"].mean())

plt.figure(figsize=(8, 4))
plt.barh(df["Movie"], df["Rating"], color="steelblue")
plt.xlabel("IMDB Rating")
plt.title("IMDB Movie Ratings")
plt.xlim(8.0, 9.2)
plt.tight_layout()
plt.savefig("imdb_ratings.png")
plt.show()
