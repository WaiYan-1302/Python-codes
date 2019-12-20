Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('\some\name')
\some
ame
>>> print(r'\some\name')
\some\name
>>> print('\some\n\\name')
\some
\name
>>> print("""\
Usage: thingy [OPTIONS]
 -h             Display this usage message
 -H hostname    Hostname to connect to
 """)
Usage: thingy [OPTIONS]
 -h             Display this usage message
 -H hostname    Hostname to connect to
 
>>> print("""\
Arduino Board           =8500 Ks
4Wheels Robot CarKit    =12000Ks
Motor Driver L298N      =3000 Ks
Bluetooth Module HC-05  =6000 Ks
""")
Arduino Board           =8500 Ks
4Wheels Robot CarKit    =12000Ks
Motor Driver L298N      =3000 Ks
Bluetooth Module HC-05  =6000 Ks

>>> 3 * 'un' + 'ium'
'unununium'
>>> 'ba' + 2 * 'na'
'banana'
>>> 'py' + 'thon'
'python'
>>> text = ('Put several strings within parentheses to have the joined together.')
>>> text
'Put several strings within parentheses to have the joined together.'
>>> prefix='Py'
>>> prefix+'thon'
'Python'
>>> word='Python'
>>> word[0]
'P'
>>> word[1]
'y'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[-5]
'y'
>>> word[0:2]
'Py'
>>> word[2:6]
'thon'
>>> word[0:6]
'Python'
>>> word[:6]
'Python'
>>> 'tri'+ word[2:]
'trithon'
>>> len(word)
6
>>> Strings='Min Min is a TTU student'
>>> len(Strings)
24
>>> 
