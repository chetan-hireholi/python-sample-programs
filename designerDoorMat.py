# To produce the below output:
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------Welcome----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

input = input().split(' ')
N = int(input[0])
M = int(input[1])
s = ".|."
w = "Welcome"
for i in range(1,N):
	if i % 2 != 0:
		c = s * i
		print(c.center(M,"-"))
print(w.center(M,"-"))
for i in range(N-1,-1,-1):
	if i % 2 != 0:
		c = s * i
		print(c.center(M,"-"))