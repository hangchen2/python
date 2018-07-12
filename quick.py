############################################# util #############################################
if __name__ == '__main__': arr = input().split()     #command line parser
  
range(beg,end,step), range(n)  #range(1,5,1) = [1,2,3,4] range(3) = [0, 1, 2]
import sys, sys.maxsize #max default size in python 3, python 2 can use sys.maxint
  
#lamda(lambda arguments: expression) 
double = lambda x: x * 2  print(double(5))   #10

#filter(function, list)
l = filter(lambda x : x % 2 == 1, range(1, 20)) #filter odds
l = filter(lambda x : x < 0,      range(-5,5))  #filter negatives
l = filter(lambda x: x in l1, l2)               #common elements from two lists

#map(function, list) apply the function on all items of the list
my_list = [1, 5, 4, 6, 8, 11, 3, 12] 
new_list = list(map(lambda x: x * 2 , my_list)) print(new_list) # Output: [2, 10, 8, 12, 16, 22, 6, 24]
sum(map(sum,arr)) #sum of 2D array or matrix    

ord() #char to unicode, ord('5') = 53 and ord('A') = 65
chr() #unicode to char
type()   #returns the data type
accumulate(l)                                 #returns cumulativeSum of a list
zip()                                         # l1 = ['a','b'], l2 = [1,2], zip(l1,l2) gives {('a',1),('b',2)}
math.modf(2)                                  #(0.0, 2.0) returns the fractional and integer parts of the number in a two-item tuple
hash()                                        #a hash is an fixed sized integer that identifies a particular value

############################################# list #############################################
#ordered collection, iterable, inhomogeneous, mutable, duplicate yes    
l = list(), l = [], l = [1,2,'a']                     #creation      
len(l)
l.append(element)
lst1.extend(lst2)
l.clear()
del[a:b]   #delete elements in range
l.pop(index) #delete at index
l.insert(element, index ) #insert data at position
l.remove(element) #remove 1st occurrence
l.sort(), l.sort(reverse=True), l.sort(key=len) #changes orignial list, ascending, descending, by element len
sorted(l), sorted(l, reverse=True), sorted(l, key=len) #return new list, orignial list unchanged
l.sort(key=lambda x: x.id) #sort list of objects
l.reverse() #reverse a list
l.copy() #shallow cpy
l.count(element) #number of occurrence 
in, not in   # operator check presence
len(l), min(l), max(l)
l.index(e), l.index(min(l)) #get index of element, index of the min element
l1 + l2, l * n  #concatenate, repetition
index(element, beg, end)  #returns the index of first occurrence of element in range
sum(l)
if l           #check if empty
float(sum(l)) / len(l)  #average
sorted(list(set(s)))[1] #2nd min
func(*list)            #pass list as arguement

############################################# string #############################################
#immutable 
s1+s2+s3                                                                           #concatenation 
s1 and s2, s1 or s2                                                                #union, intersection
s[beginning: end : step]                                                           #slicing, s='abcde', s[1:3:1] = 'bc'
s1.find(s2, beg=0,end=len(s1)) s1.rfind (s2, beg=0,end=len(s1))                    #return first/last occurrence index, returns -1 if not found 
s1.endswith(s2,beg=0,end=len(s1))                                                  #check if 1s ends with s2
islower(s), isupper(s)                                                             #check if all letters are lower/upper cased
s.lower(),s.upper(),s.swapcase(),s.title()                                         #convert case
len(s)                                                                             #length of string  
s1.count(s2,beg=0,end=len(s1))                                                     #count substring appearances
s.center(length, char), s.ljust(length, char), s.rjust(length, char)               #adjust by adding char 
s.isalpha(),s.isalnum(),s.isspace(), s.isdigit()                                    #check if all alpha, alpha or numeric, space
s.join(seq)                                                                        #seq can be string or list etc
s.strip(c), s.lstrip(c), s.rstrip(c)                                               #delete all leading and/or trailing character
min(s), max(s)                                                                     #get min/max alphabet value 
s.replace(s1,s2,howmany=unlimited)                                                 #replace s1 with s2 in s
s.split(delimiter)                                                                 #split
print(“%format”  % variable ), %d integer, %f float, %s string, %x hex, %o octal   #formatting
import re, re.match(pattern, s), re.findall(pattern, s)                            #regular expression
def mfunc(): “””docstring in triple quotes”””, print mfunc.__doc__                 #docstrings
sorted(s, key=str.lower)                                                           #sort lexicographically                     


############################################# dictionary #######################################
#similar to hash or maps in other languages, It consists of key value pairs. Key is unique
d = dict(), d = {}, d = {'a':1, 'b':2}                  #creation
len(d)                                                  #count of keys
str(d)                                                  #return all key value as a string
d.items()                                               #return all key value as a list      
d.copy()                                                #shallow copy, d2 = list(d1) for deep copy
d.clear()                                               #clear contents
d.get(key, default=None)                                #access with default if not found
if key in my_dict: my_dict[key] += 1,  else: my_dict[key] = 1  #if found add one, otherwise set to 1
d.has_key(k)   #check key present
d.setdefault(k, default_value) #like get but add if not present
from collections import OrderedDict, d = OrderedDict()  #preseves the order in which keys are inserted

############################################# tuple #############################################
#ordered collection, iterable, inhomogeneous, immutable, duplicate yes 
t = tuple(), t = (), t = (1,2,'a'), t = tuple(list)       #creation
t1 + t2                                                   #concatenation  
t3 = (t1, t2)                                             #nesting
t2 = t1 * 3                                               #repetition
t = (0, 1, 2, 3), t[1] = 4                                #immutable, TypeError: 'tuple' object does not support item assignment
del t                                                     #deletion
t = (0 ,1, 2, 3) print(t[1:]) print(t[::-1]) print(t[2:4]) # slicing(1, 2, 3) (3, 2, 1, 0) (2, 3)
len(t)                                                    #length
t.count(element)                                          #count number of appearances of an element

############################################# set #############################################
#unordered collection, iterable, mutable, duplicate no
s = set(), s = set(list/dict/tuple...)                      #Creation 
s.add(element)                                              #add
s.clear()                                                   #clear
set(l1).difference(l2)                                      #in l1 but not l2
key in s                                                    # containment check
key not in s                                                # non-containment check
s1 == s2, s1 != s2                                          # equilvalence
s1 <= s2                                                    # subset check
s1 | s2                                                     # union
s1 & s2                                                     # intersection 
s1 – s2                                                     # in s1 but not s2
s1 ˆ s2                                                     # precisely in one of s1 or s2
