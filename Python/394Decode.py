# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

## always valid!
digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ab321[12]1 //no
# ab1[12]a //no
# 1a1[ab]c // no
# a[bc] // no 
# 1[d]12 // no 
# 1]12
class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        head=[]
        content=[]
        bracket=[]
        tail=[]
        is_ready=False
        state=1 # 1: head, 2: num start, 3: wrong bracket, 4: cont start, 5: cont end, 6: tail start, 7: tail end 
        k=0
        for ix, c1 in enumerate(s):
            ## try 1: FSM
            # if is_ready and len(content)>0:
            #     if len(num)>0:
            #         k=int(num)
            #     else:
            #         k=1
            #     element = self.decodeString(content)
            #     content2=[it for it in element for cnt in range(k)]
            #     ans = head+content2+tail
            # if is_ready and len(content)==0:
            #     ans = head+tail
            # else: # not ready
            ## try 2: one by one test
            if c1 in digits and len(content)==0:
                num.append(c1)
                if ix<len(s):
                    c2=s[ix+1]
                    if c2=='[':
                        k=int(num)
                        bracket.append(ix+1)
                else: # ix >= len(s)
                    tail+=num
            elif (c1 not in digits) and len(content)==0: # not a num
                head.append(c1)
            elif len(content)>0:
                if c1==']':
                    # pop the last l
                    match_len=ix-bracket.pop()
                    short_content = self.decodeString(s[ix:bracket.pop()])
                    content = short_content
                    for cnt in range(k)-1:
                        content+short_content
                    


