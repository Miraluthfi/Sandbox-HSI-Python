"""
Modul ialah untuk mengelompokkan beberapa fungsi
Modul juga agar bisa dipakai banyak file
"""

import Matematika
from Matematika import plus #import langsung nama function

result = Matematika.plus(10, 8)
print(result)

result = Matematika.minus(10, 8)
print(result)

print("-- Import langsung nama Function --")
result = plus(10, 10)
print(result)