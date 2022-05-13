arr = list(map(int,input("Enter the list elements: ").split()))
print(arr)
s=0
max_sum=[]
for i in arr:
    s += i
    max_sum.append(s)
    if max(max_sum) > s:
        continue
    else:
        max_sum.append(s)
print(max(max_sum))
print(s) 
        
