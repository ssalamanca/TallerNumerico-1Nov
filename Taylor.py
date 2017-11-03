import numpy as np
import matplotlib.pyplot as plt
import math

def factorial( n ):
    if n == 0:
        return 1
    fact = 1
    for i in range( 1, n+1 ):
        fact *= i
    return fact
 
def taylor( f, a, b, N, IV ):
    h = (b-a)/float(N)                  # determine step-size
    t = np.arange( a, b+h, h )          # create mesh
    w = np.zeros((N+1,))                # initialize w
    t[0], w[0] = IV                     # set initial values
    for i in range(1,N+1):              # apply Euler's method
        T = 0
        for j in range(len(f)):
            h_factor = h**(j)/float(factorial(j+1))
            T += h_factor * f[j]( t[i-1], w[i-1] )
        w[i] = w[i-1] + h * T
    return w

a, b = 0.0, 2.0
N = 10
h = (b-a)/N
IV = ( 0.0, 0.5 )
t = np.arange( a, b+h, h )
 
f   = lambda x, y: x / 2 + x**2 - 11/20 * math.exp(2*x)
df  = lambda x, y: 2*y - 2*x**2 + x - 3
ddf = lambda x, y: y - x**2.0 - 2*x - 1
 
w2 = taylor( [ f, df ], a, b, N, IV )
w3 = taylor( [ f, df, ddf ], a, b, N, IV )
plt.plot( t, w2, label='2nd order' )
plt.plot( t, w3, label='3rd order' )
#plt.plot( t, y(t), label='exact' )
plt.xlabel('x') 
plt.ylabel('y(x)')
plt.legend(loc=4)
plt.grid()
plt.show()
plt.savefig( 'taylor_example.png', fmt='PNG', dpi=100 )
