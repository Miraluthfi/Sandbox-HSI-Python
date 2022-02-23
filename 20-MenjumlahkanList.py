"""Memanfaatkan list untuk mencari nilai sum 
dari penjumlahan elemen di dalam list
"""
numbers = [5, 6, 7, 8, 1]

init_number = 0
for number in numbers:
    init_number = init_number + number
    
print(init_number)