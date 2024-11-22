# Soal 3: Cek Usia dan Status
# Buatlah program yang meminta pengguna untuk memasukkan usia. Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18, dan "Anak-anak" jika kurang dari 18. Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 menggunakan if and.


usia = int(input("Masukkan usia Anda: "))

if usia >= 18:
    print("Dewasa")
elif usia >= 13 and usia <= 17:
    print("Remaja")
else:
    print("Anak-anak")
