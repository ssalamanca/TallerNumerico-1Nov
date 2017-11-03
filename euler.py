[7:44 PM, 11/2/2017] Nicolas: from math import*
def f(x,y):return 2*y-2*(x**2)+x-3
def g(x):return x/2+(x**2)-11/20*exp(2*x)+7/4
y=1.2
x=0
h=0.1
I=x+f(x,y)*h
r=g(x)
e=I-r
print('%18.15s %18.15s %18.15s'%("metodo euler","real","error"))
print('%18.15f %18.15f %18.15f'%(I,r,e))
for j in range(4):
    x+=h
    In=I+f(x,I)*h
    I=In
    r=g(x)
    e=I-r
    print('%18.15f %18.15f %18.15f'%(I,r,e))
