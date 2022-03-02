import random

bank_soal = [{"soal": "Menurut bahasa definisi puasa adalah..... ", 
         "opsi" : { "A.": "sikap menerima dengan lapang dada", "B.": "menahan diri dari sesuatu", "C.": "mengendalikan diri dari sesuatu", "D.": "berserah diri kepada Allah"}, 
         "kunci" :{"B." : "menahan diri dari sesuatu"}},
         
         {"soal": "Niat termasuk salah satu dari..... ", 
        "opsi" : { "A.": "syarat sah puasa", "B.": "anjuran puasa", "C.": "rukun puasa", "D.": "sunnah puasa"}, 
        "kunci" : {"A.": "syarat sah puasa"}},
             
         {"soal": "Salah satu syarat sah puasa Ramadhan adalah..... ", 
         "opsi" : { "A." : "melafadzkan niat dimalam Ramadhan", "B.": "sahur dengan kurma", "C.": "suci dari haid dan nifas", "D.": "orang yang sudah baligh"}, 
         "kunci" :{"C." : "suci dari haid dan nifas"}},
             
        {"soal": "Puasa Ramadhan hukumnya adalah..... ", 
         "opsi" : { "A.": "sunnah", "B.": "mubah", "C.": "wajib", "D.": "makruh"}, 
         "kunci" :{"C." : "wajib"}},
             
        {"soal": "Jika tidak terlihat hilal maka disyariatkan menyempurnakan bulan Sya'ban..... ",
         "opsi" : { "A.": "28 hari", "B.": "20 hari", "C.": "29 hari", "D.": "30 hari"}, 
         "kunci" : {"D.": "30 hari"}}
]

print("----- Evaluasi Harian HSI -----")
print("")
print("Jumlah Soal : 2")
print("Pilih satu jawaban yang paling tepat!")

pilih = input("Saya siap mengerjakan dengan jujur (y/n)?")
if pilih == "y" or "Y": 
     
    no = 0
    totalskor = 0
    for bs in random.sample(bank_soal, 2):   
        print("")
        no += 1  
        print("{}. {}".format(no, bs["soal"]))
        
        for key, value in bs["opsi"].items():
           print(key, value)

                
        skor = 0
        pilihan = input("Masukkan Jawaban Anda (A/B/C/D): ")
        
        for key, value in bs["kunci"].items():
            print(key, value)
            if pilihan == key:
                print("Thoyyib, Jawaban Anda Benar!")
                skor +=2
                print("Skor : ",skor)
            
            else:
                print("Afwan, Jawaban Anda Salah")
                skor +=1
                print("Skor : ",skor)
            totalskor = totalskor+skor
    
print("")
print("----- Alhamdulillah, Evaluasi Harian Selesai -----")
print("Total Skor Anda :", totalskor)
print("Barakallahu fiikum ^-^")
print("")
