# ----------------------------------------------
# Name:       Von Castro
# Program:    L3Q1VC.py
# ----------------------------------------------
# Purpose: Write a code that quizzes the user on
#          math and display their results.

print('\nVon Castro | January 17 2017 | L3Q1VC.py\n')
print()

print('***Math Quiz***\n')

print('Please calculate the following: \n')

#Ask user for their answers to the following questions and add a counter
#for each questions correct or incorrect
qone = int(input('1. 5*5 = '))
if(qone == 25):
    print('Correct!\n')
    cone = 1                            #adds 1 to the results count if correct
else:
    print('Incorrect!\n')
    cone = 0                            #adds 0 to the results count if wrong

qtwo = int(input('2. 3*3 = '))
if(qtwo == 9):
    print('Correct!\n')
    ctwo = 1                            #adds 1 to the results count if correct
else:
    print('Incorrect!\n')
    ctwo = 0                            #adds 0 to the results count if wrong
 
qthree = int(input('3. 6*5 = '))   
if(qthree == 30):
    print('Correct!\n')
    cthree = 1                          #adds 1 to the results count if correct
else:
    print('Incorrect!\n')
    cthree = 0                          #adds 0 to the results count if wrong
    
qfour = int(input('4. 8*4 = '))
if(qfour == 32):
    print('Correct!\n')
    cfour = 1                           #adds 1 to the results count if correct
else:
    print('Incorrect!\n')
    cfour = 0                           #adds 0 to the results count if wrong

results = cone+ctwo+cthree+cfour        #Calculcates amount user got correct

#Displays the user's quiz results
if(results < 2):
    print(results, 'answer correct')
    percent = results/4 * 100           #Calculates the results percentage
    print('You have failed, you got', str(percent)+'%', '. Please try again')
elif(results > 2):
    print(results, 'answers correct')
    percent = results/4 * 100           #Calculates the results in percentage
    print('Well done, you got', str(percent)+'%')
