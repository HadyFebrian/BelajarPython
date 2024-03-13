#Contoh Fungsi Mencari luas Persegi Panjang
def mencariluaspersegipanjang(panjang,lebar):
    luaspersegipanjang = panjang * lebar
    return luaspersegipanjang
luas_1 = mencariluaspersegipanjang(5,3)
luas_2 = mencariluaspersegipanjang(9,4)
luas_3 = mencariluaspersegipanjang(4,7)
luas_4 = mencariluaspersegipanjang(2,1)
luas_5 = mencariluaspersegipanjang(6,8)
print(f"Jadi Luas Persegi Panjang 1 Adalah : {luas_1}")
print(f"Jadi Luas Persegi Panjang 2 Adalah : {luas_2}")
print(f"Jadi Luas Persegi Panjang 3 Adalah : {luas_3}")
print(f"Jadi Luas Persegi Panjang 4 Adalah : {luas_4}")
print(f"Jadi Luas Persegi Panjang 5 Adalah : {luas_5}")
# Mencoba Menggunakan Input
def mencariluaspersegipanjang(panjang,lebar):
    luaspersegipanjang = panjang * lebar
    return luaspersegipanjang
panjang = int(input("Masukkan Panjang       : "))
lebar = int(input("Masukkan Lebar       : "))
luas = mencariluaspersegipanjang(panjang,lebar)
print(f"Jadi Luas Persegi Panjang Adalah : {luas}")
#positional/keyword
def sapaan(nama,pesan):
    return "Hallo, " + nama + "! " + pesan
print(sapaan("Hady Febrian ","Selamat Pagi"))
#Mencoba Menggunakan Input
def sapaan(nama,pesan):
    return "Hallo, " + nama + "!" + pesan
nama = input("Masukkan Nama Anda : ")
pesan = input("Masukkan Pesan Anda : ")
print(sapaan(nama,pesan))
