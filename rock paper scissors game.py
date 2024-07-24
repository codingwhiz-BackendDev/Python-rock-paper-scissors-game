# Rock papaer Scissors game 
# Code written by <----CodingWhiz---->

import random

loop = 1
count = 0
computer_count = 0
draw = 0

print('<==============      WELCOME TO ROCK PAPER SCISSORS GAME      ==============>')
while loop < 12:
    loop += 1 
    option = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(option)
    
    
    inp = input('Input either rock, paper or scissors : ')
    inp = inp.lower() 
    if inp not in option:
        print('Please input either rock or paper or scissors')
        
    if inp == 'scissors' and computer_choice == 'rock':
        print('You lost, computer picked '+ computer_choice +'\n') 
        computer_count += 1
        print('Computer score is ' + str(computer_count))
        
    elif inp == 'scissors' and computer_choice == 'paper' :
        print('You won, computer picked '+ computer_choice+'\n') 
        count += 1
        print('Your score is ' + str(count))
        
    elif inp == 'rock' and computer_choice == 'scissors' :
        print('You won, computer picked '+ computer_choice+'\n') 
        count += 1
        print('Your score is ' + str(count))
        
    elif inp == 'rock' and computer_choice == 'paper' :
        print('You lost, computer picked '+ computer_choice+'\n')
        computer_count += 1
        print('Computer score is ' + str(computer_count))
        
    elif inp == 'paper' and computer_choice == 'rock' :
        print('You won, computer picked '+ computer_choice+'\n') 
        count += 1
        print('Your score is ' + str(count))
        
    elif inp == 'paper' and computer_choice == 'scissors' :
        print('You lost, computer picked '+ computer_choice+'\n')
        computer_count += 1
        print('Computer score is ' + str(computer_count))
        
    elif inp == 'scissors' and computer_choice == 'paper' :
        print('You won, computer picked '+ computer_choice+'\n')  
        count += 1
        print('Your score is ' + str(count))
    elif inp == computer_choice:
        print('You draw, computer picked ' + computer_choice+'\n')
        draw += 1
        
    if loop == 11:
        print('<==============      GAME OVER      ==============>')
        print('Your total score is ' + str(count) + ' while Computer score is ' + str(computer_count)+' and '+ str(draw) +'draws')
        if count > computer_count:
            print('<==============      YOU WON      ==============>')
        elif count == computer_count:
            print('<==============      IT WAS A DRAW      ==============>')
        else:
            print('<==============      YOU LOST      -==============>')
        break
    