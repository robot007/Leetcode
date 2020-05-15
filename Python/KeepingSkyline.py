'''
https://leetcode.com/problems/max-increase-to-keep-city-skyline/ 

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.  

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example. 

What is the maximum total sum that the height of the buildings can be increased? 

Example: Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]] Output: 35 Explanation: The grid is: [ [3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0] ] The skyline viewed from top or bottom is: [9, 4, 8, 7] The skyline viewed from left or right is: [8, 7, 9, 3] The grid after increasing the height of buildings without affecting skylines is:  gridNew = [ [8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3] ]  

Notes: 

1 < grid.length = grid[0].length <= 50. 

All heights grid[i][j] are in the range [0, 100]. 

All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism. '''

from typing import Dict, List, Tuple

''' 
# basic. speed 45%
# 6 minutes ago	Accepted	52 ms	13.3 MB	python3

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top = [0] * len(grid[0])
        left = [0] * len(grid)
        sum0 = 0
        for row in range(len(grid)):
            max_row=0
            print('grid{}={}'.format(row,grid[row]))
            for col in range(len(grid[row])):
                if top[col]<grid[row][col]:
                    top[col]=grid[row][col]
                if max_row<grid[row][col]:
                    max_row=grid[row][col]
                sum0 += grid[row][col]
            left[row] = max_row
        print('top={}, left={}'.format(top, left))
        
        sum1=0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                h = min(top[col], left[row])
                # if grid[row][col]<h:
                grid[row][col]=h
                sum1 +=h
        
        print('After:')
        for row in range(len(grid)):
            print('grid{}={}'.format(row, grid[row]))

        s = sum1-sum0
        print('s={}'.format(s))
        return s
'''

'''
# method 2: no numpy
import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = np.array(grid)
        left = np.max(m, axis=1)
        top = np.max(m, axis=0)
        s0 = np.sum(np.sum(grid))
        s1=0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = min(left[row], top[col])
                s1+=grid[row][col]
        return s1-s0
'''

# method 3
# Runtime: 44 ms, faster than 91.43% of Python3 online submissions for Max Increase to Keep City Skyline.
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        s0 = sum([sum(r) for r in grid])
        left = [max(r) for r in grid]
        # top = [0]*len(grid[0])
        # for cid in range(len(grid[0])):
        #     top[cid] = max([r[cid] for r in grid])
        top = [ max([r[cid] for r in grid]) for cid in range(len(grid[0]))]
        
        s1=0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = min(left[row], top[col])
                s1+=grid[row][col]
        grid = [ (min(c,r) for c in r) for r in grid]
        return s1-s0


def main():
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    s = Solution()
    print(s.maxIncreaseKeepingSkyline(grid) )
        
if __name__ == "__main__":
    main()    
                
        