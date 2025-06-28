class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):
        
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]
                
s1 = Solution([1,2,3], 5)
print(s1.twoSum())