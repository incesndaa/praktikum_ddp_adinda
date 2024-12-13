class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def berjalan(self):
        if self.gender == "laki-laki":
            print(f"{self.name} bisa berjalan karena dia {self.gender}")
        else:
            print(f"{self.name} tidak bisa berjalan karena dia {self.gender}")

    def berbicara(self):
        print(f"{self.name} bisa berbicara")


class Supir(Person):
    def __init__(self, name, age, gender, sim):
        super().__init__(name, age, gender)
        self.sim = sim

    def mengendarai(self):
        print(f"{self.name} bisa mengendarai karena pekerjaannya supir")

class Mahasiswa(Person):
    def __init__(self, name, age, gender, nim):
        super().__init__(name, age, gender)
        self.nim = nim
    
    def belajar(self):
        print(f"{self.name} sedang belajar karena dia mahasiswa")

angel = Supir("angel", 18, "perempuan", "012198228")
angel.mengendarai()
angel.berjalan()

dinda = Mahasiswa("dinda", 18, "perempuan", "0110224052")
dinda.belajar()

tiara = Person("tiara", 25, "perempuan")
tiara.berbicara()