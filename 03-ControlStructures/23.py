human_years = float(input("Enter your dog's age in human years: "))

if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4

print(f"Your dog's age in dog years is: {dog_years}")