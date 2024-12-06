class Bank:
    noRek = ""
    nama = ""
    saldo = 0
    jumlahNasabah = 0
    BANK = "Bank Adinda" 
    
    def __init__(self,no,nasabah,saldo):
        self.noRek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jumlahNasabah += 1

    def nabung(self,uang):
        self.saldo += uang
        
    def tarik(self,uang):
        self.saldo -= uang

    def cetak(self):
        print(Bank.BANK,
            "\n==========================",
            "\nNo. Rekening\t:",self.noRek,
            "\nNama Nasabah\t:",self.nama,
            "\nSaldo\t\t: Rp. ",format(self.saldo, ","),
            "\n==========================-"
            )