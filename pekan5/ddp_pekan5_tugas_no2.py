pilihan = int(input("""
                1. Hitung luas persegi
                2. Hitung luas Lingkaran
                3. Hitung luas Segitiga
                Pilih salah satu: 
                """))

match pilihan:
    case 1:
        print("Menghitung luas Persegi")
        sisi = int(input("masukan sisi :"))
        luas = sisi*sisi
        print(f"luas persegi = {luas} cm")
    case 2:
        print("Menghitung luas Lingkaran")
        phi = 3.14
        r = int(input("masukan jari jari :"))
        luas = phi*r**2
        print(f"luas lingkaran = {luas} cm")
    case 3:
        print("Menghitung luas Segitiga")
        a = int(input("masukan alas :"))
        t = int(input("masukan tinggi :"))
        luas = a*t/2
        print(f"luas segitiga = {luas}")
    case _ :
        print("pilihan tidak tersedia")
        