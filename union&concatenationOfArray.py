a = list(map(int,input("Enter the list1 elements: ").split()))
b = list(map(int,input("Enter the list2 elements: ").split()))
print("Union is: ", a+b)
c=[]
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print("Intersection is: ",c)
