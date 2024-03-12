#Menampilkan Angka 1-10
#For
for i in range(1,11):
    print(i)
#While
i=0
while i<=10:
    print(i)
    i+=1
#Nested Loop
for i in range(1,11):
    for j in range(1,11):
        print(i,j)

evenNumber = []
evenNumber = [i + 2 for i in range(-2, 500,2)]
print(evenNumber)

evenNumber = []
for i in range(0,500,2):
    evenNumber.append(i)
print(evenNumber)