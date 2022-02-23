"""
Belajar tentang Random untuk menghasilkan angka Random
atau secara random memilih elemen/ item dalam sebuah list
"""

import random

names = ['Almira', 'Zaidan', 'Asni', 'Azis']

#random menggunakan index
print("---Random menggunakan Index-")
lower_limit = 0
upper_limit = len(names) - 1

for i in range(3):
    random_int = random.randint(lower_limit, upper_limit)
    print(random_int)
       
print("---Random mencetak angka-")
# mencetak angka random dimulai dari angka 10-30
print(random.randint(10, 30))

for index in range(5):
    print(random.randint(10, 30))

print(random.random())

