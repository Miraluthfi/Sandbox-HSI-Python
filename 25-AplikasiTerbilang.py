# Membuat program mengubah angka menjadi angka terbilang

numbers = input("Enter numbers : ")

numbers_mapping = {
    "1": "Satu",
    "2": "Dua",
    "3": "Tiga",
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan",
}

output = ""

for n in numbers:
    counted = numbers_mapping.get(n, "Invalid")
    
    output = output+ counted + " "

print(output)