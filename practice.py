n = [2,4,5,7]
target = 11
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i]+n[j] == target:
            print(i,j)
            
            
            
