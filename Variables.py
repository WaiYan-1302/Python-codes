
#21Dec
>>> 2 + 2
4
>>> 17 // 3
5
>>> 17 / 3
5.666666666666667
>>> 18 // 4
4
>>> 20
20
>>> 3 ** 9
19683
>>> 7 ** 3
343
>>> 17 % 3
2
>>> width = 20
>>> height= 5 * 9
>>> width * height
900
>>> round (5.55)
6
>>> vol = width * height
>>> vol
900
>>> 4 *3.75 -1
14.0
>>> 4 * 3.75 - 1.25
13.75
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> price + 12.5625
113.0625
>>> round(113.0625, 2)
113.06
>>> sale = 30000
>>> tax = 5 / 100
>>> total tax = sale * tax
SyntaxError: invalid syntax
>>> total_tax = sale * tax
>>> total_price= sale + total_tax
>>> total_price
31500.0
>>> total_tax
1500.0
>>> ' spam eggs'
' spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> '"Yes,"they said.'
'"Yes,"they said.'
>>> "\"Yes,\"they said."
'"Yes,"they said.'
>>> print('spam eggs')
spam eggs
>>> print(""Yes"")
SyntaxError: invalid syntax
>>> print('"yes"')
"yes"
>>> print('"Isn\'t,"they said.")
      
SyntaxError: EOL while scanning string literal
>>> print("First Line\nSecond Line")
First Line
Second Line
>>> s = "First Line\nSecond Line"
>>> s
'First Line\nSecond Line'
>>> s= First Line\nSecond Line
SyntaxError: invalid syntax
>>> print(s)
First Line
Second Line
>>> print("""\
Usage: thingy
      -a
      -b
      -c
""")
Usage: thingy
      -a
      -b
      -c

>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' + 'thon'
'Python'
>>> 3 * 'A'
'AAA'
>>> 2 * 'BC' + 'DE'
'BCBCDE'
>>> 10 * 'GH' + 3
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    10 * 'GH' + 3
TypeError: can only concatenate str (not "int") to str
>>> 10 * 'GH' + '3'
'GHGHGHGHGHGHGHGHGHGH3'
>>> 10 * 'GH' - '3'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    10 * 'GH' - '3'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 'Py'+'thon'
'Python'
>>> Text = ('Put several strings within parentheses '
        'to have them joined together.')
>>> Text
'Put several strings within parentheses to have them joined together.'
>>> prefix = 'py'
>>> word = 'programming'
>>> word
'programming'
>>> word[0]
'p'
>>> word[8]
'i'
>>> word[7]
'm'
>>> word[-2]
'n'
>>> word[-9]
'o'
>>> word[3:5]
'gr'
>>> word[4;9]
SyntaxError: invalid syntax
>>> word[4:9]
'rammi'
>>> word[:5]
'progr'
>>> word[8:]
'ing'
>>> word[-2:5]
''
>>> word[5:-3]
'amm'
>>> word[:2]+word[3:]
'prgramming'
>>> word[:3]+word[3:]
'programming'
>>> 