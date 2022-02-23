"""Unpack adalah pengambilan data dari collection seperti list 
atau tuple dan membaginya menjadi nilai variabel secara individual.
"""

numbers = (1 ,2, 3)

#x = numbers[0]
#y = numbers[1]
#z = numbers[2]

#x, y, z = numbers 
#x, _, _ = numbers #variabel yang tidak digunakan dg _
x, *a = numbers # * elemen sisanya bakal ada sekaligus didalam setelah *

print("")
print(x)
print(a)