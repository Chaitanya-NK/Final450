import random
k = int(input("Enter an integer: "))
arr = list(map(int,input("Enter the list elements: ").split()))
updated_arr = []
for i in arr:
    x = random.randint(1,2)
    if i<k:
        updated_arr.append(i+k)
    elif x==1:
        updated_arr.append(i+k)
    elif x==2:
        updated_arr.append(i-k)
print(max(updated_arr)-min(updated_arr))
print(updated_arr)
