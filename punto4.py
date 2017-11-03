def f(x,y,z):
    return x+y+z
def g(x,y,z):
    return -x+y-z

#x0 = float(input('Ingrese x0 : '))
#y0 = float(input('Ingrese y0 : '))
#z0 = float(input('Ingrese z0 : '))
m=40
h=0.1
h1=0.001
x0 = 0
y0 = 1
z0 = 2
x1 = x0
y1 = y0
z1 = z0
print('%18s %18s %18s %18s'%("Variable X","Variable Y ","Variable Z","h"))
for i in range (1,m):
    k1y = h*f(x0,y0,z0)
    k1z = h*g(x0,y0,z0)

    k2y = h*f(h+x0 , h+y0, h+z0)
    k2z = h*g(h+x0 , h+y0, h+z0)

    y0 = y0+(0.5*(k1y+k2y))
    z0 = z0+(0.5*(k1z+k2z))
    x0 = x0+h
    print('%18s %18s %18s %18s'%(x0,y0,z0,h))
    
print(" ")
print('%18s %18s %18s %18s'%("Variable X","Variable Y ","Variable Z","h"))
for j in range(1,m):
    k1y = h1*f(x1,y1,z1)
    k1z = h1*g(x1,y1,z1)

    k2y = h1*f(h1+x1 , h1+y1, h1+z1)
    k2z = h1*g(h1+x1 , h1+y1, h1+z1)

    y1 = y1+(0.5*(k1y+k2y))
    z1 = z1+(0.5*(k1z+k2z))
    x1 = x1+h1
    print('%18s %18s %18s %18s'%(x1,y1,z1,h1))
