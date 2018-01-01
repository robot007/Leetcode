'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
Example program
Time:  O(n)
Space: O(1)

'''
A=[1,1,2,2,4,5,5]
left=0
for right in range(1,len(A)):
    if A[left]!=A[right]:
        left+=1
        A[left]=A[right]
A_clean=A[0:left+1] # note: A[start:length] or A[start:end].
print(A_clean)
