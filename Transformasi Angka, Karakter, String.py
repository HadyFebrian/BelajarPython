#Upper()
kata = "hady febrian"
kata = kata.upper()
print(kata)
#lower()
kata1 = kata
kata1 = kata1.lower()
print(kata1)
#rstrip
print("hady febrian".rstrip("febrian"))
#lstrip
print("hady febrian".lstrip("hady"))
#strip
print("hady febrian".strip("hady"))
print("hady febrian".strip("febrian"))
print("ganteng hady febrian ganteng".strip("ganteng"))
#startswith
print("hady febrian".startswith("hady"))
print("hady febrian".startswith("febrian"))
#endswith
print("hady febrian".endswith("hady"))
print("hady febrian".endswith("febrian"))
#join
print(" ".join(["hady","febrian"]))
print(" ganteng ".join(["hady","febrian"]))
#split
print("hady febrian".split())
print("""Halo !!!
Perkenalkan Saya Hady Febrian
Saya Berusia 25 Tahun""".split("/n"))
#replace
string = ("saya sedang belajar pemograman")
print(string.replace("pemograman","python"))
#isupper
kata = "HADY FEBRIAN"
print(kata.isupper())
kata = "hady Febrian"
print(kata.isupper())
#islower
kata = "hady febrian"
print(kata.islower())
kata = "Hady Febrian"
print(kata.islower())
#isalpha
kata = "HadyFebrian"
print(kata.isalpha())
kata = "Hady Febrian"
print(kata.isalpha())
#isalnum
kata = "Hady25"
print(kata.isalnum())
kata = "Hady 25"
print(kata.isalnum())
#isdecimal
print("123".isdecimal())
print("abc".isdecimal())
#isspace
print(" ".isspace())
print("".isspace())
#istitle
print("Hady Febrian".istitle())
print("HADY FEBRIAN".istitle())
#zfill
kata = "hady"
tambah_angka = kata.zfill(5)
print(tambah_angka)
#rjust
kata = "hady febrian"
print(kata.rjust(20))
print(kata.rjust(20,"-"))
#ljust
print(kata.ljust(20))
print(kata.ljust(20,"-"))
#center
print(kata.center(20))
print(kata.center(20,"-"))