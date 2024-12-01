import math

def persegi(sisi):
    luas = sisi*sisi
    return luas

def persegiPanjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def segitiga(alas, tinggi):
    luas = 0.5*alas*tinggi
    return luas

def lingkaran(r):
    luas = math.pi*r**2
    return luas
    
def jajarGenjang(alas, tinggi):
    luas = alas*tinggi
    return luas
    