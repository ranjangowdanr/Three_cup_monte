my_list=['','0','']

#shuffle _list
from random import shuffle

def  shuffle_list(my_list):
     shuffle(my_list)
     return my_list


#mixed_list=shuffle_list(my_list)
 
 
def player_guess():
     guess=''
     while guess  not in ['1','2','0']:
          guess=input("pick up a number:0 1 and 2 ") 
     return int(guess)
   
     
def check_guess(mixed_list, guess):
    if my_list[guess]=='0':
       print("correct") 
    else:
       print("wrong guess")
       print(mixed_list)
       


guess=player_guess()
mixed_list=shuffle_list(my_list)
check_guess(mixed_list,guess)    
        
