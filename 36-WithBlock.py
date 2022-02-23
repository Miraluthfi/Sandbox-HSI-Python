"""
Jika ada error kemudian crash dapat menggunakan
with statement kalau lupa di close/ di close 
tetapi ad file error
"""
import csv

with open("file.csv", "r") as files:
    files_csv = csv.reader(files, delimiter=",")

    for row in files_csv:
        print(f"Name : {row[0]}, Age: {row[1]}, Status : {row[-1]}")