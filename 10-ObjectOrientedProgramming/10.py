class Song():
    def __init__(self,author,song,album,year):
        self.author = author
        self.song = song
        self.album = album
        self.year = year
    def __str__(self):
        return f"author  {self.author}\nsong  {self.song}\nalbum  {self.album}\nyear  {song.year}"
      
song = Song(
    "Bisz","Wilk Chodnikowy", "Wilk chodnikowy", "2012"
)
song2 = Song(
    "Eripe", "Wszystko w porzadku", "Chamskie rzeczy", "2012"
)

print(song)
print()
print(song2)



