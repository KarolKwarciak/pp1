import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
temperatures = [int(i) for i in temperatures]
sum = sum(temperatures)/len(temperatures)
print(sum)