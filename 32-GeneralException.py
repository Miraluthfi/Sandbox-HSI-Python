"""
Bagaimana ketika ada error
tipe except ditangkap secara general
"""
from ast import excepthandler


try:
    level = input("Your level : ")
    level = int(level)
    level = level / 0
    print(level)
    
except:
    print("There is an error")