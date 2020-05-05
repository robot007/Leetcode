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
    def romanToInt(self, s: str) -> int:
        method =3
        if method == 1:
            token={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
            total=0
            
            ix=0
            while ix < len(s)-1:
                it1 = s[ix]
                it2 = s[ix+1]
                if token[it1]>=token[it2]:
                    total+=token[it1]
                    ix+=1
                else: # token[]
                    total+=token[it2]-token[it1]
                    ix+=2
            # for the last
            if ix<len(s):
                total+=token[s[ix]]
            return total

# Runtime: 40 ms, faster than 89.96% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.8 MB, less than 5.38% of Python3 online submissions for Roman to Integer.
        if method==2:
            roman = s

            components = []
            for r in roman:
                if r not in Mapping:
                    raise Exception()
                components.append(Mapping[r])
            summed = 0
            prev = None
            for val in reversed(components):
                if prev is None or prev <= val:
                    summed += val
                else:
                    summed -= val
                prev = val
            return summed
## When the dictionary is global, it is about 20% faster, in this case.
# Runtime: 32 ms, faster than 99.15% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.7 MB, less than 5.38% of Python3 online submissions for Roman to Integer.
# It took 0.009149000000000074 s to exection 1000 times
        if method == 3:
            convert_dic ={'0':0, "I":1,"V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
            # 当i 到最后了， i+1 越界了，这里我们可以给s加一个零的尾巴。这样无论s最后是啥字母，肯定比0都大。
            # s += '0'
            ans = 0
            # 思路很简单，就是指针从左往右移动。
            # 遇到5 = IV这样的，我们可以理解为左边i比右边i+1小的，i那一位为负数。也就是IV = -1 + 5 = 4， IX = -1 + 10 = 9
            # 令hash为罗马字到数字的map：
            # 整个s 从左往右读取，if hash s[i] < hash s[i+1], ans -= hash s[i]. else ans += hash s[i]   
            for i in range(len(s)-1):#此处要减一，数字下标从0开始
                if convert_dic[s[i]] < convert_dic[s[i+1]]:
                    ans -= convert_dic[s[i]]
                else:
                    ans += convert_dic[s[i]]
            ans += convert_dic[s[len(s)-1]]
            return ans
## The minimal memory method
# It took 0.006883399999999984 s to exection 1000 times        

Mapping = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }

def test_speed():
    sol = Solution()
    nums = ['III', 'II']
    exp = [3, 2]
    for x, e in zip(nums, exp):
        ans = sol.romanToInt(x)
        # print('x:{}, e:{} ans:{}'.format(x,e, ans))
        assert(ans==e), 'wrong result'

if __name__ == "__main__":
    number=1000 
    st = timeit.timeit(test_speed, number=number)
    print('It took {} s to exection {} times'.format(st, number))

