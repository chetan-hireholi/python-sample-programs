# Replace a letter by slicing
s = str(input())

replace = input().split(' ')

if int(replace[0]) < len(s):
	print(s[:int(replace[0])-1] + replace[1] + s[int(replace[0]):len(s)])