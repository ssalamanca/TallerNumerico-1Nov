from math import*
import numpy as np

def f(x,y):return 2*y-2*(x**2)+x-3
def g(x1):return x1/2+(x1**2)-11/20*exp(2*x1)+7/4
h=0.1
x = np.arange( 0, 4, h )          
y = np.zeros((4+1,))               
y[0]=1.2
x[0]=2
print('%18.15s %18.15s %18.15s'%("Runge-Kutta","real","error"))
for i in range(1,4+1):            
    k1 = h * f( x[i-1], y[i-1] )
    k2 = h * f( x[i-1] + h / 2, y[i-1] + k1 / 2 )
    k3 = h * f( x[i-1] + h / 2, y[i-1] + k2 / 2 )
    k4 = h * f( x[i], y[i-1] + k3 )
    y[i] = y[i-1] + ( k1 + 2.0 * k2 + 2.0 * k3 + k4 ) / 6.0
    I=y[i]
    r=g( x[i])
    e=r-I
    
    print('%18.15f %18.15f %18.15f'%(I,r,e))
