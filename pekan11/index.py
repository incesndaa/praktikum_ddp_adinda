class Orang:
    #property
    # nama = "Kagura"
    # umur = 0
    # jk = ""

    def __init__(self, nama, umur, jk):
        self.nama = nama
        self.umur = umur
        self.jk = jk
    #method
    def ngomong(self):
        print("saya bisa bicara karena saya", self.jk)
    
    def jalan(self):
        print("saya bisa berjalan karena saya", self.nama)