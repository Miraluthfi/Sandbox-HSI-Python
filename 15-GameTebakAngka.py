# Menggabungkan while, if dan ditambah break untuk memaksa perulangan berhenti
trying = 0
secret_number = 7
limit = 3

while trying < limit:
    guess_number = input("Enter numbers (1-9) : ")
    guess_number = int(guess_number)
    
    if guess_number == secret_number:
        print("Congrats!, You Win")
        break
    
    trying += 1