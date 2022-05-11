a = list(map(int,input("Enter the array values : ").split()))
print("Entered list is: ",a)
n = len(a)
'''st = [1,2,3,4,5]
n = 5'''
a_trial = []
a_trial.append(a[-1])
a_trial.extend(a[:n-1])
print("List after cycle rotation by one: ",a_trial)
