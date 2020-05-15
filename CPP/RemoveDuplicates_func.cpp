// Given a sorted array, remove the duplicates in place such that each element appear only once
// and return the new length.
// Do not allocate extra space for another array, you must do this in place with constant memory.
// For example, Given input array A = [1,1,2],
// Your function should return length = 2, and A is now [1,2].

#include <iostream>
using namespace std;
int main()
{
    const int len=5;
    unsigned int sorted_array[]={1, 1, 1, 3, 4};

    int pt_nodup, pt;
    int i;
    // pt=0;
    // pt_nodup=0;
    for(pt=1, pt_nodup=0; pt<len; pt++)
    {
        if (sorted_array[pt] == sorted_array[pt_nodup])
        {
            
        }
        else{
            sorted_array[pt_nodup] = sorted_array[pt];
            pt_nodup++;

        }
        std::cout<<"pt="<<pt<<endl;
    }

    std::cout<<"length = "<<pt_nodup+1<<std::endl;
    for(pt=0; pt<pt_nodup; pt++)
        std::cout<<pt<<": "<<sorted_array[pt]<<endl;
    return 1;
}
