from bank import *

arya = Bank('001','Arya',700000000000)
floryn = Bank('007','Floryn',5500000)
angela = Bank('010','Angela',8000000)
badang = Bank('011','Muhammad Badang', 11000000)

arya.nabung(2000000)
angela.nabung(1000000)
floryn.tarik(2000000)
angela.tarik(6000000)

arya.cetak()
floryn.cetak()
angela.cetak()
badang.cetak()
print("Jumlah Nasabah: %i orang" %Bank.jumlahNasabah)