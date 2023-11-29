import json
student = {
    "Name":"Karol",
    "Surname":"Kwarciak",
    "Year":{"leading":"Samuel.L.Jackson","supporting":"Kurt Russel"},
    "Semester":False,
    "":"QUentin Tarantino"
}
file = open("favourite.json","a")
json.dump(student,file,indent = 6)

file.close()