count = int(input())
num = map(int, input().split(' '))
t = tuple(num)
print(hash(t))