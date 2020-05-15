# DP
# Fibnacci numbers

#%%
def fib(n, table):
    # memorization
    if n==0 or n==1:
        table[n]=n
        return n
    table[n]=fib(n-1, table)+fib(n-2, table)
    return table[n]

if __name__=='__main__':
    table = [None]*100
    print(fib(40, table))

