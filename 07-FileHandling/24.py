import csv
with open("studentlist.csv", "r") as file:
   reader = csv.DictReader(file)
   for rows in reader:
      if int(rows["age"]) < 30:
         print(f"\n{rows['first_name']}  {rows['last_name']}  {rows['email']}")