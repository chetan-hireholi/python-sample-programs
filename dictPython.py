# Find the avg marks
dict = {}
for i in range(0, int(input("Enter number of students : "))):
	name = str(input("Enter name : "))
	Phy = float(input("Enter Phy marks : "))
	Math = float(input("Enter Math marks : "))
	Chem = float(input("Enter Chem marks : "))
	dict[name] = [Phy,Math,Chem]

result = str(input("Enter the name to calculate avg : "))

if result in dict:
	print("Found the user.")
	marks = dict[result]
	avg = sum(marks)/len(marks)

print(float("{0:.2f}".format(avg)))