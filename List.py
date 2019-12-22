#List

>>> square='Square'
>>> wore='Programming'
>>> len(square)+len(wore)
17
>>> word='Programming'
>>> len(word)
11
>>> cube=[10,20,30,40,50]
>>> cube[5]=60 #Error
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cube[5]=60
IndexError: list assignment index out of range
>>> cube.append(60)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.append(4+10+20+36)
>>> cube
[10, 20, 30, 40, 50, 60, 70]
>>> cube.append(80,90)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    cube.append(80,90)
TypeError: append() takes exactly one argument (2 given)
>>> ProgramA= ['A','B','C','D','E']
>>> ProgramB= ['a','b','c','d','e']
>>> programC = ProgramA + ProgramB
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> ProgramD = [1,2,3,4,5]
>>> programC = programC + ProgramD
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
>>> programC[:9]=[]
>>> programC
['e', 1, 2, 3, 4, 5]
>>> programC[5:9]= ProgramD
>>> programC
['e', 1, 2, 3, 4, 1, 2, 3, 4, 5]
>>> programC[:]=ProgramA+ProgramB+ProgramD
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
>>> programC[9:]=[]
>>> programC[5:9]=ProgramD
>>> programC
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]
>>> 