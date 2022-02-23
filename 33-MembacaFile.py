"""
Bagaimana cara membaca isi dari sebuah File?
mode r = read, w = write, a = append, r+ = read + write
"""

files = open("file.txt", "r")

#print(files.read()) #membaca semua isi file
"""
print(files.readline()) 
print(files.readline()) #membaca file hanya sebaris
print(files.readline())
"""
list = files.readlines() # list dari string perbaris dari file
#print(list[2])

# mencetak satu persatu
index = 1
for file in list:
    print(f"{index} - {file}")
    index += 1
    
files.close()