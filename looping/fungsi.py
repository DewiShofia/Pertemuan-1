# fungsi def adalah blok kode yang dapat dipanggil berulang kali
def sapa():
    print("Halo, selamat pagi")
sapa()  # memanggil fungsi
sapa()
# parameter(nilai yang dikirimkan ke fungsi) dan return(mengembalikan hasil fungsi/nilai dari hasil logic yang ditulis)
def tambah(a,b):
    return a + b

# function(return) itu hasil dan parameter itu (2,5)
hasil = tambah(2, 5)
print(hasil)

# variabel
def penjumlahan(a, b, c):
    return (a - b) * c
hasil = penjumlahan(7, 2, 2)
print(hasil)

hasil2 = 7 - 2
print(hasil2)

def desimalpenjumlahan(d, e):
    return d + e

hasildesimalpenjumlahan = desimalpenjumlahan(1.2, 1.3)
print(hasildesimalpenjumlahan)

def stringWithParam(f):
    return(f)

hasilstring = stringWithParam("Halo, selamat pagi")
print(hasilstring)

# default parameter
# jadi kalau misal parameter lupa dimasukkan nilainya, maka akan menggunakan nilai default, misal g=0

def desimalpenjumlahan(f, g=0):
    return f + g
hasildesimalpenjumlahan = desimalpenjumlahan(1.2)
print(hasildesimalpenjumlahan)

# default string
def  stringWithParam(h="Selamat Pagi dari default"):
    return h
hasilstring = stringWithParam()
print(hasilstring)






    