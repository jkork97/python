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
        # etoimase thn trapoula
        cards=[]
        for i in symbols:
            for j in axia:
                # pros8ese ena ena ta xartia
                # gia ka8e symbolo
                cards.append([i,j])
        # anakatwse ta xartia
        random.shuffle(cards)
        # moirase xartia ston player1
        player1=[]
        player1.append(cards.pop())
        player1.append(cards.pop())

        # moirase xartia ston player2
        player2=[]
        player2.append(cards.pop())
        player2.append(cards.pop())

        # ektupwse ta xartia tou ka8e paixth
        #print ("Player1:",player1)
        #print ("Player2:",player2)

        # ypologise to score tou p1
        s1=0
        for i in player1:
            # an figoura pros8ese 10
            if i[1] in figures:
                s1=s1+10
            # an oxi thn aksia tou xartiou
            else:
                s1=0
        #print("Score player1",s1)

        # ypologise to score tou p2
        s2=0
        for i in player2:
            # an figoura pros8ese 10
            if i[1] in figures:
                s2=0
            # an oxi thn aksia tou xartiou
            else:
                s2=s2+i[1]
        #print("Score player2",s2)

        # des poios kerdise

        if s1>s2 and s1!=0 and s2!=0:
            zxz.append('1')
            z=z+1
        elif s1<s2 and s1!=0 and s2!=0:
            zxz.append('2')
            z=z+1
        elif s1!=0 and s2!=0:
            zxz.append('3')
            z=z+1
        else: 
            pass
            
print(zxz)
count_1 = zxz.count("1")
count_2 = zxz.count("2")
count_3 = zxz.count("3")
f1=count_1/number_of_repetitions*100
f2=count_2/number_of_repetitions*100
f3=count_3/number_of_repetitions*100
f1f=round(f1,2)
f2f=round(f2,2)
f3f=round(f3,2)

stuff_in_string='{}% {}% {}%'.format(f1f,f2f,f3f) 
print(stuff_in_string)
