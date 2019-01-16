
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

class Solution:
    def maxCoins(self, nums, idx=-1):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 and idx==0:
            return 0
        if idx >= 0:
            nums=nums.copy()
            nums.pop(idx)
        val1 = [v[0]*v[1]*v[2] for v in zip([1]+nums[:-2], nums, nums[1:]+[1])]
        val2= [self.maxCoins(nums, ix2) for ix2 in range(len(nums))]
        val = [v[0]+v[1] for v in zip(val1, val2)]
        print(f'val={val}')
        coin = max(val)
        ix = val.index(coin)
        print(f'if remove {nums[ix]} from {nums}, get {val1[ix]} coins of total {coin} coins.')
        return coin


if __name__ == '__main__':
    nums=[3,1,5,8]
    sol = Solution()
    print(sol.maxCoins(nums))        