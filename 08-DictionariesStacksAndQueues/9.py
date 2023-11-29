countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Brazil", "population":20000000},
    {"name":"Argentina", "population":15000000},
    {"name":"Spain", "population":47000000},
    {"name":"Germany", "population":83000000}
]
print(f'{"COUNTRY":10}{"POPULATION":10}')
i = 0
while i != len(countries):
    print(f'{countries[i]["name"]:10}{countries[i]["population"]:<10}')
    i += 1

 


