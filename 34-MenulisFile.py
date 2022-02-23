files = open("file.txt", "w") 
# append ialah menambahkan data baru ke sebuah file yang sudah ada isi
# write mengganti data baru dan meulis apa yang kita tulis
# mode write namun nama file belum ada, maka akan dibuat file baru
"""
print(files.readable()) #untuk tahu apakah sebuah file bisa di baca atau tidak
print(files.writable())    
"""

files.write("Instagram = miraluthfi")
 
files.close()