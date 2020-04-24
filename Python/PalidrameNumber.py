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
    def palindromeNumber(self, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
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

'''
Comparable C++ implementation
Runtime: 8 ms, faster than 88.45% of C++ online submissions for Palindrome Number.
Memory Usage: 5.8 MB, less than 100.00% of C++ online submissions for Palindrome Number.
    bool isPalindrome(int x) {
        if(x < 0 || (x > 0 && x % 10 == 0)) //  "20" is invalid
            return false;
        int tmp = 0;
        while(tmp < x && tmp < x / 10) {
            tmp *= 10;
            tmp += x % 10;
            x /= 10;
        }
        return tmp == x || tmp == x/10;
    }

Java implementation
Runtime: 7 ms, faster than 74.06% of Java online submissions for Palindrome Number.
Memory Usage: 38.3 MB, less than 5.02% of Java online submissions for Palindrome Number.
    public boolean isPalindrome(int x) {
        int rev = 0, y = x;
        while (y > 0) {
            rev = rev * 10 + y % 10;
            y /= 10;
        }
        return rev == x;
    }

    '''