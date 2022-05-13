arr = list(map(int,input("Enter the list elements: ").split()))
print("Array: ",arr)
duplicates=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            duplicates.append(arr[j])
print("Duplicates: ",duplicates)
