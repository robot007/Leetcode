#

import timeit
from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            ans = [nums] # I forgot [] at the beginning.
        # if len(nums)==2:
        #     ans = [nums, nums[::-1]]
        else:
            ans = []
            for ix, n in enumerate(nums):
                shorter = nums[:ix]+nums[ix+1:]
                for it in  self.permute(shorter):
                    ans.append([n]+it)
        return ans
# It took 0.006941899999999997 s to exection 1000 times
# Runtime: 40 ms, faster than 64.82% of Python3 online submissions for Permutations.
# Memory Usage: 13.8 MB, less than 5.36% of Python3 online submissions for Permutations.
    
    def permute2(self, nums):
        if len(nums) <= 1:
            return [nums]
        # nums.sort(reverse=True)
        subs = self.permute(nums[1:])
        ans = [[nums[0]] + sub for sub in subs]
        # print('A: nums={}, subs={} ans={}'.format(nums, subs, ans))
        for sub in subs:
            ans += [sub[:i+1] + [nums[0]] + sub[i+1:] for i in range(len(sub))]
        print('B: nums={}, subs={} ans={}'.format(nums, subs, ans))
        return ans

    def permute3(self, nums):
        perm = permutations(nums)
        return [list(_) for _ in perm]

def test_speed():
    sol = Solution()
    nums = [1,2,3]
    exp = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    ans = sol.permute3(nums)
    for it in exp:
        assert(it in ans)
    for it in ans:
        assert(it in exp)

if __name__ == "__main__":
    number=1000 
    st = timeit.timeit(test_speed, number=number)
    print('It took {} s to exection {} times'.format(st, number))

