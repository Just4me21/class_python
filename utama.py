class keluarga:
    def __init__(self, nama, peran, jenis_kelamin, usia):
        self.nama = nama
        self.peran = peran
        self.jenis_kelamin = jenis_kelamin
        self.usia = usia

class Matakuliah:
    def __init__(self, nama_matakuliah, dosen, sks, grade):
        self.nama_matakuliah = nama_matakuliah
        self.dosen = dosen
        self.sks = sks
        self.grade = grade

class Pasien:
    def __init__(self, nama, jenis_kelamin, keluhan, tanggal_datang, jam_kedatangan):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.keluhan = keluhan
        self.tanggal_datang = tanggal_datang
        self.jam_kedatangan =jam_kedatangan

class Menu:
    def __init__(self, menu, jenis, harga):
        self.menu = menu
        self.jenis = jenis
        self.harga = harga

class Lingkaran:
    def __init__(self,jari_jari):
        self.jari_jari = jari_jari

    def keliling(self):
        return 2 * 3,14 * self.jari_jari
   
    def luas(self):
        return 3,14 * self.jari_jari ** 2

class persegipanjang:
    def __init__(self,pjg,lbr):
        self.pjg = pjg
        self.lbr = lbr

    def keliling(self):
        return 2 * self.pjg + 2 * self.lbr
   
    def luas(self):
        return self.pjg * self.lbr