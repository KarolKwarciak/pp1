import csv
with open("studentlist.csv", "r") as file:
   reader = csv.DictReader(file)
   for i in reader:
      if int(i["age"]) < 30:
         print(f"\n{i['first_name']}  {i['last_name']}  {i['email']}")