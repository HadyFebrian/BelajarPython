#List []
x = ["laptop","monitor","mouse","mousepad","keyboard","webcam","microphone",1,2.2,"jakarta"]
print(x)
#List Bersifat Mutable(bisa berubah)
x[9]=("Indonesia")
print(x)
#Indexing Pada List
print(x[0])
print(x[9])
print(x[-1])
#Slicing Pada List Sequence[start:stop:step]
print(x[0:])
print((x[0:5]))
print(x[0:10:2])
#Tuple()
x = ("laptop","monitor","mouse","mousepad","keyboard","webcam","microphone",1,2.2,"jakarta")
print(x)
"""Tuple Bersifat Imutable(tidak bisa berubah)
x[9]=("Indonesia")
print(x)"""
#Indexing Pada Tuple
print(x[0])
print(x[9])
print(x[-1])
#Slicing Pada Tuple Sequence[start:stop:step]
print(x[0:])
print((x[0:5]))
print(x[0:10:2])
#Set{}
x =  {0,1,2,3,4,5,6,7,8,9}
print(x)
#Set Bersifat Unik(tidak ada duplikat)
x = {1,2,1,3,4,3,6,9,8,7,9,5,0}
print(x)
"""Tidak Bisa Indexing Pada Set Karena Tidak Memiliki Index
print(x[0])
print(x[9])
print(x[-1])"""
#Union dan Intersection Pada Set
x = {1,2,3,4,5,6}
y = {4,5,6,7,8,9}
union = x.union(y)
print("Union :",union)
intersection = x.intersection(y)
print("intersection :",intersection)
#Dictionary{}
x = {"Nama": "Hady Febrian", "Umur": 25, "Status": "Single"}
print(x)
"""Tidak Bisa Indexing Pada Dictionary
print(x[0])"""
#Menambah Data Pada Dictionary
x["Pekerjaan"] = "Machine Learning Developer"
print(x)
#Menghapus Data Pada Dictionary
del x["Status"]
print(x)
#Mengubah Nilai Pada Dictionary
x["Nama"] = "Rian Ganteng"
print(x)