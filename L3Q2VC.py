# ----------------------------------------------
# Name:       Von Castro
# Program:    L3Q2VC.py
# ----------------------------------------------
# Purpose: Write a code that calculates how much
#          a driver is fined for speeding.

print('\nVon Castro | January 17 2017 | L3Q2VC.py\n')
print()

print('SPEEDING TICKET CALCULATOR v1.0\n')

# Variable for user's speed
speed = int(input('How fast (in kilometres, km) were you driving?: '))

# Output if user is not speeding
if speed < 51:
    print('You were not speeding! Continue to drive safely')
    



# 
# 50 to 66, ticket is $57
elif speed>50 and speed<66:
    fine = 57             #fine = Price of ticket accumulated
    spdiff = speed - 50   #spdiff = calculates by how much the user is speeding
    print('\nYou were going', spdiff, 'km/h over the 50km/h speed limit!\n'
          'Your fine is: $'+str(fine))



#66 to 85, ticket is $103
elif speed>=66 and speed<=85:
    fine = 103
    spdiff = speed - 50
    print('\nYou were going', spdiff, 'km/h over the 50km/h speed limit!\n'
          'Your fine is: $'+str(fine))
    


#86 to 100, ticket is $174
elif speed>=86 and speed<=100:
    fine = 174
    spdiff = speed - 50
    print('\nYou were going', spdiff, 'km/h over the 50km/h speed limit!\n'
          'Your fine is: $'+str(fine))    



#If the user inputs over 100 as their speed, prompt to ask if it is their
#birthday and if the user answers yes, the ticket price is $500. If the user
#answers no, the fine will be waived. Take into account case sensitivity.
elif speed>100:
    dob = input('Is it your birthday? (Yes or No): ')    
    if dob.lower() == 'no':
        fine = 500
        spdiff = speed - 50
        print('\nYou were going', spdiff, 'km/h over the 50km/h speed limit!\n'
              'Your fine is: $'+str(fine))
    
    
    
    elif speed>100 and dob.lower() == 'yes':
        fine = 500
        spdiff = speed - 50
        print('\nYou were going', spdiff, 'km/h over the 50km/h speed limit!\n'
              'Your fine would have been: $'+str(fine),
              'BUT it\'s your birthday so it\'s on us')
        print('Your fine is $0')

