import numpy as np

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))


print(x1)
print("x1 ndim: ", x1.ndim) # nombre de dimensions total
print("x1 shape: ", x1.shape) # taile de chaque dimension
print("x1 size: ", x1.size) # size de tableau (nombre des elements total)
print("-------------")
print(x2)
print("x2 ndim: ", x2.ndim)
print("x2 shape: ", x2.shape)
print("x2 size: ", x2.size)
print("-------------")
print(x3)
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)

a=np.array(range(10),float)
print("a: \n", a)

b = a.reshape(5,2)
print("b: \n", b)

c = np.array([[2, 1, 2],[-5, 4, 5]],float)
print("c: \n", c)
d = c
e = c.copy()
print("e, copy de c: \n", e)

c = c.flatten()
print("c flatten: \n", c)

n = np.arange(5,dtype=float)
print("n:\n",n)
p = np.arange(0,4,1,dtype=int)
print("p: \n", p)

# on peut faire les operations comme les autres types

k = sorted(c)
print("k: \n",k)

print("-----------PLOT----------")
import matplotlib as mpl
import matplotlib.pyplot as plt

I = [1, 2 , 3]
for item in I:
    print(item)

h = [1,2,3,10]
y = [-1,-5, 0, 7]
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption")
#plt.plot(h,y, "ob") # points
#plt.plot(h,y)

"""
x = np.linspace(1, 10 ,100)
plt.subplot(2,1,1)
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
"""

plt.show()