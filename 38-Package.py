"""
Package adalah kumpulan dari kode-kode.
Package bentuknya folder
"""
import marketplace.Matematika
from marketplace import Matematika #Hanya memanggil matematika.plus saja
from marketplace.Matematika import plus, minus #Langsung memanggil plus, minus

result = marketplace.Matematika.plus(10, 8)
print(result)

print("--Hanya memanggil matematika.plus saja--")
result = Matematika.plus(10, 8)
print(result)

print("--Langsung memanggil plus--")
result = plus(10, 8)
print(result)

print("--Langsung memanggil minus--")
result = minus(10, 8)
print(result)