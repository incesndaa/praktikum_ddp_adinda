namaKendaraan = input("Nama Kendaraan : ")
jenisBensin = input("Jenis Bensin : ").lower()
kotaTujuan = input("Kota yang anda tuju : ").lower()


if jenisBensin == "pertalite":
    harga = 10000
    jarakTempuh = 12
elif jenisBensin == "pertamax":
    harga = 14000
    jarakTempuh = 13
elif jenisBensin == "pertamax turbo":
    harga = 17000
    jarakTempuh = 13.5
else:
    print("Jenis bensin tidak tersedia")

if kotaTujuan == "jakarta":
    jarak = 20
elif kotaTujuan == "bekasi":
    jarak = 35.7
elif kotaTujuan == "depok":
    jarak = 5
elif kotaTujuan == "tangerang":
    jarak = 99
elif kotaTujuan == "bogor":
    jarak = 120.6
else:
    print("Kota tujuan tidak tersedia")


pemakaianBensin = float(jarak / jarakTempuh)
totalHarga = float(pemakaianBensin * harga)

print("Nama kendaraan ", namaKendaraan)
print("Jenis bensin ", jenisBensin)
print("Kota yang dituju ", kotaTujuan)
print("Pemakaian bensin? ",  pemakaianBensin)
print("Total harga bensin ", totalHarga)




