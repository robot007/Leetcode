// Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
// Do not allocate extra space for another array, you must do this in place with constant memory.
// For example, Given input array A = [1,1,2],
// Your function should return length = 2, and A is now [1,2].
// Example program
// Time:  O(n)
// Space: O(1)

// c++11 syntax
// g++ RemoveDuplicates_STL.cpp  -std=c++11 -o stl.exe

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int remove_dups(vector<int>& nums) {
        int left=0, right; // = 1;
        for(right=1; right<nums.size(); right++)
            if( nums[left]!=nums[right])
                nums[++left]=nums[right];
        return ++left; // left is index, which is 1 less than the length
    }
};

int main()
{
  // int num_init[]={1,2,2,3,4};
  // vector<int> nums_old=vector<int>(num_init, num_init+5);

  // c++11 or c++14
  vector<int> nums={1,1,2,2,4};
  Solution clean;
  int len=clean.remove_dups(nums);
  cout<<"Total len="<<len<<endl;
  for(int i=0; i<len; i++){
      cout<<nums[i]<<endl;
  }

}
