# Soal 4: Cek Keanggotaan
# Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon". Gunakan if or.

status = input("Masukkan Status Keanggotaan : ").lower()

if status == "gold" or status == "silver":
    print("Selamat! Anda mendapat diskon")
else :
    print("Tidak mendapat diskon")

