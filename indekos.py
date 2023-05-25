from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, luas_tanah=0, kap_listrik=0):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.luas_tanah = luas_tanah
        self.kap_listrik = kap_listrik

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos dengan luas tanah (" + str(self.luas_tanah) + " satuan luas) dan kapasitas listrik sebesar (" + str(self.kap_listrik) + " VA)."