# To create the below pattern:
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

import string
a = string.ascii_lowercase
print(a[2].center(9,"-"))
print((a[2]+"-"+a[1]+"-"+a[2]).center(9,"-"))
print((a[2]+"-"+a[1]+"-"+a[0]+"-"+a[1]+"-"+a[2]).center(9,"-"))

N = 5
for i in range(N-1,-1,-1):
	print(a[i].center((N*3),"-"))
	print((a[i]+"-"+a[i-1]+"-"+a[i]).center(9,"-"))
	break

