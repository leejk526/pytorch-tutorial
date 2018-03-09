# http://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
from __future__ import print_function
import torch

#x = torch.Tensor(5, 3)
#print(x)

x = torch.rand(5, 3)
print("x is ", x)

#print(x.size())
#print(x.size()[0])

y = torch.rand(5, 3)
print("y is ", y)
#print(x + y)
#print(torch.add(x, y))
result = torch.Tensor(5, 3)
torch.add(x, y, out=result)
print("result is ",result)

y.add_(x)
print("new y is (same as result)", y)

x = torch.randn(4, 4)
print("new x is ", x)
y = x.view(16)
z = x.view(-1, 8)
print("x.size() is", x.size())
print("y.size() is", y.size())
print("z.size() is", z.size())

# The Torch Tensor and NumPy array will share their underlying memory locations, and changing one will change the other.
a = torch.ones(5)
print("a is", a)

# converting torch tensor to numpy array
b = a.numpy()
print("b is", b)
print("b's type is", type(b))

a.add_(1)
print("new a is (shared with b)", a)
print("new b is ", b)

# converting numpy array to torch tensor
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print("numpy a is ", a)
print("torch b is ", b)


