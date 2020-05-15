# QuickSort
import numpy as np
# 8:16
def qsort(A, lo, hi):
    if lo<hi:
        p = partition( A, lo, hi)
        print(f'A={A}, lo={lo}, hi={hi}, p={p}')
        qsort(A, lo, p)
        qsort(A, p+1, hi)
  

def swap(a, b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)

def partition(A, lo, hi):
    lo = int(lo)
    i = lo
    hi = int(hi)
    j = hi
    p = int( (lo+hi)/2 )
    bypass=False
    while lo < hi:
        print(f'A={A}, lo={lo}, p={p}, hi={hi}, A[lo]={A[lo]}, A[p]={A[p]}, A[hi]={A[hi]} ')        
        while A[lo] <= A[p] and lo<p:
            lo+=1
            bypass = True
            # break
        while A[hi] >= A[p] and hi>p:
            hi-=1
            bypass = True
            # break
        if bypass==False:
            if i>j:
                return j
            else:
                print(f'B: swap A[{i}] with A[{j}]')
                a,  b = swap(A[i], A[j])
                A[i]=a
                A[j]=b
                print(f'A: A={A}')
        i = lo
        j = hi
        bypass=False
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
    print('before: A='+str(A))
    qsort(A, 0, len(A)-1)
    # print('after: A='+ str(A))

if __name__=='__main__':
    test()