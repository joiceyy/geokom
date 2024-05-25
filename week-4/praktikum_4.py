gr = 30
grmin = 20
grmax = 80
vshale = (gr - grmin)/ (grmax - grmin)
def world ():
    print ('im alive')

def namadia (n, m):
    print ('namanya adalah' ,n, 'dan dia suka', m)
namadia ('jola', 'yuyu')
# memasukkan nilai default
def apa(n = 'harimau'):
    print('ini merupakan', n)

apa ('apa ya?')
# soal uts nanti
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
    
# SOAL UTS
# BUATLAH FUNCTION UNTUK MENGHITUNG LUAS LINGKARAN
def calc_circle_area(r):
    l = 3.14*r**2
    return(l)

calc_circle_area(2)
# 2. buatlah fanction untuk menghitung vshale
gr = 25
grmin = 19
grmax = 87
vshale = (gr - grmin)/ (grmax - grmin)
print(vshale)
def vshale(gr, grmin, grmax):

    x = (gr - grmin)/(grmax - grmin)
    return x
vshale (27, 20, 87)
# 3. buatlah sebuah program yang dapat menghitunng nilai gr dari list berupa gr =[20,25,34,91,64,57,92,64,15,85,34,52,21,62] menggunakan function dan itiration (loop) beserta nilai dari gmin = 10 dan gmax= 100
def daftar (gr, grmin, grmax):
    vshale = (gr - grmin)/ (grmax - grmin)
    return vshale
gr = [20,25,34,91,64,57,92,64,15,85,34,52,21,62]

for i in gr :
    print(daftar(i,10,100))
