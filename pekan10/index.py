import luasBangunDatar as lbd, luasBangunRuang as lbr

pilihan = int(input("""
                1. Hitung luas bangun datar
                2. Hitung luas bangun ruang
                Pilih salah satu: 
                """))

if pilihan == 1:
    bd = int(input("""
                Pilih bangun datar yang ingin dihitung luasnya
                1. Persegi
                2. Persegi Panjang
                3. Segitiga
                4. Lingkaran
                5. JajarGenjang
                Pilih salah satu: 
                """))
    
    match bd:
        case 1:
            print("Menghitung Luas Persegi")
            s = float(input("Masukan Sisi :"))
            lbd.persegi(s)
        case 2:
            print("Menghitung Luas Persegi Panjang")
            p = float(input("Masukan Panjang : "))
            l = float(input("Masukan Lebar : "))
            lbd.persegiPanjang(p,l)
        case 3:
            print("Menghitung Luas segitiga")
            a = float(input("Masukan Alas : "))
            t = float(input("Masukan Tinggi : "))
            lbd.segitiga(a,t)
        case 4:
            print("Menghitung Luas Lingkaran")
            r = float(input("Masukan Jari-jari : "))
            lbd.lingkaran(r)
        case 5:
            print("Menghitung Luas JajarGenjang")
            a = float(input("Masukan Alas : "))
            t = float(input("Masukan Tinggi : "))
            lbd.jajarGenjang(a,t)

elif pilihan == 2:
    br = int(input("""
                Pilih bangun ruang yang ingin dihitung luas permukaannya
                1. Kubus
                2. Balok
                3. Tabung
                4. Bola
                5. Limas Segitiga
                Pilih salah satu: 
                """))
    
    match br:
        case 1:
            print("Menghitung Luas Permukaan Kubus")
            s = float(input("Masukan Sisi :"))
            lbr.kubus(s)
        case 2:
            print("Menghitung Luas Permukaan Balok")
            p = float(input("Masukan Panjang : "))
            l = float(input("Masukan Lebar : "))
            t = float(input("Masukan Tinggi : "))
            lbr.balok(p,l,t)
        case 3:
            print("Menghitung Luas Permukaan Tabung")
            r = float(input("Masukan Jari-jari : "))
            t = float(input("Masukan Tinggi : "))
            lbr.tabung(r,t)
        case 4:
            print("Menghitung Luas Permukaan Bola")
            r = float(input("Masukan Jari-jari : "))
            lbr.bola(r)
        case 5:
            print("Menghitung Luas Permukaan Limas Segitiga")
            alas = float(input("Masukkan panjang alas segitiga : "))
            tinggiAlas = float(input("Masukkan tinggi segitiga : "))
            sisi_a = float(input("Masukkan panjang sisi a segitiga : "))
            sisi_b = float(input("Masukkan panjang sisi b segitiga : "))
            sisi_c = float(input("Masukkan panjang sisi c segitiga : "))
            tinggiSisiTegak = float(input("Masukkan tinggi sisi tegak : "))
            lbr.limas(alas, tinggiAlas, sisi_a, sisi_b, sisi_c, tinggiSisiTegak)

else:
    print("tidak valid")



