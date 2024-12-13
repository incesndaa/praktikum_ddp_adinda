from animal import *

class Kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenis, warnaBulu, namaPanggilan):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenis = jenis
        self.warnaBulu = warnaBulu
        self.namaPanggilan = namaPanggilan
    
    def mengeong(self):
        print(f"miaw miaw miaw aku kucing {self.jenis}, majikanku memanggil aku {self.namaPanggilan}")

    def berlari(self):
        print(f"saya kucing berwarna {self.warnaBulu} dan dapat berlari dengan cepat")

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, paruh, sayap):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.paruh = paruh
        self.sayap = sayap

    def terbang(self):
        print(f"saya burung {self.nama} terbang dengan sayap {self.sayap}")

    def berkicau(self):
        print(f"saya bisa berkicau dengan paruh {self.paruh}")

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, sirip, jenis):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.sirip = sirip
        self.jenis = jenis

    def berenang(self):
        print(f"saya adalah {self.nama} saya bisa berenang menggunakan sirip {self.sirip}")

    def bermain(self):
        print(f"saya suka bermain di perairan {self.jenis}")
