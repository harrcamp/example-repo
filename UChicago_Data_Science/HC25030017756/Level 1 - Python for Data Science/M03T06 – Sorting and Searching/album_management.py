# Defining the Album class and performing all requested operations

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


# 3. Create albums1 with five Album objects and print it
albums1 = [
    Album("Abbey Road", 17, "The Beatles"),
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Hotel California", 9, "Eagles")
]
print("albums1:", [str(album) for album in albums1])

# 4. Sort albums1 by number_of_songs and print
albums1.sort(key=lambda a: a.number_of_songs)
print("albums1 sorted by number_of_songs:", [str(album) for album in albums1])

# 5. Swap element at position 1 (index 0) with position 2 (index 1) and print
albums1[0], albums1[1] = albums1[1], albums1[0]
print("after swapping first two elements:", [str(album) for album in albums1])

# 6. Create albums2
albums2 = [
    Album("Nevermind", 13, "Nirvana"),
    Album("Born to Run", 8, "Bruce Springsteen"),
    Album("Led Zeppelin IV", 8, "Led Zeppelin"),
    Album("Purple Rain", 9, "Prince"),
    Album("Bad", 10, "Michael Jackson")
]
print("albums2:", [str(album) for album in albums2])

# 8. Copy all albums from albums1 into albums2
albums2.extend(albums1)

# 9. Add two new albums
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# 10. Sort albums2 alphabetically by album_name and print
albums2.sort(key=lambda a: a.album_name)
print("albums2 sorted alphabetically by album_name:", [str(album) for album in albums2])

# 11. Search for "Dark Side of the Moon" and print its index
index = next((i for i, a in enumerate(albums2) if a.album_name == "Dark Side of the Moon"), None)
print("Index of 'Dark Side of the Moon' in albums2:", index)
