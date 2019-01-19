
// Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

// Find the maximum coins you can collect by bursting the balloons wisely.

// Note:

// You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
// 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

// # Wrong Answer 1/18/19
// [9,76,64,21,97,60,5], expected 1088290, output 1088286

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n  = nums.size();
        /// Insert two 1s in the begining and in the end.
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        vector<vector<int>> c(n+2, vector<int>(n+2, 0));
        for(int l  = 1; l <=n ; ++l) {
            for (int i = 1; i <= n-l+1; ++i) {
                int j = i + l -1;
                for(int k = i; k <= j; ++k) {
                    c[i][j] = max(c[i][j], c[i][k-1]+ nums[i-1]*nums[k]*nums[j+1] + c[k+1][j]);
                }
            }
        }
        return c[1][n];
    }
};