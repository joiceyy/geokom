{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "merah\n"
     ]
    }
   ],
   "source": [
    "class mobil:\n",
    "  warna = 'merah'\n",
    "\n",
    "mobil_1 = mobil ()\n",
    "print(mobil_1.warna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "merah\n",
      "hitam\n"
     ]
    }
   ],
   "source": [
    "# kita juga dapat merepolace atribut warna dewngan warna lain\n",
    "class mobil:\n",
    "  warna = 'merah'\n",
    "\n",
    "mobil_1 = mobil ()\n",
    "print(mobil_1.warna)\n",
    "\n",
    "# menambahkan code dibawah ini\n",
    "mobil.warna = 'hitam'\n",
    "print(mobil_1.warna)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "class mobil:\n",
    "  def __init__(self, color, speed):\n",
    "      self.warna = color\n",
    "      self.kecepatan = speed\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "lamborghini = mobil('kuning', 900)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'kuning'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ingin mengetahui warna lamborghini\n",
    "lamborghini.warna"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "900"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ingin mengetahui kecepatan lamborghini\n",
    "lamborghini.kecepatan\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "# menambahkan fungsi percepatan pada class mobil\n",
    "\n",
    "class mobil:\n",
    "  def __init__(self, color, speed):\n",
    "      self.warna = color\n",
    "      self.kecepatan = speed\n",
    "      print(f'mobil ini memiliki warna {color} dan kecepatan {speed}') \n",
    "      \n",
    "  def percepatan(self):\n",
    "      self.percepatan = self.kecepatan * 2\n",
    "\n",
    "      print(f'mobil ini memiliki warna {self.warna} percapatannya {self.percepatan}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mobil ini memiliki warna kuning dan kecepatan 900\n",
      "mobil ini memiliki warna kuning percapatannya 1800\n"
     ]
    }
   ],
   "source": [
    "lamborghini = mobil('kuning', 900)\n",
    "lamborghini.percepatan()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tahun' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# TUGAS SHIFT DCN\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;66;03m# 1. buatlah class tahun dengan atribut (nama, jumlah_hari,jumlah_bulan) dengan input HARI = 30 dan BULAN = 12\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;43;01mclass\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[38;5;21;43;01mTahun\u001b[39;49;00m\u001b[43m:\u001b[49m\n\u001b[0;32m      4\u001b[0m \u001b[43m  \u001b[49m\u001b[38;5;28;43;01mdef\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[38;5;21;43m__init__\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnama\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mjumlah_hari\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mjumlah_bulan\u001b[49m\u001b[43m)\u001b[49m\u001b[43m:\u001b[49m\n\u001b[0;32m      5\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnama\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mnama\u001b[49m\n",
      "Cell \u001b[1;32mIn[3], line 12\u001b[0m, in \u001b[0;36mTahun\u001b[1;34m()\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mhari_setahun\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m     11\u001b[0m    \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mjumlah_hari \u001b[38;5;241m*\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mjumlah_bulan\n\u001b[1;32m---> 12\u001b[0m tahun2024 \u001b[38;5;241m=\u001b[39m \u001b[43mtahun\u001b[49m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m2024\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;241m30\u001b[39m,\u001b[38;5;241m12\u001b[39m)\n\u001b[0;32m     13\u001b[0m \u001b[38;5;28mprint\u001b[39m(tahun2024\u001b[38;5;241m.\u001b[39mhari_setahun())\n",
      "\u001b[1;31mNameError\u001b[0m: name 'tahun' is not defined"
     ]
    }
   ],
   "source": [
    "# TUGAS SHIFT DCN\n",
    "# 1. buatlah class tahun dengan atribut (nama, jumlah_hari,jumlah_bulan) dengan input HARI = 30 dan BULAN = 12\n",
    "class Tahun:\n",
    "  def __init__(self, nama, jumlah_hari, jumlah_bulan):\n",
    "    self.nama = nama\n",
    "    self.jumlah_hari = jumlah_hari\n",
    "    self.jumlah_bulan = jumlah_bulan\n",
    "\n",
    "# 2. Tambahkan fungsi hari_setahun untuk menghitung jumlah hari dalam satu tahun menggunakan atribut yang telah di inpu\n",
    "  def hari_setahun(self):\n",
    "     return self.jumlah_hari *self.jumlah_bulan\n",
    "  tahun2024 = tahun('2024', 30,12)\n",
    "  print(tahun2024.hari_setahun())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "class kereta:\n",
    "    def __init__(self, nama,jenis_kereta, jumlah_gerbong, gerbong_tambahan):\n",
    "        self.nama = nama\n",
    "        self.jenis_kereta = jenis_kereta\n",
    "        self.jumlah_gerbong = jumlah_gerbong\n",
    "        self.gerbong_tambahan = gerbong_tambahan\n",
    "        print (f'Selamat anda {self.nama} telah berhasil memboking kereta {self.jenis_kereta} dengan jumlah gerbong {self.jumlah_gerbong}') \n",
    "    \n",
    "    def total_gerbong (self):\n",
    "        self.jumlah_gerbong = self.jumlah_gerbong + self.gerbong_tambahan\n",
    "        print(f'setelah ditambah total gerbong kereta saat ini adalah {self.jumlah_gerbong}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Selamat anda Kai telah berhasil memboking kereta tempur dengan jumlah gerbong 2\n",
      "setelah ditambah total gerbong kereta saat ini adalah 4\n"
     ]
    }
   ],
   "source": [
    "keretaTempur = kereta('Kai', 'tempur', 2, 2)\n",
    "keretaTempur.total_gerbong()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Petrofisis:\n",
    "  def __init__(self, gr, nphi, rhob, phid):\n",
    "    self.gr = gr\n",
    "    self.nphi = nphi\n",
    "    self.rhob = rhob\n",
    "    self.phid = phid \n",
    "\n",
    "def vshale(self, grmin, grmax):\n",
    "  return(se)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "class emoney:\n",
    "  def __init__(self, id, name, balance):\n",
    "    self.id = id\n",
    "    self.name = name\n",
    "    self.balance = balance\n",
    "\n",
    "  def check_balance(self):\n",
    "   return(self.balance) \n",
    "\n",
    "  def pay(self):\n",
    "    self.balance = self.balance - pay\n",
    "\n",
    "  def top_up(self):\n",
    "    self.balance = top_up + self.balance\n",
    "\n",
    "\n",
    "kartu = emoney('8370474', 'brizzi', 65.000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
