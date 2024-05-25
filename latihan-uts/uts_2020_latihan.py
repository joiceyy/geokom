# In[1]:
# a = [1,2,3,4,4,5,6]
# for i in range (5):
#   print(i)

who = ('dana', 'nana', 'dina', 'dana', 'nana', 'dana', 'nana', 'dina', 'dana', 'dina',
'dana', 'nana', 'dina' )
money = (200000, 120000, 120000, 200000, 150000, 200000, 400000, 200000, 310000, 210000,
160000, 200000, 200000, )

jajan_dana = 0
jajan_nana = 0
jajan_dina = 0

for i in range (len(who)):
  print(who[i])

  if who[i] == 'dana':
    jajan_dana += money[i]
  elif who[i] == 'nana':
    jajan_nana += money[i]
  elif who[i] == 'dina':
    jajan_dina += money[i]

print('uang jajan dana:', jajan_dana)
print('uang jajan dina:', jajan_dina)
print('uang jajan nana:', jajan_nana)

# %%
buat class nasabah dengan  isinya nama, norek, jlh uang dan buat function menabung, tarik uang

class nasabah:
  def __init__(self,nama, norek, jumlah_uang,):
    self.nama = nama
    self.norek = norek
    self.jumlah_uang = jumlah_uang

  def menabung (self, jumlah_uang):
    self.jumlah_uang = 
# In[3]:
  
print(str(10))
print(int(10.5))
print(float(15))
print(str(20))

print(str(int(5*10e3)))
print(str(int(10-5)*0.3))

print(str(float(int(int('20')*10-1.2)**4)))
print(int('1'))

# In[]
who = ('dana', 'nana', 'dina', 'dana', 'nana', 'dana', 'nana', 'dina', 'dana', 'dina', 'dana', 'nana', 'dina')
money = (200000, 120000, 120000, 200000, 150000, 200000, 400000, 200000, 310000, 210000, 160000, 200000, 200000)

# Inisialisasi variabel untuk jumlah uang jajan setiap orang
jajan_dana = 0
jajan_dina = 0
jajan_nana = 0

# Iterasi melalui tuple 'who' dan 'money'
for i in range(len(who)):
    if who[i] == 'dana':
        jajan_dana += money[i]
    elif who[i] == 'dina':
        jajan_dina += money[i]
    elif who[i] == 'nana':
        jajan_nana += money[i]

# Menampilkan jumlah uang jajan setiap orang
print('uang jajan dana:', jajan_dana)
print('uang jajan dina:', jajan_dina)
print('uang jajan nana:', jajan_nana)

# In[]
who	= ('dana', 'nana', 'dina', 'dana', 'nana', 'dana', 'nana', 'dina', 'dana', 'dina', 'dana', 'nana', 'dina')
money = (200000, 120000, 120000, 200000, 150000, 200000, 400000, 200000, 310000, 210000,
160000, 200000, 200000)

jajan_dana = 0
jajan_dina = 0
jajan_nana = 0
for idx in range(len(who)):
  if 'dana' == who[idx]:
    jajan_dana = jajan_dana + money[idx]
  if 'dina' == who[idx]:
    jajan_dina = jajan_dina + money[idx]
  if 'nana' == who[idx]:
    jajan_nana = jajan_nana + money[idx]

# output lines
print('uang jajan dana:',jajan_dana)
print('uang jajan dina:',jajan_dina)
print('uang jajan nana:',jajan_nana)

# In[]:
import matplotlib.pyplot as plt

# Data
jajan_dana = [20000, 30000, 15000, 30000, 50000, 60000]
jajan_dina = [5000, 15000, 20000, 40000, 55000, 50000]
jajan_nana = [50000, 40000, 30000, 40000, 52000, 40000]
waktu = ['jan', 'feb', 'mar', 'apr', 'mei', 'jun']

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(waktu, jajan_dana, marker='o', label='Jajan Dana')
plt.plot(waktu, jajan_dina, marker='o', label='Jajan Dina')
plt.plot(waktu, jajan_nana, marker='o', label='Jajan Nana')

# Adding labels and title
plt.title('Grafik Pengeluaran Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah (IDR)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

# Adding legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()

# In[]
test_variable = 'test
test_variable.capitalize
'
# In[]
lst = [3,2,1,5,6,7]
for val in lst :
   print('nilai :', val)


# In[]
class mahasiswa :
   def __init__(self, nama, nim):
      self.nama = nama
      delf.nim = nim
      self.nama_min = nama + nim
  mahasiswa = nana, 20194


# In[]:
def calc_circle_area(r):
    l = 3.14*r**2
    return(l)
calc_circle_area(2)

# In[]
def pangkat(a, b):
    c = a**b
    print('-----')
    return c
pangkat(2,7)
def tambah(a, b):
    c = a + b
    print(c)
tambah (1,2)
def tambah(a, b):
    c = a + b
    return c
tambah (1,2)
xy = pangkat(2,7)
xy
nomor = [1,5,7,6,4]
for i in nomor :
    print (pangkat(i,2))

    # In[]
    def luas_area (r,p,l):
       if a == 'lingkaran':
          a = 3.14*r**2
       return a