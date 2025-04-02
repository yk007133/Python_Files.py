
print("\n")
import random
print('********************** Welcome to this game ****************')
print('\n')
print('                       Snake-Water-Gun GAME                               ')
print('\n') 
print('Press 1 for wants to Gun')
print('Press 2 for wants to Snake')
print('Press 3 for wants to Water')
print('\n')
players_num = [1,2,3] 
players_name = ['Gun','Snake','Water']
i=0
while i<1:
    a=int(input(' Enter which you wants\n'))
    print('\n')
    if a in players_num:
        if a==1:
            print(' You -',"Gun") 
        if a==2:
            print(' You -',"Snake") 
        if a==3:
            print(' You -',"Water") 
        b=random.choice(players_name)
        print(' Computer -',b)
        print('\n')
        if a==1 and b=='Gun':
            print(' Draw')
            print('\n')
        if a==1 and b=='Snake':
            print(' You Won')
            print('\n')
        if a==1 and b=='Water':
            print(' Computer Won')
            print('\n')
        if a==2 and b=='Gun':
            print(' Computer Won')
            print('\n')
        if a==2 and b=='Snake':
            print(' Draw')
            print('\n')
        if a==2 and b=='Water':
            print(' You Won')
            print('\n')
        if a==3 and b=='Gun':
            print(' You Won')
            print('\n')
        if a==3 and b=='Snake':
            print(' Computer Won')
            print('\n')
        if a==3 and b=='Water':
            print(' Draw')
            print('\n')  
    else:
        print(' Please enter a valid option!')

