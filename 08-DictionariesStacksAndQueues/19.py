import json
with open("limited.json","r") as file:
    data = json.load(file)

limited_data  = []
for i in data:
    i = {
        "name":i['name'],
        "surname":i['surname'],
        "student ID":i['student ID']
    }
    limited_data.append(i)

limited_file = open("students.txt","w")
json.dump(limited_data, limited_file, indent=2)
limited_file.close()

    

