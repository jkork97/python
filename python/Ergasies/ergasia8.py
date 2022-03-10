import random

print("oriste mhkos kai platos pinaka")

horizontal = int(input ())
vertical = int(input ())
print("oriste epanalipseis")
Repetitions=int(input ())
results=[]
rep=0
while Repetitions>rep:
    
    h=horizontal+1
    numbersx=list(range(1,h))
    v=vertical+1
    numbersy=list(range(1,v))
    #print(numbersx,numbersy)
    positions=[]
    for i in numbersx:
        for j in numbersy:
            positions.append([i,j])
    random.shuffle(positions)
    rook1=[]
    bishop1=[]
    rook1.append(positions.pop())
    bishop1.append(positions.pop())
    rook=rook1[0]
    bishop=bishop1[0]

    stuff_in_string='rook={},\nbishop={}'.format(rook,bishop) 
    #print(stuff_in_string)
    #first number is i second number is j
    bishop_moves=[]
    rook_moves=[]

    z=int
    if h>=v:
        z=horizontal
    else:
        z=vertical

    g=1
    p=0
    while z>p:
            
        p1=[g,g]
        p2=[g,-g]
        p3=[-g,g]
        p4=[-g,-g]
        
        bishop_moves_list1=[]
        for i in range(len(bishop)):
            bishop_moves_list1.append(bishop[i] + p1[i])
            bishop_moves.append(bishop_moves_list1)
        
        bishop_moves_list2=[]
        for i in range(len(bishop)):
            bishop_moves_list2.append(bishop[i] + p2[i])
            bishop_moves.append(bishop_moves_list2)
        
        bishop_moves_list3=[]
        for i in range(len(bishop)):
            bishop_moves_list3.append(bishop[i] + p3[i])
            bishop_moves.append(bishop_moves_list3)
        
        bishop_moves_list4=[]
        for i in range(len(bishop)):
            bishop_moves_list4.append(bishop[i] + p4[i])
            bishop_moves.append(bishop_moves_list4)   
        p=p+1
        g=g+1
    #print(bishop_moves) 
    

    j=1
    k=0
    while z>k:
            
        k1=[j,0]
        k2=[-j,0]
        k3=[0,j]
        k4=[0,-j]
        
        rook_moves_list1=[]
        for i in range(len(bishop)):
            rook_moves_list1.append(rook[i] + k1[i])
            rook_moves.append(rook_moves_list1)
        
        rook_moves_list2=[]
        for i in range(len(bishop)):
            rook_moves_list2.append(rook[i] + k2[i])
            rook_moves.append(rook_moves_list2)
        
        rook_moves_list3=[]
        for i in range(len(bishop)):
            rook_moves_list3.append(rook[i] + k3[i])
            rook_moves.append(rook_moves_list3)
        
        rook_moves_list4=[]
        for i in range(len(bishop)):
            rook_moves_list4.append(rook[i] + k4[i])
            rook_moves.append(rook_moves_list4)   
        k=k+1
        j=j+1
        
    #print(rook_moves)
    if rook in bishop_moves:
        #print('bishop wins')
        results.append('1')
        rep+=1

    elif bishop in rook_moves:
        #print('rook wins')
        results.append('2')
        rep+=1
    else:
        #print('draw')
        results.append('3')
        rep+=1

#print(results)
count_1 = results.count("1")
count_2 = results.count("2")
count_3 = results.count("3")
f1=count_1/Repetitions*100
f2=count_2/Repetitions*100
f3=count_3/Repetitions*100
f1f=round(f1,2)
f2f=round(f2,2)
f3f=round(f3,2)

stuff_in_string2='bishop wins {}% dhladh {} fores stis {} epanalipseis\nrook   wins {}% dhladh {} fores stis {} epanalipseis \nisopalia    {}% dhladh {} fores stis {} epanalipseis '.format(f1f,count_1,Repetitions,f2f,count_2,Repetitions,f3f,count_3,Repetitions) 
print(stuff_in_string2)



