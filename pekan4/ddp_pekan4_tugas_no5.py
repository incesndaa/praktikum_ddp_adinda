# Soal 5: Pembelian Diskon
# Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
# example : 
# minyak 25.000, indomie 5.000, beras 75.000, gula 25.000, kopi 20.000, teh 10.000

minyak = 25000
indomie = 5000 
beras = 75000 
gula = 25000 
kopi = 20000 
teh = 10000

jumlahPembelianMinyak = int(input("Masukkan jumlah minyak : "))
jumlahPembelianIndomie = int(input("Masukkan jumlah indomie : "))
jumlahPembelianBeras = int(input("Masukkan jumlah beras : "))
jumlahPembelianGula = int(input("Masukkan jumlah gula : "))
jumlahPembelianKopi = int(input("Masukkan jumlah kopi : "))
jumlahPembelianTeh = int(input("Masukkan jumlah teh : "))

totalHarga = (jumlahPembelianMinyak * minyak) + \
             (jumlahPembelianIndomie * indomie) + \
             (jumlahPembelianBeras * beras) + \
             (jumlahPembelianGula * gula) + \
             (jumlahPembelianKopi * kopi) + \
             (jumlahPembelianTeh * teh)
diskon = 0.1

totalDiskon = totalHarga*diskon if(jumlahPembelianMinyak + jumlahPembelianIndomie + 
                                    jumlahPembelianBeras + jumlahPembelianGula + 
                                    jumlahPembelianKopi + jumlahPembelianTeh) > 100 else 0
totalHarga -= totalDiskon

print(f"diskon yg anda dptkan sebesar 10% Rp {totalDiskon}" if totalDiskon > 0 else "tidak ada diskon")
print("total harga: Rp", totalHarga)

