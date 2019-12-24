name = input("Enter full name: ")
sname = name.split(" ")
n = "" #declaring empty string
for i in sname:
	n += str(i.capitalize()) + " "
	
print(n)