class LibraryItem:
    def __init__(self, name, artist, rating=0):     #create constructor
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0

    def info(self):     #Return a string combining track name, artist, and visual star rating
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):     #Generates a string of asterisks (*) representing a rating
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
