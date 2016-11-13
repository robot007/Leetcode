// Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
// Do not allocate extra space for another array, you must do this in place with constant memory.
// For example, Given input array A = [1,1,2],
// Your function should return length = 2, and A is now [1,2].
// Example program
#include <iostream>
#include <string>
#include <list>
#include <iterator>
using namespace std;

// Remove Duplicates from Sorted Array
// No STL
class Solution {
    public:
        // Solution(){};
        int removeDuplicates(int nums[], int len)
        {
        // if (nums.length == 0) return 0;
            if (len==0) return 0;
            int id_tail= 0;
            for (int id_head = 0; id_head < len; id_head++) {
                // start from 0, otherwise lost the 1st item

                if (nums[id_tail] != nums[id_head])
                    nums[id_tail++] = nums[id_head];

            }
            // cout<<nums[id_tail]<<endl;
            return id_tail;
        }
};

int main()
{
  int nums[]={1,2,2,3,4};
  int len=5;
  Solution clean;
  int len2=clean.removeDuplicates(nums, len);
  cout<<"Total len="<<len2<<endl;
  for(int i=0; i<len2; i++){
      cout<<nums[i]<<endl;
  }

}
