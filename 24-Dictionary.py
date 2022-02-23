"""
Dictionary adalah sebuah struktur data yang bisa
menyimpan data dalam bentuk key (kunci) dan value (nilai)  
"""

user = {
    "name": "Almiraluthfi Pratiwi",
    "age": 21,
    "is_admin": True
}

user["username"] = "almiraluthfi_22"
user["name"] = "Almiraluthfi P"

# agar tidak terjadi error ketika tidak ada key, dia mencetak tipe data none
temp = user.get("username", "Almiraluthfi") #tidak mencetak none lagi karena sudah ada paramter string ini
temp = user.get("name") 


name = user["name"]
age = user["age"]

print(age)
print(temp)
