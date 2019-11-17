
def HandleInsert(l):
	print("Enter the position and the item to be inserted : ")
	posAndVal = input().split(' ')
	l.insert(int(posAndVal[0]), int(posAndVal[1]))
	print(l)


def HandlePrint(l):
	print("printing l ")
	print(l)


def HandleRemove(l):
	print("Enter the item to be removed : ")
	itemToBeDeleted = int(input())
	l.remove(itemToBeDeleted)
	print("deleted item " + str(itemToBeDeleted) + "from the list")
	HandlePrint(l)


def HandleAppend(l):
	print("Enter the item to be appended: ")
	itemToBeAppended = int(input())
	l.append(itemToBeAppended)
	print("Item " + str(itemToBeAppended) + "has been appended")
	HandlePrint(l)


def HandleSort(l):
	print("Sorting the list ")
	l.sort()
	HandlePrint(l)


def HandlePop(l):
	print("Popping the last element ")
	l.pop()
	HandlePrint(l)


def HandleReverse(l):
	print('Reversing the list')
	l.reverse()
	HandlePrint(l)

l = []

print("Enter the no of command you wanna execute  :")
n = int(input())

for i in range(0, n):
	print("Enter command : ")
	command = input()
	if command == 'insert':
		HandleInsert(l)

	elif command == 'print':
		HandlePrint(l)

	if command == 'remove':
		HandleRemove(l)

	if command == 'append':
		HandleAppend(l)
	

	if command == 'pop':
		HandlePop(l)

	if command == 'sort':
		HandleSort(l)

	if command == 'reverse':
		HandleReverse(l)


