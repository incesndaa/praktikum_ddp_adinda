namaPembeli = input("masukan nama : ")
noHP = input("masukan no HP: ")
menu = input("pesan apa? ").lower()

if menu == "makanan" :
    print("""
        menu makanan
          nasi goreng -> Rp.15.000
          mie goreng -> Rp.12.000
          ayam geprek -> Rp.18.000
    """)
elif menu == "minuman":
    print("""
        menu minuman
          aneka jus -> Rp.15.000
          soft drink -> Rp.10.000
          sweet ice tea -> Rp.5.000
    """)
else:
    print("tidak tersedia")

pesanan = input("masukan pesanan : ").lower()
jumlahPesanan = int(input("masukan jumlah pesanan :"))

if pesanan == "nasi goreng":
    harga = 15000
elif pesanan == "mie goreng":
    harga = 12000
elif pesanan == "ayam geprek":
    harga = 18000
elif pesanan == "aneka jus":
    harga = 15000
elif pesanan == "soft drink":
    harga = 10000
elif pesanan == "sweet ice tea":
    harga = 5000
else:
    print("tidak tersedia")

totalHarga = int(harga * jumlahPesanan)

print("Nama pembeli :", namaPembeli)
print("Nomor HP :", noHP)
print("Menu yang dipesan :", pesanan)
print("Jumlah Pesanan :",  jumlahPesanan)
print("Harga yang dibayar :", totalHarga)

