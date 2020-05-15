# 73. Set Matrix Zeroes
# Medium

# 1811

# 285

# Add to List

# Share
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

from typing import *

import timeit
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for ir,r in enumerate(matrix):
            for ic,v in enumerate(r):
                if v==0:
                    col.append(ic)
                    row.append(ir)
        row=list(set(row))
        col=list(set(col))
        for ir, r in enumerate(matrix):
            for ic, v in enumerate(r):
                if ir in row:
                    matrix[ir][ic]=0
                if ic in col:
                    matrix[ir][ic]=0
# Runtime: 188 ms, faster than 10.60% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.2 MB, less than 5.13% of Python3 online submissions for Set Matrix Zeroes.                    

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_row=False # without it, the matrix will always be full 0.
        zero_col=False # rule: don't change the indicator while chaning others.
        for ir,r in enumerate(matrix):
            for ic,v in enumerate(r):
                if v==0:
                    matrix[ir][0]=0
                    matrix[0][ic]=0
                    zero_row = True if ir==0 else zero_row
                    zero_col = True if ic==0 else zero_col

        print(matrix)
        for ir in range(1, m):
            if matrix[ir][0]==0:
                matrix[ir]=[0]*n
                
        for ic in range(1, n): 
            if matrix[0][ic]==0:
                for ir in range(m):
                    matrix[ir][ic]=0

        if zero_row:
            matrix[0]=[0]*n
        if zero_col:
            for i in range(m):
                matrix[i][0]=0
# Runtime: 132 ms, faster than 87.95% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.4 MB, less than 5.13% of Python3 online submissions for Set Matrix Zeroes.

def test_speed():
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    rt = [[1,0,1],[0,0,0],[1,0,1]]
    assert(matrix == rt)


if __name__ == "__main__":
    number=1000 
    st = timeit.timeit(test_speed, number=number)
    print('It took {} s to exection {} times'.format(st, number))

