from imdb import IMDB


name = "Skyscraper"
i = IMDB()

m1 = i.search(name,year=2018)
print(m1)


