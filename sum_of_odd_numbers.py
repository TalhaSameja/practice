num = [1,2,3,4,57,7,9,-59,-7,-9,-13]
def sumOfOddNumbers (num):
    total = 0
    for i in num:
        if i % 2 !=0:
            total += i
    return total
        
        
print(sumOfOddNumbers(num))