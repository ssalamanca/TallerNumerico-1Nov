import matplotlib.pyplot as plt
def funcion(x,y):
    return y+x-(x**2)+1

h=0.0009
m=40
x0=0
y0=1
#x0 = float(input('Ingrese x0 : '))
#y0 = float(input('Ingrese y0 : '))
grafx=[]
grafy = []
funcReal=funcion(x0,y0)
grafx.append(x0)
grafy.append(y0)
print('%18s %18s %18s %18s %18s'%("Variable X","Variable Y ","Funcion","Funcion real","error"))
for i in range(1,m): 
    funcDif=funcion(x0,y0)
    
    k1=h*funcion(x0,y0)
    k2=h*funcion(x0+h,y0+h)
    y0=y0+(0.5*(k1+k2))
    x0=x0+h
    grafx.append(x0)
    grafy.append(y0)
    err=funcReal-funcDif
    print('%18s %18s %18s %18s %18s'%(x0,y0,funcDif,funcReal,err))
    
plt.plot(grafx,grafy)
plt.plot(grafx, grafy, 'k:', linewidth = 2)
plt.title('Solucion de una ecuacion diferencial')
plt.xlabel('Cambio en x0')
plt.ylabel('Cambio en y0')
plt.show()

