# 1. twoSum
# one pass with hash table

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            try:
                k=nums.index(target-v)
                if i != k:
                    return [i,k]
            except:
                pass
