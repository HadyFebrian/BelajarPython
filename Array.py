var_list = [1,2,3,4,5]
for element in var_list:
    print(id(element))
#Deklarasi Array
var_arr = [1,2,3,4,5]
print(var_arr)
#Deklarasi Nilai Default
var_arr = [0 for i in range(5)]
print(var_arr)
#merubah Nilai Default
for i in range(5):
    var_arr[i] = i
print(var_arr)
#Mengakses Element Array
var_arr = [1,2,3,4,5,6,7,8,9,0]
print(var_arr[1])
var_arr = [1,2,3,4,5,6,7,8,9,0]
for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:next_element = None
    print(f"Current Element : {current_element}, Next Element : {next_element}")
#Contoh Lain
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]
for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)