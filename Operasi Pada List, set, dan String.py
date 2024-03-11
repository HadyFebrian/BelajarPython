#len()
#contoh pada list
x = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(x)
print(len(x))
#contoh pada set
x = {1, 3, 3, 5, 5, 5, 7, 7, 9}
print(x)
print(len(x))
#contoh pada string
x = "HADY FEBRIAN"
print(x)
print(len(x))
#min()
x = (0,1,2,3,4,5,6,7,8,9)
print(min(x))
#max()
print(max(x))
#count
x = (0,1,1,1,1,1,2,3,4,5,6)
print(x.count(1))
x = "nama saya hady febrian"
print(x.count("a"))
#in()
print("nama"in x)
print("saya"in x)
print("python"in x)
#memberikan nilai untuk multiple variable
x = ("sepatu","sekolah","warna","hitam")
a,b,c,d = x
print(x)
print(a)
print(b)
print(c)
print(d)
#sort()
x = ["sepatu","sekolah","warna","hitam"]
x.sort()
print(x)
#reverse sort
x.sort(reverse=True)
print(x)