import json

with open("./imdb-top250.json", encoding="utf-8") as f:
    movies = json.load(f)

print(f"The first movie in the list is: {movies[0]['navn']}")

ratings_total = 0
for movie in movies:
    ratings_total += movie["karakter"]

print(f"The average rating is: {ratings_total / len(movies)}/10")

ratings_total = 0
for movie in movies[:11]:
    ratings_total += movie["karakter"]

print(f"The average rating of the first 10 movies is: {ratings_total / 10}/10")

directors = {}
for movie in movies:
    for director in movie["regissører"]:
        if not director in directors:
            directors[director] = 1
        else:
            directors[director] += 1

most_directed_num = max(directors.values())
most_directed = []

for director, movies_num in directors.items():
    if movies_num == most_directed_num:
        most_directed.append(director)

print("The directors which have directed the most movies from the top 250 list:")
print("\n".join(most_directed))
print(f"Which have all directed {most_directed_num} movies")
