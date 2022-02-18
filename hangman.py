from curses.ascii import isalpha
import random
import os
from art import tprint
import colorama
from simple_term_menu import TerminalMenu
from arthangman import HANGMANPICS

#Clear terminal and print hangman in art
def hangman_art(is_clear,lifes):
    if (is_clear == 'clear'):
        os.system('cls||clear')  
    
    tprint("""========
HANGMAN
========""")
    print("💖 " * lifes)
    print(HANGMANPICS[6-lifes])
    print('\n')


#Open a file and choose random word to guess
def get_word():
    f = open('words.txt', 'r')
    list_of_words =  f.read().split('\n')
    f.close
    word = random.choice(list_of_words)
    return word


#Print list of available letters
def print_available_letters(letters):
    print('Guess a letter [' , end ='')
    print(*letters, sep = "/", end = '/')
    print('quit:] ' , end = '')


#Print guessed word with hidden and opened letters
def print_answer(answer):
    for x in range(0,len(answer)):
            print(answer[x], end =' ')
    print("\n") 

#Delete used letter from available list and add it to used list
def move_letter(letters, used_letters, guess, word):
    for x in range(0, len(letters)):
        if guess == letters[x]:
            if guess in word:
                used_letters.append(letters[x])
            letters[x] = '_'

def error_check(guess, answer, letters, lifes):
    while (guess != 'quit') and (len(guess)!= 1 or isalpha(guess) != True):
        hangman_art('clear', lifes)
        print('\033[31m'+'Write ONE LETTER each guess')
        print('\033[39m')
        print_answer(answer)
        print_available_letters(letters)
        guess = input('')
    return guess

def is_quit(guess):
    if guess == 'quit':
        exit()
        


#
def main():
    word = get_word()
    #word = "flight      ------     check-in'bit_m@ney"
    
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']         #list to visualise active letters
    used_letters = []                               #list to save letter that was already used 
    lifes = 6                                       #variable to track tries

    #Hide letters in answer
    answer = []
    for x in word:
        if x.isalpha():
            answer.append('_')
        else:
            answer.append(x) 
    

    while lifes > 0:       
        #Visual print HANGMAN
        hangman_art('clear', lifes)
        
        #Print word with hidden letters
        print_answer(answer)
        
        #Print list of available letters and ask input
        print_available_letters(letters)
        guess = input('')
        move_letter(letters, used_letters, guess, word)

        is_quit(guess)

        #Handle errors
        guess = error_check(guess, answer, letters, lifes)
        move_letter(letters, used_letters, guess, word)
        

        #Open letter in word
        if guess in word:
            for x in range(0,len(word)):
                if guess == word[x]:
                    answer[x] = guess
                                
        #Take one life if letter not in word
        while guess not in word :
            if guess not in used_letters:
                lifes -= 1
                used_letters.append(guess)
                move_letter(letters, used_letters, guess, word)
            
            if lifes == 0:
                break
            
            hangman_art('clear', lifes)
            print('\033[31m'+f'"{guess}" not in word, you have {lifes} tries left')
            print('\033[39m')
            print_answer(answer)
            print_available_letters(letters)
            is_quit(guess)
            guess = input('')
            guess = error_check(guess, answer, letters, lifes)
            move_letter(letters, used_letters, guess, word)
            
            if guess in word:
                for x in range(0,len(word)):
                    if guess == word[x]:
                        answer[x] = guess
        

       
        #End game in case of winning
        if "_" not in answer:
            os.system('cls||clear')
            tprint('''========
 You won!
 ========''')
            print(f'The answer is "{word}"')
            break

    #End game in case of lose 
    if lifes == 0:
        os.system('cls||clear')
        tprint("""========
YOU LOST
========""")
        print(HANGMANPICS[6])
        print(f'''The answer was "{word}"\n''')

#Ask to restart game and do it if 'yes'
def restart():
    while True:
        choose = input('Do you want to restart a game? ').lower()
        if choose not in ('y','n','yes','no'):
            print ('Invalid input ')
            break
        elif choose in ('y', 'yes'):
            main()
        else:
            tprint("""========
GOODBYE
========""")
            break

#Start a game
main()

#Try to restart game
restart()







