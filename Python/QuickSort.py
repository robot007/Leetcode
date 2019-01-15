# QuickSort
import numpy as np
# 8:16
def qsort(A, lo, hi):
    if lo<hi:
        p = partition( A, lo, hi)
        print(f'A={A}, lo={lo}, hi={hi}, p={p}')
        qsort(A, lo, p)
        qsort(A, p+1, hi)
    else:
        print('leaf end')    

def swap(a, b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)

def partition(A, lo, hi):
    lo = int(lo)
    hi = int(hi)
    p = int( (lo+hi)/2 )
    while lo < hi:
        print(f'p={p}, lo={lo}, hi={hi}, A[p]={A[p]}, A[lo]={A[lo]}')        
        while A[lo] <= A[p]:
            lo+=1
        while A[hi] >= A[p]:
            hi-=1
        if lo>hi:
            p=hi
            return p
        else:
            print(f'B: swap A[{lo}] with A=[{hi}]')
            (A[lo], A[hi]) = swap(A[lo], A[hi])
            print(f'A: A={A}')
        # if A[hi] >= A[p]:
        #     hi -= 1
        # elif A[lo] <= A[p]:
        #     lo += 1
        # elif A[lo]>A[p] and A[hi]<A[p]:
        #     A[lo] += A[hi]
        #     A[hi] = A[lo]-A[hi]
        #     A[lo] = A[lo]-A[hi]
        #     lo += 1
        #     hi -= 1
        # elif A[lo]>A[p]:
        #     A[lo], A[p] = swap(A[lo], A[p])
        # elif A[hi]<A[p]:
        #     A[lo], A[p] = swap(A[lo], A[p])
    return p

def test():
    A=[5, 4, 8, 3, 2, 1]
    print('beofre: A='+str(A))
    qsort(A, 0, len(A)-1)
    # print('after: A='+ str(A))

if __name__=='__main__':
    test()