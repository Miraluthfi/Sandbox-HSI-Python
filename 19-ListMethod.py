# Cek list ada fungtion method apa saja yang digunakan

numbers = [5, 6, 7, 8, 1]
print("----------Angka awal----------")
print(numbers)

"""
append digunakan untuk menambahkan sebuah data baru
ke list yang letak di paling belakang
"""
numbers.append(99)
print("")
print("----------Append----------")
print(numbers)

"""
insert digunakan untuk menambahkan sebuah data baru
ke list ke index sesuai perintah (index, angka)
"""
numbers.insert(2, 100)
print("")
print("----------Insert----------")
print(numbers)

"""
pop digunakan untuk menghapus item
dengan index ke berapa
"""
numbers.pop(5)
print("")
print("------------Pop-----------")
print(numbers)

"""
remove digunakan untuk menghapus item
dengan angkanya
"""
numbers.remove(8)
print("")
print("----------Remove----------")
print(numbers)

"""
sort digunakan untuk mengurutkan elemen
yang ada dalam list
"""
numbers.sort()
print("")
print("-----------Sort-----------")
print(numbers)