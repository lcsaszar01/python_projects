#quiz.py
#written in python3
#by Lydia Csaszar

print()
print('Welcome to your health survery to screen for potential covid-19 infection.')
print('Please answer all questions as "yes" or "no" answers')
print('Have you have a fever of 99 degrees or greater in the past 24hr?')
count = 0
warning = 0
good = 0

temp = input()
if temp == 'yes':
    count += 1
    warning += 1
elif temp == 'no':
    good += 1
else:
    print('please try again answering yes or no')
    go to 

print('Have you have any difficulty breathing or shortness of breath?')
breath = input()
if breath == 'yes':
    print('Have you been experencing any allery issues or have you been exposed to mold in the past 24hrs?')
    mold = input()
    if mold == 'yes':
        count += 1
    elif mold == 'no': 
        count += 1
        warning += 1 
    else:
        print('please try again answering yes or no')
elif breath == 'no':
    good += 1
else:
    print('please try again answering yes or no')
    continue



print('Have you experences any lost of taste or smell?')
taste = input()
if taste == 'yes':
    count += 1
    warning += 1

print()
print('Thank you for completing the survey')
if count >=3 or warning >0 :
    print('Please stay home and continue to monitor your symptoms. Contact a health care professonal for evalutaion if any of your symptions worsen.')
elif count >= 1:
    print('Your symptoms indication you could have a potential infection of some sort.')
    print('Please wear a mask today when you are unable to keep socially distant and wash your hands regularly.')
    print('Continue monitoring your symptoms and if new symptoms develop or worsen please consider isolating yourself from the general population.')
else:
    print('You are likely to not have any concerning infection. Have a great day!')

print()

    
