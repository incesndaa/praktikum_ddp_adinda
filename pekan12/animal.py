class Animal:
    def __init__(self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    
    def deskripsi(self):
        print(f"Nama Hewan : {self.nama} \nMakanan : {self.makanan} \nHidup : {self.hidup} \nBerkembangbiak : {self.berkembangBiak}" )
