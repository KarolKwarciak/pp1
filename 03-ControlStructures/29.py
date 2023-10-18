washing_products = input("which product do you want to wash? (jacket/shoes/underwear):").lower() 
rinse = input("Do you want to use rinse? (yes/no):").lower() == "yes"
spin = input("Do you want to use another spin? (yes/no):").lower() == "yes"


washing_times = {
    "jacket": 40,
    "shoes": 20, 
    "underwear": 70
}

rinse_time = 15 if rinse else 0
spin_time = 9 if spin else 0

Total_wash_time = washing_times.get(washing_products, 0) + rinse_time + spin_time
print(f"Total wash time ={Total_wash_time} minutes")