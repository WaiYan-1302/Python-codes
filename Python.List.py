Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> squares = [1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> square[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    square[5]
NameError: name 'square' is not defined
>>> squares[4]
25
>>> squares[-1]
25
>>> squares[-5]
1
>>> squares[-3]
9
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36,49,64,81,100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> number=[1 4 9 16 25]
SyntaxError: invalid syntax
>>> number=[1491625]
>>> number+3
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    number+3
TypeError: can only concatenate list (not "int") to list
>>> number+[3]
[1491625, 3]
>>> cubes = [1,8,27,65,125]
>>> 4**3
64
>>> cubes[3]=64
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)
>>> cubes.append(7**3)
>>> cubes.append(8**3,9**3,10**3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    cubes.append(8**3,9**3,10**3)
TypeError: append() takes exactly one argument (3 given)
>>> cubes.append(8**3)(9**3)(10**3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cubes.append(8**3)(9**3)(10**3)
TypeError: 'NoneType' object is not callable
>>> cubes
[1, 8, 27, 64, 125, 216, 343, 512]
>>> letters=['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5]
['c', 'd', 'e']
>>> letters[2:5]=['C','D','E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5]
['C', 'D', 'E']
>>> letters[:]=[]
>>> letters
[]
>>> letters[:]=['A','B','C','D','E','F','G']
>>> len(letters)
7
>>> a=['a','b','c','d']
>>> n=[1,2,3,4]
>>> x=[a,n]
>>> x
[['a', 'b', 'c', 'd'], [1, 2, 3, 4]]
>>> x[0]
['a', 'b', 'c', 'd']
>>> x[0][3]
'd'
>>> x{1][3]
SyntaxError: invalid syntax
>>> x[1][3]
4
>>> 
