
n=1
while n==1:

    n=1
    print('Which game do you want to play')
    print('Game 1 is with normal probabilites')
    print('Game 2 is with first player always 10 first hand and second always less than 10 first hand')
    print('For exit press 0')
    choice = int(input ())
        
    if choice==1:
            import ergasia4_a
    elif choice==2:
            import ergasia4_b
    elif choice==0:
        n=0
    else:
        print('*****************')    
        print('Wrong Input!')
        print('*****************')
            