"""
distribution.py
Author: Sam
Credit: Ethan and Earl

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
numbers = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']


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
        letter[k]=-1
    k+=1

k=0
a=int(alphabet.index(letter[0]))
while(k<=len(letter)):
    if letter[k]== (-1):
        k=k
    elif(a<=alphabet.index(letter[k])):
        a=a
    else: a=letter[k]
    k+=1
print(alphabet[a])
