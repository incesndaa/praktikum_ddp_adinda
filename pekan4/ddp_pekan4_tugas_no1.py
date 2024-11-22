# Soal 1: Bilangan Genap atau Ganjil
# Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.

number = int(input("Masukkan Angka : "))

if number % 2 == 0 :
    print(number, "adalah bilangan genap")
else :
    print(number, "adalah bilangan ganjil")
