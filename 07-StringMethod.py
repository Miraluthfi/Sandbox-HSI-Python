# fungsi-fungsi di string
course = "belajar python bareng almiraluthfi"
course_capital = course.upper()
length = len(course)
language = "python"

print("")
print(language in course)
print("--------------------------")
print("length : " + str(length)) # jumlah panjang
print("upper : " + course_capital)
print("replace : " + course.replace("python", "javascript")) # mengganti kalimat

# method
print("")
print("----------Method----------")
print("upper : " + course.upper()) # mengubah kalimat menjadi kapital
print("lower : " + course.lower()) # mengubah kalimat menjadi kecil
print("capitalize : " + course.capitalize()) # mengubah hanya bagian depan awal kalimat menjadi kapital
print("title : " + course.title()) # mengubah semua awal kalimat menjadi kapital (seperti judul)