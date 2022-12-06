"""
German language study tool v2
Student: Blake Allen
File:    Allen_study_german_v2.py
Course:  CIS 156, CGCC
"""

import random

# Dictionaries
german_dict = {
    'hello' : 'hallo',
    'bye' : 'tschuss',
    'please' : 'bitte',
    'thanks' : 'danke',
    'goodbye' : 'auf wiedersehen',
    'who' : 'wer',
    'what' : 'was',
    'where' : 'wo',
    'why' : 'warum'
    }
german_dict_days = {
    'monday' : 'montag',
    'tuesday' : 'dienstag',
    'wednesday' : 'mittwoch',
    'thursday' : 'donnerstag',
    'friday' : 'freitag',
    'saturday' : 'samstag',
    'sunday' : 'sonntag'
    }
german_dict_phrases = {
    'How are you?' : 'wie gehts',
    'I come from...' : 'ich komme aus',
    'What is your profession?' : 'was ist dein beruf',
    'What is your mother tongue?' : 'was ist deine muttersprache',
    'Which languages do you speak?' : 'welche sprachen sprichst du'
    }
    
    

# Classes and Functions



def main():
    print("This is a simple program to help you study common words and phrases in the German language.\nNote: This program only accepts umlauts(ä, ö, ü) as (a, o, u).\nNote: Please enter your responses in lowercase with no punctuation.\n")





# call main
if __name__ == '__main__':
    main()
    num_correct = 0
    num_incorrect = 0
    user_input = ''
    # First dictionary
    keys_group_1 = list(german_dict.keys())
    random.shuffle(keys_group_1)
    # Second dictionary
    keys_group_2 = list(german_dict_days.keys())
    random.shuffle(keys_group_2)
    # Third dictionary
    keys_group_3 = list(german_dict_phrases.keys())
    random.shuffle(keys_group_3)
    
    
    game_select = int(input('Press 1 to study common everyday German words\nPress 2 to study the days of the week\nPress 3 to study common phrases and questions\n'))
    
    if game_select == 1:
        for i in keys_group_1:
            print(f'To quit: Enter character \"/\" at any time to exit.\nHow do you say \"{i}\" in German?\n')
            user_input = input()
            if user_input == german_dict[i]:
                print('\nCorrect!')
                num_correct += 1
            elif user_input == '/':
                break
            else:
                print('\nIncorrect!')
                print(f'The correct answer was \"{german_dict[i]}\"\n')
                num_incorrect += 1
        total_asked = num_correct + num_incorrect
        try:
            score = float(num_correct / float(total_asked) * 100)   
            print(f'Your score: {score:.2f}%\n{num_correct} correct out of {total_asked} total questions.\nGoodbye')
        except ZeroDivisionError:
            print('Goodbye')
            
    if game_select == 2:
        for i in keys_group_2:
            print(f'To quit: Enter character \"/\" at any time to exit.\nHow do you say \"{i}\" in German?\n')
            user_input = input()
            if user_input == german_dict_days[i]:
                print('\nCorrect!')
                num_correct += 1
            elif user_input == '/':
                break
            else:
                print('\nIncorrect!')
                print(f'The correct answer was \"{german_dict_days[i]}\"\n')
                num_incorrect += 1
        total_asked = num_correct + num_incorrect
        try:
            score = float(num_correct / float(total_asked) * 100)   
            print(f'Your score: {score:.2f}%\n{num_correct} correct out of {total_asked} total questions.\nGoodbye')
        except ZeroDivisionError:
            print('Goodbye')
            
    if game_select == 3:
        for i in keys_group_3:
            print(f'To quit: Enter character \"/\" at any time to exit.\nHow do you say \"{i}\" in German?\n')
            user_input = input()
            if user_input == german_dict_phrases[i]:
                print('\nCorrect!')
                num_correct += 1
            elif user_input == '/':
                break
            else:
                print('\nIncorrect!')
                print(f'The correct answer was \"{german_dict_phrases[i]}\"\n')
                num_incorrect += 1
        total_asked = num_correct + num_incorrect
        try:
            score = float(num_correct / float(total_asked) * 100)   
            print(f'Your score: {score:.2f}%\n{num_correct} correct out of {total_asked} total questions.\nGoodbye')
        except ZeroDivisionError:
            print('Goodbye')
            
