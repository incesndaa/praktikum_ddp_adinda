class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif self.skala >= 2 and self.skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6:
            print("Dampak gempa bangunan roboh")
        elif self.skala > 6:
            print("Dampak gempa bangunan roboh dan berpotensi tsunami")
        else:
            print("tidak valid")

        print("Lokasi Gempa :", self.lokasi)
        print("Skala Gempa :", self.skala)
        
        