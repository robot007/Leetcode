# 1. twoSum
# one pass with hash table
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
import timeit
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        method = 3
        if method==1:
            for ix, v in enumerate(nums):
                for iy, v2 in enumerate(nums[ix+1:]):
                    if v+v2==target:
                        return [ix, iy+ix+1]
        # Runtime: 5140 ms, faster than 18.79% of Python3 online submissions for Two Sum.
        # Memory Usage: 14.7 MB, less than 17.21% of Python3 online submissions for Two Sum.                        
        # for nums
        if method ==2: 
            return [[ix, iy] for ix, vx in enumerate(nums) for iy in range(ix+1,len(nums)) if vx+nums[iy]==target][0]
        ## short code, but poor performance
        # Runtime: 5848 ms, faster than 14.74% of Python3 online submissions for Two Sum.
        # Memory Usage: 14.9 MB, less than 9.76% of Python3 online submissions for Two Sum.            
        
        if method ==3: # dictionary
            dic = {}
            for ix in range(len(nums)):
                if target - nums[ix] not in dic:
                    dic[nums[ix]]=ix
                else:
                    return [dic[target-nums[ix]], ix]
        # Runtime: 40 ms, faster than 97.89% of Python3 online submissions for Two Sum.
        # Memory Usage: 15.1 MB, less than 5.34% of Python3 online submissions for Two Sum.


def test_speed():
    sol = Solution()
    nums = [2, 7, 8, 3]
    sol.twoSum(nums, 9)

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 8, 3]
    ans = sol.twoSum(nums, 9)
    cmd = '''test_speed()'''
    st = timeit.timeit(test_speed, number=1000 )
    exp = [0, 1]
    print(ans)
    print(st)
    assert (ans==exp)