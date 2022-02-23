# Membaca CSV
# Fitur mengimport data 
# CSV adalah file yang dipisahkan dengan tanda koma
import csv

files = open("file.csv", "r")

#delimiter >> antar kolom dipisahkan oleh tanda apa

files_csv = csv.reader(files, delimiter=",")

print(files_csv)

# perulangan mendapatkan data setiap baris dalam bentuk array/list
for row in files_csv:
    #print(row) -> ini hanya menampilkan dalam bentuk array
    print(f"Name : {row[0]}, Age: {row[1]}, Status : {row[-1]}")

files.close()