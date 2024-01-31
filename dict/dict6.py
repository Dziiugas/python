komanda = {
    'Jonas' : 12,
    'Tadas' : 15,
    'Rimas' : 25,
    'Pranas' : 23,
    'Arunas' : 14
}
pagalVarda = dict(sorted(komanda.items()))
print(pagalVarda)
print(sorted(komanda))
#pagalTaskus = dict(sorted(komanda.items(), key = lambda))



cities = [
    {
        "name": "new york city",
        "country": "USA",
        "population": 20.14,
        "area": 1223.59
    }
]

cities1 = sorted(cities, key=lambda city: city["population"])
print(cities1)

sorted_cities = dict(sorted(cities.items(), key=lambda city: city[1]["population"], reverse=True))
print(sorted_cities)