import numpy as np
ls = [1,4,3]
print(np.array(ls))

ls2 = [[1,2,3],[1,2,3],[4,5,7]]
print(np.array(ls2))

print(np.arange(1,100))

print(np.arange(1,100,5))

print(np.zeros(3))

print(np.zeros((5,5)))

print(np.ones(5))

print(np.ones((5,7)))

print(np.identity(3))

print(np.linspace(1,100,5))

print(np.random.rand())

print(np.random.rand(1))

print(np.random.rand(1,2))

print(np.random.randn())

print(np.random.randint(1,8))

print(np.random.randint(1,8,10))

#Array Attributes and Methods
arr= np.arange(25)
randarr= np.random.randint(1,100,5)
print(arr)

print(randarr)

print(randarr.min())

print(randarr.max())

print(randarr.argmax())

print(randarr.argmin())

print(randarr.shape)

print(randarr.dtype)

print(randarr[1])

ls2 = [[1,2,3],[1,2,3],[4,5,7]]
print(ls2[1:3])

ls2=np.array(ls2)
print(ls2)

print(ls2[1:2])

print(ls2[1:2])

y = ls2[:,0] = 1
print(ls2[y,:])