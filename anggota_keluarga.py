class AnggotaKeluarga:
    def __init__(self, nama, peran, jenis_kelamin, usia):
        self.nama = nama
        self.peran = peran
        self.jenis_kelamin = jenis_kelamin
        self.usia = usia

# Contoh penggunaan class AnggotaKeluarga
ayah = AnggotaKeluarga(nama="Bapak", peran="Ayah", jenis_kelamin="Laki-laki", usia=30)
ibu = AnggotaKeluarga(nama="Ibu", peran="Ibu", jenis_kelamin="Perempuan", usia=25)
anak = AnggotaKeluarga(nama="Anak", peran="Anak", jenis_kelamin="Laki-laki", usia=10)

# Menampilkan informasi anggota keluarga
print(f"Informasi Ayah: {ayah.nama}, {ayah.peran}, {ayah.jenis_kelamin}, {ayah.usia} tahun")
print(f"Informasi Ibu: {ibu.nama}, {ibu.peran}, {ibu.jenis_kelamin}, {ibu.usia} tahun")
print(f"Informasi Anak: {anak.nama}, {anak.peran}, {anak.jenis_kelamin}, {anak.usia} tahun")
