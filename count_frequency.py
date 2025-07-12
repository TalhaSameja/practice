def count_frequnecy(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency
arr = [1,1,12,3,4,6,12,3,3,3]
result = count_frequnecy(arr)
for number in result:
    print(f"{number} => {result[number]} times")