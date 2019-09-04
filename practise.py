#Git test 
#python practise
import random
import sys
import os


print("Hello Wor ld")
print(17//4);
a = 10 ; 

#strings
str1 = "Yes it's str1 containing \""
str1_m = '''#its a multi
#line str1_m 
''' 

print("%s %s %s" %('%s string',str1, str1_m))
print(str1)
print(str1_m)
print("abc is abc", end="")  # eliminate new line
print("fgh is fgh")

#list
list1 = ['abc', 'fgh', 'jkl', 'aaa', 'bbb']
list2= ['ccc', 'ddd', 'eee', 'cc']
print(list1[0])
list1[1] = "mango"
print(list1[1:4])     #item 4 ignored
print([list1,list2]) #concatinate list
list3= [list1,list2] 
print(list3[1][1])
print(list3[1][2])
print(list3[1][0])

list2.append('fff')
print(list2)
list2.insert(0, 'aa')
print(list2)
list2.reverse()
print(list2)
list2.sort()
print(list2)
del list2[1]
print(list2)
# remove, len, max, min, (min in alphabetwise), + (join list)

#tuple, data dont want to be changed
tuple1 = 1,2,3,4,5
print(tuple1)
list4 = list(tuple1)
#len, min, max tuple1
print(list4)

#Dictonaries
dict1 = {'a':1, 'b':2, 'c':3 }
print(dict1['a'])
del dict1['b']
dict1['c'] = 5 
#len(dict1), get(dict1('a'))
print(dict1.keys())
print(dict1.values())

#if else elif 
age = 18 
if age>21 :
    print('correct')
elif age < 21:
    print("wrong")
age1 = 2
if(age1>1 and age1<21):
    print('yes')
else:
    print('no')

for i in range(0,11) :
    print(i," " ,end="")
print("\n")
list5 = ['aa', 'ss', 'dd']
for i in list5 :
    print(i," " ,end="")
    
print('\n')
list6 = [[1,2,3],[6,7,8]]
for i in range(0,2):
    for j in range(0,3):
        print(list6[i][j]," " ,end="")

rand1 = random.randrange(0,11)
while(rand1 != 10):
    print(rand1," " ,end="")
    rand1 = random.randrange(0,11)

#functions 
def sum(a,b):
    sum = a + b 
    return sum 
    
d= sum(1,2)
print(d)
  
print("name?")
name = sys.stdin.readline() 
print('Hello', name)

str2 = "This is a sample"
str3 = 'Flowervase'
print(str2[:2])
print(str2[:-2])
print(str2[-5:])
# str2.capitalize() first letter 
print(str2.find("sample")) # position 
print(str3.isalpha())
#isalnum all numbers, len(str3)
# str2.replace("Sample", "newword")
# str2.strip strip white spaces
list7 = [str2.split(" ")]
print(list7)

# fh = open("test.txt", "r+")
fh_text = fh.read() 
print(fh_text)
fh.close()
#.write, .remove

