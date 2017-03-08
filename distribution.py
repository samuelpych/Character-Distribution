"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
alphabet=list(string.ascii_lowercase)


letter=input("Please enter a string of text (the bigger the better): ")
print("The distrubution of characters in \"" +letter+ "\". is:")
letter=letter.lower()
#print(letter)
letter=list(letter)
#print(letter)
k=0
while(k<len(letter)):
    if(letter[k] in alphabet):
        letter[k]=letter[k]
    else:
        letter[k]=100
    k+=1
print(letter)
"""
((letter).count('a'))
((letter).count('b'))
((letter).count('c'))
((letter).count('d'))
((letter).count('e'))
((letter).count('f'))
((letter).count('g'))
((letter).count('h'))
((letter).count('i'))
((letter).count('j'))
((letter).count('k'))
((letter).count('l'))
((letter).count('m'))
((letter).count('n'))
((letter).count('o'))
((letter).count('p'))
((letter).count('q'))
((letter).count('r'))
((letter).count('s'))
((letter).count('t'))
((letter).count('u'))
((letter).count('v'))
((letter).count('w'))
((letter).count('x'))
((letter).count('y'))
((letter).count('z'))

for x in letter:
    if letter==" " or letter=="." or letter=="?" or letter=="," or letter==";"  or letter==":" or letter=="!":
"""
