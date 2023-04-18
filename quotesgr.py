import random

with open("greek_quotes.txt", encoding="iso8859-7") as fil:
    data = fil.read().split("%")


print(random.choice(data))
