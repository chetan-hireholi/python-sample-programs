# List Operations

l = []
n = int(input("Enter the # of iterations: "))

for i in range(0, n):
	ins = input().split(' ')
	if "insert" in ins:
		l.insert(int(ins[1]), int(ins[2]))
	elif "print" in ins:
		print(l)
	elif "remove" in ins:
		l.remove(int(ins[1]))
	elif "append" in ins:
		l.append(int(ins[1]))
	elif "sort" in ins:
		l.sort()
	elif "pop" in ins:
		l.pop()
	elif "reverse" in ins:
		l.reverse()