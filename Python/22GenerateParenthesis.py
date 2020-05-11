22. Generate Parentheses
Medium

4655

248

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Accepted
513,904
Submissions
841,466

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        result  = []
        self.helper(n,n,'', result)
        return result

    def helper(self, l, r, item, result):
        if l==0 and r==0:
            result.append(item)
        if r<l:
            return

        if r>0:
            self.helper(l, r-1, item+')', result)
        if l>0:
            self.helper(l-1, r, item+'(', result)
