class Song:
    def __init__(self, tittle, author, lyrics):
        self.tittle = tittle
        self.author = author
        self.lyrics = lyrics
        print(f"New song {tittle} written by {author} is made.")


    def sing(self):
        print(f"{self.tittle} by {self.author}")
        for i in self.lyrics:
            print(i)


    def yell(self):
        capital_lyrics = [line.upper() for line in self.lyrics]
        capital_tittle = self.tittle.upper()
        capital_author = self.author.upper()
        print(f"{capital_tittle} by {capital_author}")
        for i in capital_lyrics:
            print(i)


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])

ziemelmeita.sing()
print("\n")
ziemelmeita.yell()
