import luasBangunDatar as lbd, luasBangunRuang as lbr, modulAritmatika as ma

pilihan = int(input("""
                1. Hitung luas bangun datar
                2. Hitung luas bangun ruang
                3. Hitung Aritmatika
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
            print("luas persegi dengan sisi",s," = ",lbd.persegi(s))
        case 2:
            print("Menghitung Luas Persegi Panjang")
            p = float(input("Masukan Panjang : "))
            l = float(input("Masukan Lebar : "))
            print("luas persegi panjang dengan panjang",p,"dan lebar",l,"=",lbd.persegiPanjang(p,l))
        case 3:
            print("Menghitung Luas segitiga")
            a = float(input("Masukan Alas : "))
            t = float(input("Masukan Tinggi : "))
            print("luas segitiga dengan alas",a,"dan tinggi",t,"=",lbd.segitiga(a,t))
        case 4:
            print("Menghitung Luas Lingkaran")
            r = float(input("Masukan Jari-jari : "))
            print("luas lingkaran dengan jari jari",r,"=",lbd.lingkaran(r))
        case 5:
            print("Menghitung Luas JajarGenjang")
            a = float(input("Masukan Alas : "))
            t = float(input("Masukan Tinggi : "))
            print("luas jajargenjang dengan alas",a,"dan tinggi",t,"=",lbd.jajarGenjang(a,t))
            
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
            print("luas kubus dengan sisi",s,"adalah",f"{lbr.kubus(s):.2f} cm²")
            
        case 2:
            print("Menghitung Luas Permukaan Balok")
            p = float(input("Masukan Panjang : "))
            l = float(input("Masukan Lebar : "))
            t = float(input("Masukan Tinggi : "))
            print("luas permukaan balok dengan panjang",p,"lebar",l,"dan tinggi",t, "adalah", f"{lbr.balok(p,l,t):2f} cm²")
            
        case 3:
            print("Menghitung Luas Permukaan Tabung")
            r = float(input("Masukan Jari-jari : "))
            t = float(input("Masukan Tinggi : "))
            print("luas permukaan tabung dengan jari jari",r,"dan tinggi",t,"adalah", f"{lbr.tabung(r,t):.2f} cm²")
            
        case 4:
            print("Menghitung Luas Permukaan Bola")
            r = float(input("Masukan Jari-jari : "))
            print("luas permukaan bola dengan jari jari",r,"adalah",f"{lbr.bola(r):.2f} cm²")
            
        case 5:
            print("Menghitung Luas Permukaan Limas Segitiga")
            alas = float(input("Masukkan panjang alas segitiga : "))
            tinggiAlas = float(input("Masukkan tinggi segitiga : "))
            sisi_a = float(input("Masukkan panjang sisi a segitiga : "))
            sisi_b = float(input("Masukkan panjang sisi b segitiga : "))
            sisi_c = float(input("Masukkan panjang sisi c segitiga : "))
            tinggiSisiTegak = float(input("Masukkan tinggi sisi tegak : "))
            print(f"Luas permukaan limas adalah {lbr.limas(alas, tinggiAlas, sisi_a, sisi_b, sisi_c, tinggiSisiTegak):.2f} cm²")
            

elif pilihan == 3:
    hitung = int(input("""
                Pilih perhitungan aritmatika
                1. Pertambahan
                2. Perkurangan
                3. Perkalian
                4. Pembagian
                5. Pemangkatan
                Pilih salah satu: 
                """))
    
    match hitung:
        case 1:
            print("Menghitung Pertambahan")
            a = float(input("Masukan Angka Pertama :"))
            b = float(input("Masukan Angka Kedua :"))
            print("hasil tambah dari",a,"+",b,"=", ma.tambah(a,b))
            
        case 2:
            print("Menghitung Perkurangan")
            a = float(input("Masukan Angka Pertama :"))
            b = float(input("Masukan Angka Kedua :"))
            print("hasil pengurangan dari",a,"-",b,"=",ma.kurang(a,b))
            
        case 3:
            print("Menghitung Perkalian")
            a = float(input("Masukan Angka Pertama :"))
            b = float(input("Masukan Angka Kedua :"))
            print("hasil perkalian dari",a,"x",b,"=",ma.kali(a,b))
           
        case 4:
            print("Menghitung Pembagian")
            a = float(input("Masukan Angka Pertama :"))
            b = float(input("Masukan Angka Kedua :"))
            print("hasil pembagian dari",a,":",b,"=",ma.bagi(a,b))
        case 5:
            print("Menghitung Pemangkatan")
            a = float(input("Masukan Angka Pertama :"))
            b = float(input("Masukan mau pangkat berapa :"))
            print("hasil pemangkatan dari",a,"^",b,"=",ma.pangkat(a,b))

else:
    print("tidak valid")



