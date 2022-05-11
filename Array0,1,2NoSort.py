def SortWithoutFunc(arr):
    l1=[]
    l2=[]
    l3=[]
    for i in range(len(arr)):
        if arr[i] == 0:
            l1.append(arr[i])
        if arr[i] == 1:
            l2.append(arr[i])
        if arr[i] == 2:
            l3.append(arr[i])
    return (l1+l2+l3)
a = list(map(int,input("Enter the list elements: ").split()))
print(SortWithoutFunc(a))
