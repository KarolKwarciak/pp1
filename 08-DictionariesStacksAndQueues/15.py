basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}
dict = {

}
for key,value in basic_data.items():
    dict[key] = value
for key,value in advanced_data.items():
    dict[key] = value
print(dict)