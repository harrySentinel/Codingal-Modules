import pandas as pd

ratings = {
    "Aditya": {"Inception": 5, "Interstellar": 4, "Titanic": 2, "Avengers": 5, "The Notebook": 1},
    "Riya":   {"Inception": 4, "Interstellar": 2, "Titanic": 5, "Avengers": 3, "The Notebook": 5},
    "Aman":   {"Inception": 5, "Interstellar": 5, "Titanic": 1, "Avengers": 4, "The Notebook": 2},
    "Neha":   {"Inception": 2, "Interstellar": 1, "Titanic": 5, "Avengers": 2, "The Notebook": 4},
    "Rohan":  {"Inception": 4, "Interstellar": 4, "Titanic": 3, "Avengers": 5, "The Notebook": 2}
}

df = pd.DataFrame(ratings).T
print("User-Movie Rating Matrix:")
print(df)
print()

def cosine_similarity(u1, u2):
    common = [m for m in u1.index if u1[m] > 0 and u2[m] > 0]
    if not common:
        return 0
    dot = sum(u1[m] * u2[m] for m in common)
    mag1 = sum(u1[m] ** 2 for m in common) ** 0.5
    mag2 = sum(u2[m] ** 2 for m in common) ** 0.5
    return dot / (mag1 * mag2)

def recommend(user, df, top_n=2):
    user_ratings = df.loc[user]
    similarities = {}
    for other in df.index:
        if other != user:
            similarities[other] = cosine_similarity(user_ratings, df.loc[other])

    most_similar = sorted(similarities, key=similarities.get, reverse=True)[0]
    print(f"Most similar user to {user}: {most_similar} (similarity: {round(similarities[most_similar], 2)})")

    not_watched = df.loc[user][df.loc[user] == 0].index.tolist()
    if not not_watched:
        not_watched = df.columns[df.loc[user] < 3].tolist()

    scored = {m: df.loc[most_similar, m] for m in df.columns if df.loc[user, m] < 3}
    top = sorted(scored, key=scored.get, reverse=True)[:top_n]
    return top

user = input("Enter your name (Aditya/Riya/Aman/Neha/Rohan): ").strip()
if user in df.index:
    recs = recommend(user, df)
    print(f"Recommended movies for {user}:", recs)
else:
    print("User not found.")
