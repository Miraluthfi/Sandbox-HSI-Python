"""
Bagaimana cara menghandle error?
Dengan menggunakan try dan except
"""
try:
    level = input("Your level : ")
    level = int(level)
    level = level / 0
    print(level)
    
except ZeroDivisionError:
    print("Error cannot be divided by 0 ")
    
except ValueError:
    print("What you enter is not number")