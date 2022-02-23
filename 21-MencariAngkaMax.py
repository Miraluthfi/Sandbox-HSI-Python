"""
function sum digunakan untuk mempermudah
penjumlahan sebuah list tanpa menggunakan for
"""

numbers = [5, 6, 7, 8, 1]

total = sum(numbers)
print(total)

"""Cara pertama mendapatkan angka yang paling besar
dengan menggunakan max"""
max_number = max(numbers)
print(max_number)

""""Cara kedua mendapatkan angka 
yang paling besar"""
numbers.sort() #mengurutkan list
max_numbers = numbers[-1]
print(max_number)

""""Cara ketiga (ribet) mendapatkan angka 
yang paling besar dengan menggunakan for"""
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
    
print(max_number)

