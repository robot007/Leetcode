# 229. Majority Element II
# Medium

# 1416

# 159

# Add to List

# Share
# Given a SINGLE integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
## NOTE: [10, 11, 1000] is illegal

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

## [1,2,3,4,5,1,2,3,4,5,3,4,5,3,4,5,3]

from typing import *

import timeit
class Solution:
    def majority(self, nums:List[int]) -> List[int]:
        # since there are 0-9 numbers, it can has 2 values in the array at most.
        num=[0, 1]
        cnt=[0, 0]
        for v in nums:
            if v==num[0]:
                cnt[0]+=1
            elif v==num[1]:
                cnt[1]+=1
            elif cnt[0]==0:
                num[0]=v
                cnt[0]=1
            elif cnt[1]==0:
                num[1]=v
                cnt[1]=1
            else:
                cnt[0]-=1
                cnt[1]-=1
        cnt=[0,0]
        for v in nums:
            if v ==num[0]:
                cnt[0]+=1
            if v ==num[1]:
                cnt[1]+=1
        ans =[ ]
        if cnt[0]>len(nums)//3:
            ans.append(num[0])
        if cnt[1]>len(nums)//3:
            ans.append(num[1])
        return ans
# Runtime: 136 ms, faster than 16.87% of Python3 online submissions for Majority Element II.
# Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Majority Element II.

    def majority2(self, nums:List[int]) -> List[int]: 
        t = len(nums) // 3
        return [n for n in set(sorted(nums)[t::max(t,1)]) if nums.count(n) > t]

def test_speed():
    sol = Solution()
    ans = sol.majority([1,1,1,3,3,2,2,2])
    assert(set(ans) == set([1,2]))
    ans = sol.majority2([1,1,1,3,3,2,2,2])
    assert(set(ans) == set([1,2]))

if __name__ == "__main__":
    number=1000 
    st = timeit.timeit(test_speed, number=number)
    print('It took {} s to exection {} times'.format(st, number))

