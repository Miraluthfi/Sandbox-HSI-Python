# Mentranslate sebuah character menjadi emoticon

message = input(">>> ")

emoji_mapping = {
    ":)": "😊",
    ":D": "😄",
    ":|": "😐"
}

words = message.split(" ") # sebuah list dipecah dengan ada spasi

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "
    
print(output) 