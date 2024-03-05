# dictonary ={key : expression for (key, value) in iterable}
# dictonary ={key : expression for (key, value) in iterable if conditional}
# dictonary ={key : (if/else) for (key, value) in iterable }
cities_in_F = {"cities":{"New York ":32,"Boston":75,"los Angles":100,"Chicago":50}}
cities_in_C ={key: round((value-32)*(5/9),2) for (key,value) in cities_in_F.items()}
print(cities_in_C)
greater_than_50 ={key:value for (key,value)in cities_in_F.items() if value >50}
# print(greater_than_50)
desc_cities ={key : (value if value >50 else "cold") for (key, value) in cities_in_F.items() }
# print(desc_cities)