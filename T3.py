Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> z="hi how are you?"
>>> num_r=z.replace('h','g')
>>> print("num_r=",num_r)
num_r= gi gow are you?
>>> num_h=len(z)
>>> print("num_h=",num_h)
num_h= 15
>>> num_k=len(z.split(" "))
>>> print("num_k=",num_k)
num_k= 4
>>> x="hi how are you?,im fine."
>>> num_j=len(x.split(","))
>>> print("num_j=",num_j)
num_j= 2
>>> 