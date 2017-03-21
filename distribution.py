"""
distribution.py
Author: Sam
Credit: Ethan, Earl, and Kezar

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
alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
letter=input("Please enter a string of text (the bigger the better): ")
print("The distrubution of characters in \"" +letter+ "\". is:")
letter=letter.lower()
thingweird=[]
for a in alphabet:
    fakeletter = letter.count(a)
    if not fakeletter == 0:
        thingweird.append(a*fakeletter)

for b in range (26):
    wub=0
    while wub < len(thingweird)-1:
        if len(thingweird[wub]) < len(thingweird[wub+1]):
            ire = thingweird[wub]
            thingweird[wub]=thingweird[wub+1]
            thingweird[wub+1]=ire
        ire+=1
for g in thingweird:
    print(g)
    
"""
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
    if int(a<alphabet.index(letter[k])):
        a=a
    else: a=letter[k]
    k+=1
print(alphabet[a])
"""
