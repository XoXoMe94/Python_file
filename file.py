# -*- coding: utf-8 -*-
"""


@author: sara
"""
#ex1
#file open
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt' ,'r')
#consider it as a raw string. add r before your windows path.
handle =open(r'C:\Users\sara\Desktop\office 2021\sara.txt' ,'w')
print(fhand) #just detail
print(handle) #just detail



#ex2
# open whole file with  for 
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt')
for i in fhand:
    print(i) #print whole file
print('done')



#ex3
#counting lines
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt')
count=0
for i in fhand:
    count=count+1
    print('line:', count)
    
    

#ex4 read file
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt' )
a=fhand.read() 
print(a)
print(len(a))
print(a[:2])



#ex5 searching in file 
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt')
for i in fhand:
    i=i.lstrip()
    if i.startswith('s'):
        print(i)


 
#ex6 skipping in the file  
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt')
for i in fhand:
    i=i.lstrip()
    if not  i.startswith('s'):
       continue  
    print(i) #just print lines start with s



#ex7 skipping in the file  
fhand =open(r'C:\Users\sara\Desktop\office 2021\sara.txt')
for i in fhand:
    i=i.lstrip()
    if not 's' in i:
       continue  
    print(i) #just print lines start with s




#ex8 
fname=input ('Enter file name:')
fhand =open(fname)
count =0
for i in fhand:
    if  i.startswith('s'):
       count=count+1 
print("there were" ,count,"subject lines in", fname) 
    




#ex9 bad file name 
fname=input ('Enter file name:')
try:
    fhand =open(fname)
except:
    print('file can not be opened:', fname)
    quit()
count =0
for i in fhand:
    if  i.startswith('s'):
       count=count+1 
print("there were" ,count,"subject lines in", fname) 
