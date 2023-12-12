#def hotel_list(hotels):
 #   return ",".join(map(str,hotels))
#count = 0

#a = ["sky", "Metropol", "New Port"]
#print(hotel_list(a))
#def avg_price(hotels):
 #   count = 0
  #  for i in hotels:
   #     count += i
    #return count/len(hotels)
#b = [2500,1000,1500]
#print(avg_price(b))

Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
count = 0
list = []
for i in Hotels_in_Krakow:
    list.append(i["name"])
print(f"Hotels in Krakow: {",".join(map(str,list))}")


for i in Hotels_in_Krakow:
    count += i["price"]
print(f"Average hotel price in Krakow: {count}")


count1 = 0
list = []
for i in hotels_in_Sopot:
    list.append(i["name"])
print(f"Hotels in Sopot: {",".join(map(str,list))}")


for i in hotels_in_Sopot:
    count1 += i["price"]
print(f"Average hotel price in Sopot: {count1}")


if count1 > count:
    print("Cheaper hotels in: Krakow")
elif count < count1:
    print("Cheaper hotels in: Sopot")




    
