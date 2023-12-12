def f(subjects):
    list = []
    for key,value in subjects.items():
        a = sum(value)/len(value)
        list.append(a)
        b = max(list)
    for key,value in subjects.items():
        if sum(value)/len(value) == b:
            return key
print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))






#dict = ({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})
#list = []
#for key,value in dict.items():
 #   a = ((sum(value)/len(value)))
 #   list.append(a)
 #   b = max(list)
#for key,value in dict.items():
 #   if sum(value)/len(value) == b:
  #      print(key)
