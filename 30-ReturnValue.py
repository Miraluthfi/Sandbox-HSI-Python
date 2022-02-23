"""
Return Statement adalah nilai yang dikembalikan
dari operasi sebuah fungsi
"""
# contoh kurang bagus
"""
def halo_user(name, level):
    print(f"Halo {name} - {level}")
    print("Selamat Belajar Python")
    return 100

temp = halo_user("Almira", 10) #mengembalikan sebuah nilai
print(temp)
"""

def multiply(a, b):
    #result = a * b
    #return result
    return a * b # lebih singkat

result = multiply(2, 10)
print(result) #hasil yang diinginkan = 2 * 10 = 20


# nilai kembalian dari sebuah fungsi adalah none (tidak menghasilkan apa")
# di fungsi ada input >> proses >> output