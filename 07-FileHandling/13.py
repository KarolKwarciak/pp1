file = open("movies.txt", "a")
movie_titles = ["D", "Joker", "Batman", "B", "c"]
count = 1
for i in movie_titles:
    file.write(f"{count}. {i}"+"\n")
    count += 1
file.close()
