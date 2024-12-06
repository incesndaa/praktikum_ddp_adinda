from gempa import *

print("=========INFO GEMPA 2024=========")
print("============Gempa 1==============")
gempaPertama = Gempa("Banten", 1.2)
gempaPertama.dampak()
print("============Gempa 2==============")
gempaKedua = Gempa("Palu", 6.1)
gempaKedua.dampak()
print("============Gempa 3==============")
gempaKetiga = Gempa("Cianjur", 5.6)
gempaKetiga.dampak()
print("============Gempa 4==============")
gempaKeempat = Gempa("Jayapura", 3.3)
gempaKeempat.dampak()
print("============Gempa 5==============")
gempaKelima = Gempa("Garut", 4.0)
gempaKelima.dampak()