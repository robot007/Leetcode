import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


def ridge_plot():
    # X is the 10x10 Hilbert matrix
    ## MM: arange([from,] to [,step])
    X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
    y = np.ones(10)

    # #############################################################################
    # Compute paths

    n_alphas = 200
    alphas = np.logspace(-10, -2, n_alphas)

    coefs = []
    for a in alphas:
        ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
        ridge.fit(X, y)
        coefs.append(ridge.coef_)

    # #############################################################################
    # Display results

    ax = plt.gca()
    plt.ion()
    ax.plot(alphas, coefs)
    ax.set_xscale('log')
    # ax.set_xlim(ax.get_xlim()[::-1])  # reverse axis
    plt.xlabel('alpha')
    plt.ylabel('weights')
    plt.title('Ridge coefficients as a function of the regularization')
    plt.axis('tight')
    plt.show()

def optional_para1(a,b, *args, **kwargs):
      c = kwargs.get('c', None)
      d = kwargs.get('d', None)
      print(c)
      print(d)
      #etc
def optional_para2(a,b,*args, **kwargs):
    for ar in args:
        print(ar)

def add_to_mutable(num, target=[]):
    target.append(num)
    return target        

# namedtuple
from collections import namedtuple
def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)

def find_val():
    a = np.arange(1,10)
    l = [ ('less then or equal to 3', 'bigger then 3')[bool(v>3)] for v in a ]
# In [50]: type(t[0]>3)
# Out[50]: numpy.bool_

# In [51]: type(bool(t[0]>3))
# Out[51]: bool
    print(l)

from pprint import pprint
def np_val():
    '''
    ## https://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u
    # for ndarray, @, T, **, 
    # for mat, assign '1,2; 3,4'
    '''
    print('in np_val()')
    a1=np.array(range(6))[:, np.newaxis]
    a0=a1.reshape((1,6))
    a2=a1
    # print in one line
    print('a2 is a reference of a1. id(a1)={}, id(a2)={} '.format(id(a1), id(a2))),  print(f'id(a0)={id(a0)}')
    a2[0,0]=12
    print(f'a1[0,0] is changed due to a2[0,0] assignment. a1[0,0]={a1[0,0]:4d}, a2[0,0]={a2[0,0]}')
    print(f'matrix product a1@a0=\n{a1@a0}, or np.dot(a1,a0)=\n{ np.dot(a1,a0) }. dot product is \n{ a1*a0 }')

if __name__ == "__main__":
    ridge_plot()

    print('optional parameters')

    ## Python tips
    optional_para1(1,2,c=3,d=4)
    optional_para2(1,2,3.1,4.1)
    # mutable objects are copy by references. For deep copy, use copy.deepcopy() 
    ## immutable classes are limited 10 types https://www.pythonforthelab.com/blog/mutable-and-immutable-objects/#mutable-and-immutable-data-types
    print(add_to_mutable(1))
    print(add_to_mutable(2))
    print(add_to_mutable(3))

    print(profile())
    p=profile()
    print(p)

    find_val()

    np_val()
    pass