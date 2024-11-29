import math

def kubus(sisi):
    luas = 6*sisi**2
    print ("luas kubus dengan sisi",r,"adalah",f"{luas:.2f} cm²")

def balok(panjang, lebar, tinggi):
    luas = 2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi))
    print("luas permukaan balok dengan panjang",panjang,"lebar",lebar,"dan tinggi",tinggi, "adalah", f"{luas:2f} cm²")

def tabung(r, tinggi):
    luas = 2*math.pi*r*(r+tinggi)
    print("luas permukaan tabung dengan jari jari",r,"dan tinggi",tinggi,"adalah", f"{luas:.2f} cm²")

def bola(r):
    luas = 4*math.pi*r**2
    print("luas permukaan bola dengan jari jari",r,"adalah",f"{luas:.2f} cm²")

def limas(alas, tinggiAlas, sisi_a, sisi_b, sisi_c, tinggiSisiTegak):
    luasAlas = 0.5 * alas * tinggiAlas

    luasSisiTegak_a = 0.5 * sisi_a * tinggiSisiTegak
    luasSisiTegak_b = 0.5 * sisi_b * tinggiSisiTegak
    luasSisiTegak_c = 0.5 * sisi_c * tinggiSisiTegak
    luasSelimut = luasSisiTegak_a + luasSisiTegak_b + luasSisiTegak_c

    luasTotal = luasAlas + luasSelimut
    print(f"Luas permukaan limas adalah {luasTotal:.2f} cm²")

