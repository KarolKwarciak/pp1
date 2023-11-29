import json
movie = {
    "title":"The Hateful Eight",
    "year": "2016",
    "actor":{"leading":"Samuel.L.Jackson","supporting":"Kurt Russel"},
    "oscar":False,
    "Director":"QUentin Tarantino"
}
file = open("favourite.json","a")
json.dump(movie,file)

file.close()