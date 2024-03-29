fav_colors = ["blue", "red", "black", "green"]

siblings_age = [24, 20, 25, 40]

coin_toss = ["heads", "tails", "tails", "heads", "tails"]

fav_artists = ["RHCP", "Azuna", "Romeo Santos"]

fav_words = {
    "abject": "expeirenced or present to the maximum degree",
    "direful": "extremely bad or dreadful",
    "furtive": "attempting to avoid notice or attention, typically because of guilt",
}

fav_movies = {"hulk": 2003, "juice": 1992, "city_of_god": 2002}

fav_cities = {"san_juan": 347052, "st_maarten": 41109, "st_thomas": 41813}

friends = {"me": 24, "eden": 25, "steph": 20}

# get the last item in the list 
print(fav_colors[-1])

# add city to fav_cities 
fav_cities['toronto'] = 2930000

print(fav_cities)

# reverse list
# print(coin_toss[::-1])

# reverse list another way 
coin_toss.reverse()
reversed_flip = coin_toss
print(reversed_flip)

# show the population of a city 
print(fav_cities['toronto'])

# for artist 
for artist in fav_artists: 
    print(f'I think {artist} is great!')

# print the first two artists - range 
print(fav_artists[0:2])

# print when the movie was released 
for movie, year in fav_movies.items(): 
    print(f'{movie} came out in {year}')

# sort and reverse list 
print(list(sorted(siblings_age, reverse = True)))

#add "Beauty and the Beast" to fav_movies with release date 1991 and 2017 
fav_movies['beauty_and_the_beast'] = [1991, 2017]
print(fav_movies)

