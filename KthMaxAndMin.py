a = list(map(int,input("Enter the list elements: ").split()))
print("List is: ", a)
k = int(input("Enter a value: "))
sorted_a = sorted(a)
print("Kth Max element in the list is: ", sorted_a[len(sorted_a)-1-k])
print("Min element in the list is: ", sorted_a[0+k])
