def SortWithoutFunc(arr):
    l1=[]
    l2=[]
    for i in range(len(arr)):
        if arr[i] < 0:
            l1.append(arr[i])
        if arr[i] >= 0:
            l2.append(arr[i])
    return (l1+l2)
a = list(map(int,input("Enter the list elements: ").split()))
print(SortWithoutFunc(a))
