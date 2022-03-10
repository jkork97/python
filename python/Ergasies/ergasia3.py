from itertools import count
import re

whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  
file_path = ".\data.txt"

with open(file_path) as text_file:
    myStr = text_file.read()
        

x1 = myStr.replace('.', ' ')
x3 = x1.replace('\n', ' ')
x4 = re.sub(' +', ' ', x3)

answer = ''.join(filter(whitelist.__contains__, x4))
x5 = answer.split(" ")

print(x5)

x6=x5
i=0
for x in x5[i]:
    for x in x5[i+1]:
            if len(x5[i]) + len(x5[i+1]) == 20:
                x6[i]=''
                x6[i+1]=''
                i=i+2
            else:
                x6[i]=x5[i]
                i=i+1
#print(x6[1])
#print(x6[2])
#print(x6[3])

#number_of_wordz= total words with spaces and other non-words
#wrong_wordz=spaces created after elimination of couple of words with total lenght 20
#number_of_words=total words left

number_of_wordz = len(x5)
wrong_wordz= x6.count('')
number_of_words = number_of_wordz-wrong_wordz

x7=x6
i=0
for x in x6:
    x7[i]= len(x6[i])
    #print(x7[i])
    i=i+1
    if i==number_of_wordz:
        break

#convert string list to integer list for count function to work properly
integer_map =map(int, x7)
x8=list(integer_map)
i=0
for x in x7:
    x8[i]= x7.count(i)
    #print(x8[i])
    i=i+1   
    if i==25:
        break
    
i=1
for x in x8:
    fa=(x8[i]/number_of_words)*100
    fb=round(fa,2)
    stuff_in_string3='Words with {} letter(s) are {}% of total words({})'.format(i,fb,x8[i]) 
    print(stuff_in_string3)
    i=i+1
    if i==25:
        break
