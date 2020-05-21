from typing import List
import timeit

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pd = [0] + [-1]*amount
        for i, v in enumerate(pd):
            if pd[i]<0:
                continue
            for c in coins:
                if i+c>amount:
                    continue
                if pd[c+i]<0 or pd[c+i] > pd[i]+1:
                    pd[i+c]=pd[i]+1
        # print([i for i,v in enumerate(pd)])
        # print(pd)
        return pd[amount]  

def test_speed():
    sol = Solution()
    coins = [1,2,5] 
    amount = 11
    assert(sol.coinChange(coins, amount) == 3)
    c=[2,5,10,1]
    a=27
    assert(sol.coinChange(c, a) == 4)

# Runtime: 1012 ms, faster than 91.03% of Python3 online submissions for Coin Change.
# Memory Usage: 14 MB, less than 30.56% of Python3 online submissions for Coin Change.

if __name__ == "__main__":
    number=1000 
    st = timeit.timeit(test_speed, number=number)
    print('It took {} s to exection {} times'.format(st, number))
