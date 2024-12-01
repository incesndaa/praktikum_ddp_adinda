import math

def kubus(sisi):
    luas = 6*sisi**2
    return luas

def balok(panjang, lebar, tinggi):
    luas = 2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi))
    return luas

def tabung(r, tinggi):
    luas = 2*math.pi*r*(r+tinggi)
    return luas

def bola(r):
    luas = 4*math.pi*r**2
    return luas

def limas(alas, tinggiAlas, sisi_a, sisi_b, sisi_c, tinggiSisiTegak):
    luasAlas = 0.5 * alas * tinggiAlas

    luasSisiTegak_a = 0.5 * sisi_a * tinggiSisiTegak
    luasSisiTegak_b = 0.5 * sisi_b * tinggiSisiTegak
    luasSisiTegak_c = 0.5 * sisi_c * tinggiSisiTegak
    luasSelimut = luasSisiTegak_a + luasSisiTegak_b + luasSisiTegak_c

    luasTotal = luasAlas + luasSelimut
    return luasTotal
    

