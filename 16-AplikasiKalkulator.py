# Aplikasi Kalkulator

# (+ - * / exit)
command = ""

while command != "exit":
    command = input("Command : ")

    if command == "exit":
        break
    
    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Sorry, Command is not recognized")
        continue # memaksa jalannya program didalam while akan balik ek perulangan lagi tanpa menjalankan kode di bawah

    a = int(input("First Number : "))
    b = int(input("Second Number : "))
    
    if command == "+":
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b
        
    print(f"Result : {result}")
print("Thank you for using this application^^")