from childClassAnimal import *

# objek kucing
mila = Kucing("Kucing", "cat choize", "di darat", "melahirkan", "persia kampung", "putih", "mila")
bomber = Kucing("Kucing", "cat choize", "di darat", "melahirkan", "anggora", "putih dan coklat", "bomber")
oreo = Kucing("Kucing", "cat choize", "di darat", "melahirkan", "kampung", "hitam dan putih", "oreo")

mila.deskripsi()
print("--------------------------------------------------------------------")
bomber.mengeong()
print("--------------------------------------------------------------------")
oreo.berlari()
print("--------------------------------------------------------------------")
print("\n")

# objek burung
gagak = Burung("gagak", "pisang", "di udara", "bertelur", "sedikit melengkung", "sedang")
elang = Burung("elang", "daging", "di udara", "bertelur", "melengkung", "besar")
merpati = Burung("merpati", "biji jagung", "di udara", "bertelur", "tidak melengkung", "kecil")
print("--------------------------------------------------------------------")

gagak.deskripsi()
gagak.terbang()
gagak.berkicau()
print("--------------------------------------------------------------------")

elang.deskripsi()
elang.terbang()
elang.berkicau()
print("--------------------------------------------------------------------")

merpati.deskripsi()
merpati.terbang()
merpati.berkicau()
print("--------------------------------------------------------------------")
print("\n")

# objek ikan
lele = Ikan("Ikan Lele", "pakan ikan", "di air", "bertelur", "sirip dada", "air tawar")
hiu = Ikan("Ikan Hiu", "daging", "di air", "melahirkan", "sirip punggung", "laut dalam")
koi = Ikan("Ikan Koi", "pakan ikan", "di air", "bertelur", "sirip punggung", "air sungai")
print("--------------------------------------------------------------------")

lele.deskripsi()
lele.berenang()
lele.bermain()
print("--------------------------------------------------------------------")

hiu.deskripsi()
hiu.berenang()
hiu.bermain()
print("--------------------------------------------------------------------")

koi.deskripsi()
koi.berenang()
koi.bermain()
print("--------------------------------------------------------------------")