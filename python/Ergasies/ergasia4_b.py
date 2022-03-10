import random

print('how many time to repeat the game2')
number_of_repetitions = int(input ())
z=0
zxz=[]
final=number_of_repetitions-1
while z <= final: 
        
    figures=["J","Q","K"]
    numbers=list(range(1,11))
    axia=numbers+figures
    symbols=["D","H","C","S"]
    cards=[]
    for i in symbols:
        for j in axia:
            cards.append([i,j])
    random.shuffle(cards)

    player1=[]
    player1.append(cards.pop())

    player2=[]
    player2.append(cards.pop())


    s1=0
    for i in player1:
    
        if i[1] in figures:
            s1=10
        else:
            s1=0
    s2=0
    for i in player2:
        
        if i[1] in figures:
            s2=0
        else:
            s2=i[1]

    if s1!=0 and s2!=0:
        player1.append(cards.pop())
        player2.append(cards.pop())
        s1=0
        for i in player1:
                
            if i[1] in figures:
                s1=s1+10
            else:
                s1=s1+i[1]
            #print("Score player1",s1)
            s2=0
        for i in player2:
            if i[1] in figures:
                s2=s2+10
            else:
                s2=s2+i[1]
            #print("Score player2",s2)
    else:
        s1=99
        s2=99

    if s1>s2 and s1!=0 and s2!=0 and s1<=90:
                zxz.append('1')
                z=z+1
    elif s1<s2 and s1!=0 and s2!=0 and s1<=90:
                zxz.append('2')
                z=z+1
    elif s1!=0 and s2!=0 and s1<=90:
                zxz.append('3')
                z=z+1
    else: 
        pass
            
#print(zxz)
count_1 = zxz.count("1")
count_2 = zxz.count("2")
count_3 = zxz.count("3")
f1=count_1/number_of_repetitions*100
f2=count_2/number_of_repetitions*100
f3=count_3/number_of_repetitions*100
f1f=round(f1,2)
f2f=round(f2,2)
f3f=round(f3,2)

stuff_in_string='O 1os paixths kerdise {} fores stis {} epanalispeis h alliws {}%.\nO 2os paixths kerdise {} fores stis {} epanalispeis h alliws {}%.\nIsopalia     eixame    {} fores stis {} epanalispeis h alliws {}%'.format(count_1,number_of_repetitions,f1f,count_2,number_of_repetitions,f2f,count_3,number_of_repetitions,f3f) 
print(stuff_in_string)

