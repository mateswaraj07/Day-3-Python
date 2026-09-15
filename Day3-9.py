# Calculate the sum of all numbers form 1 to N uisng loop
num = int(input("Enter n: "))
total = 0
for i in range(1, num+1):
    total += i  
print(total)