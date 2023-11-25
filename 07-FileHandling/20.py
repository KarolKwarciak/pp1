with open("GrainsAndBread.txt") as file:
    with open("MeatAndFish.txt") as file_2:
        og_file = open("allproducts.txt", "a")
        og_file.write(file.read())
        og_file.write(file_2.read())
        og_file.close()


