from itertools import count

  
file_path = ".\data.txt"

with open(file_path) as text_file:
    myStr = text_file.read()
        
answer = myStr

def bit_make(answer):
    
    binary = ""
    for char in answer:
        num = ord(char)
        binary2 = bin(num)[2:]
        bits=binary2.zfill(7)
        binary+=bits
    return binary


def getMaxLength0(arr, n):
 
    count = 0
    result = 0
 
    for i in range(0, n):
     
        if (arr[i] == 0):
            count = 0
        else:
            count+= 1
            result = max(result, count)
         
    return result

def getMaxLength1(arr, n):
 
    count = 0
    result = 0
 
    for i in range(0, n):
     
        if (arr[i] == 1):
            count = 0
        else:
            count+= 1
            result = max(result, count)
         
    return result

          
myStr7 = bit_make(answer)
arr2=list(myStr7)
arr = [int(i) for i in arr2]
n = len(arr)
print(answer)
print(myStr7)
answer_for_0=getMaxLength0(arr, n)
answer_for_1=getMaxLength1(arr, n)
stuff_in_strings='Ta sunexomena 0 einai {}. \nTa sunexomena 1 einai {}.'.format(answer_for_0,answer_for_1) 
print(stuff_in_strings)



