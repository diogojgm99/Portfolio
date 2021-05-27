arr = [10,2,4,8,1,22,15]

print(arr)

#arr.sort()
#print(arr)
def new_func(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

new_arr = new_func(arr)

print(new_arr)



