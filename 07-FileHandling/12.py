name = "Karol Kwarciak"
University = "UEK"
field = "Applied informatics"


file = open("student.txt", "w")
file.write(name+"\n")
file.write(University+"\n")
file.write(field+"\n")

file.close()