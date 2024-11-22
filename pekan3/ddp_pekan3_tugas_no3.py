jk = input("Masukkan jenis kelamin (pria/wanita) : ").lower()
tb = float(input("Masukkan tinggi badan : "))

if jk == "pria":
    rumus = int((tb - 100) - ((tb - 100) * 10/100))
elif jk == "wanita":
    rumus = int((tb - 100) - ((tb - 100) * 15/100))
else:
    rumus = None

if rumus is not None:
    print("Berat badan ideal Anda adalah:", rumus, "kg")
else:
    print("Jenis kelamin tidak valid.")
