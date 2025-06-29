n = [2,4,5,2]

n.sort()
#[2,2,4,5]

# for i in range(len(n)):
#     for j in range(i+1, len(n)):
#         if n[i] == n[j]:
#             print(i,j)
            
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        print(True)        
            
