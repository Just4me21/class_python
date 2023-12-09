class Pasien:
    def __init__(self, nama, jenis_kelamin, keluhan, tanggal_datang, jam_kedatangan):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.keluhan = keluhan
        self.tanggal_datang = tanggal_datang
        self.jam_kedatangan = jam_kedatangan

# Contoh penggunaan class Pasien
pasien1 = Pasien(nama="abdul hayyi", jenis_kelamin="Laki-laki", keluhan="Sakit kepala", tanggal_datang="2023-12-09", jam_kedatangan="08:30")
pasien2 = Pasien(nama="ihwan", jenis_kelamin="laki-laki", keluhan="Demam", tanggal_datang="2023-12-09", jam_kedatangan="10:45")

# Menampilkan informasi pasien
print(f"Informasi Pasien 1: {pasien1.nama}, {pasien1.jenis_kelamin}, {pasien1.keluhan}, Tanggal: {pasien1.tanggal_datang}, Jam: {pasien1.jam_kedatangan}")
print(f"Informasi Pasien 2: {pasien2.nama}, {pasien2.jenis_kelamin}, {pasien2.keluhan}, Tanggal: {pasien2.tanggal_datang}, Jam: {pasien2.jam_kedatangan}")
