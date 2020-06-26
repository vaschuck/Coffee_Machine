class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

title_ = input()
artist_ = input()
year_ = int(input())

new_painting = Painting(title_, artist_, year_)
print(f'"{new_painting.title}" by {new_painting.artist}',
      f'({new_painting.year}) hangs in the {new_painting.museum}.')
