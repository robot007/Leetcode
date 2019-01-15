# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

## 7:32~7:37
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=[float(v) for v in nums1]
        nums2=[float(v) for v in nums2]
        m=len(nums1)
        n=len(nums2)
        p1s=0
        p1l=m-1
        p2s=0
        p2l=n-1
        while max(nums1[p1s], nums2[p2s]) < min(nums1[p1l], nums2[p2l]):
            if p1s<p2s:
                p1s+=1
            else:
                p2s+=1
            if p1l>p2s:
                p1l-=1
            else:
                p2l-=1

        if max(nums1[p1s], nums2[p2s]) == min(nums1[p1l], nums2[p2l]):
            # if nums1[p1s]>nums2[p2s]:
            #     return nums1[p1s]
            # else:
            #     return nums2[p2s]
            return max(nums1[p1s], nums2[p2s])
        else:
            s=max(nums1[p1s], nums2[p2s])
            l=min(nums1[p1l], nums2[p2l])
            return (s+l)/2

if __name__=='__main__':
    sol=Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1, nums2))

    nums3=[1, 2]
    nums4 = [3, 4]
    print(sol.findMedianSortedArrays(nums3,nums4))