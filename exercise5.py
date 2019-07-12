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

# sum all the cities population 
fav_cities = sum(fav_cities.values())
print(fav_cities)

# show message depending on age 
for name, age in friends.items(): 
    if age >= 21: 
        old = 'old'
        print(f'{name} is {old}')
    else:  
        young = 'young'
        print(f'{name} is {young}')

# print the last two colours 
print(fav_colors[-2:])

# add 1 to everyones age 
for age in siblings_age: 
    age += 1
    print(age)

# add two colors to the fav_color list 
fav_colors.extend(['yellow', 'teal'])
print(fav_colors)

