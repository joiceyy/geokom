# In[ ]:
# 1. buatlah class tahun dengan atribut (nama, jumlah_hari,jumlah_bulan) dengan input HARI = 30 dan BULAN = 12
class Tahun:
  def __init__(self, nama, jumlah_hari, jumlah_bulan):
    self.nama = nama
    self.jumlah_hari = jumlah_hari
    self.jumlah_bulan = jumlah_bulan

#  2. Tambahkan fungsi hari_setahun untuk menghitung jumlah hari dalam satu tahun menggunakan atribut yang telah di inpu
  def hari_setahun(self):
     return self.jumlah_hari *self.jumlah_bulan
  
tahun2024 = Tahun('2024', 30,12)
print(tahun2024.hari_setahun())

# In[2]:
class kereta:
    def __init__(self, nama,jenis_kereta, jumlah_gerbong, gerbong_tambahan):
        self.nama = nama
        self.jenis_kereta = jenis_kereta
        self.jumlah_gerbong = jumlah_gerbong
        self.gerbong_tambahan = gerbong_tambahan
        print (f'Selamat anda {self.nama} telah berhasil memboking kereta {self.jenis_kereta} dengan jumlah gerbong {self.jumlah_gerbong}') 
    
    def total_gerbong (self):
        self.jumlah_gerbong = self.jumlah_gerbong + self.gerbong_tambahan
        print(f'setelah ditambah total gerbong kereta saat ini adalah {self.jumlah_gerbong}')

bogowonto = kereta('bogowonto', 'ekonomi', 23, 2)
bogowonto.total_gerbong()

# In[]:
class orang:
   def __init__(self, nama, gender, tinggi_badan, berat_badan, umur_sekarang):
      self.nama = nama
      self.gender = gender
      self.tinggi_badan = tinggi_badan
      self.berat_badan = berat_badan
      self.umur_sekarang = umur_sekarang
      print(f'Mahasiswa {self.nama} dengan jenis kelamin {self.gender} memiliki tinggi badan {self.tinggi_badan} dan berat badan {self.berat_badan} dan usia saat ini {self.umur_sekarang}')

   def kondisi_sekarang (self):
      self.kondisi_sekarang = self.tinggi_badan + 5
      print(f'setelah 2 tahun kemudian, tinggi badan mahasiswa itu menjadi {self.kondisi_sekarang}')
   
   def ulangtahun(self):
      self.umur_sekarang = self.umur_sekarang + 1
      print(f'lola sekarang berusia {self.umur_sekarang}')
   
   def meninggal(self):
      self.umur_sekarang = 0
      print(f'lola sekarang berusia {self.umur_sekarang}')



lola = orang('lola', 'Pria', 178, 60, 12)
lola.kondisi_sekarang()
lola.ulangtahun()
lola.ulangtahun()
lola.ulangtahun()
lola.meninggal()
lola.umur_sekarang
