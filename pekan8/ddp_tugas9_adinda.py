print("---Nomor 1---")
def celciusKeFahrenheit(suhuCelcius):
    konversi = (suhuCelcius * 9/5) + 32
    return konversi

print(celciusKeFahrenheit(0))
print(celciusKeFahrenheit(100))

print("---Nomor 2---")
def isGenap(bilanganBulat):
    if bilanganBulat % 2 == 0 :
        return True
    else :
        return False

print(isGenap(8))
print(isGenap(3))

print("---Nomor 3---")
def nilai(keterangan):
    if keterangan >= 80:
        print("Lulus")
    elif keterangan <= 60:
        print("Gagal")

nilai(80)
nilai(60)

print("---Nomor 4---")
def bilangan(n):
    return[i for i in range(1, n, 2)]

print(bilangan(20))
