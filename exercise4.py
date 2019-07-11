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

# print all ages that is less than 21 
for age in siblings_age: 
    if age < 21:
        print(f"You\'re {age}. You are\'nt legal in the US yet.")
    else: 
        print(f"You\'re {age}. You can come into the casino.")

# get max age 
print(max(siblings_age))

# count how many times heads was flipped 
count = coin_toss.count('heads') 
print(count) 

# remove item with slice(start, stop, step) 
fav_artists_slice = slice(0, 1) 
print(fav_artists[fav_artists_slice]) 
print(fav_artists) 

# remove item with pop(index)
print(fav_artists.pop(1))
print(fav_artists)

# change dictionary 
fav_cities['san_juan'] = 26000
print(fav_cities)

