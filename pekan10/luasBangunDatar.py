import math

def persegi(sisi):
    luas = sisi*sisi
    print("luas persegi dengan sisi",sisi," = ",luas)

def persegiPanjang(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang dengan panjang",panjang,"dan lebar",lebar,"=",luas)

def segitiga(alas, tinggi):
    luas = 1/2*alas*tinggi
    print("luas segitiga dengan alas",alas,"dan tinggi",tinggi,"=",luas)

def lingkaran(r):
    luas = math.pi*r**2
    print("luas lingkaran dengan jari jari",r,"=",luas)
    
def jajarGenjang(alas, tinggi):
    luas = alas*tinggi
    print("luas jajargenjang dengan alas",alas,"dan tinggi",tinggi,"=",luas)