import json

def f(years, course):
    with open("data.json") as file:
        count = 0
        data = json.load(file)

        for student in data:
            age = student.get("age", 0)
            courses = student.get("studies", {}).get("courses", [])

            if age >= years:
                for c in courses:
                    if c["name"] == course and all(grade >= 4 for grade in c.get("grades", [])):
                        count += 1
                        break 

    return count

print(f(21, "statistics"))
