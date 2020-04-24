# # 13 roman to int
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

import timeit
class Solution:
    def romanToInt(self, x):
        method = 2
        if method==1:
            strnum=str(x)
            if x>=0:
                strnumrev = strnum[::-1]
                x2=int(strnumrev)
                return (x==x2)
            else:
                return False
# Runtime: 52 ms, faster than 88.06% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
        if method ==12:
            strnum=str(x)
            if x>=0:
                strnumrev = strnum[::-1]
                # x2=int(strnumrev)
                return (strnum==strnumrev)
            else:
                return False
# Runtime: 56 ms, faster than 77.86% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 6.50% of Python3 online submissions for Palindrome Number.                
        if method == 13:
            return x>=0 and (str(x) == str(x)[::-1])
# Runtime: 60 ms, faster than 65.13% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.9 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
        if method == 2: 
            num = 0
            a = abs(x)
            while (a !=0 ):
                bigdig = a % 10
                num = num*10 + bigdig
                # a = int(a/10)
# Runtime: 80 ms, faster than 18.23% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.9 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
                a = a // 10
# Runtime: 64 ms, faster than 51.80% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 6.50% of Python3 online submissions for Palindrome Number.                
            if (num == x):
                return True
            else:
                return False
def test_speed():
    sol = Solution()
    nums = [121, -121]
    exp = [True, False]
    for x, e in zip(nums, exp):
        ans = sol.palindromeNumber(x)
        # print('x:{}, e:{} ans:{}'.format(x,e, ans))
        assert(ans==e), 'wrong result'

if __name__ == "__main__":
    number=1000 
    st = timeit.timeit(test_speed, number=number)
    print('It took {} s to exection {} times'.format(st, number))

