class Phone():
    def __init__ (self,brand,number,year,applications):
        self.brand = brand
        self.number = number
        self.year = year
        self.Turn_off = True
        self.current_application = 1
    def Turn_on(self):
        self.Turn_off = False
    def Turn_off(self):
        self.Turn_off = True
    def add_application(self,application):
        self.current_application = application

phone = Phone(
    "Xiaomi","793 234 544", "2019",11)
print(f"My phone brand is {phone.brand}\n",end = "")
print(f"My phone number is {phone.number}\n", end = "")
print(f"My phone comes from the year {phone.year}")

phone.Turn_on()
phone.add_application(15)

if phone.Turn_on:
    print(f"My phone is currently turned on")
else:
    print(f"My phone is currently turned on")
print(f"My phone has {phone.add_application} applications")
