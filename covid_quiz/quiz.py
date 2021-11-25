#quiz.py
#written in python3
#by Lydia Csaszar

count = 0
warning = 0
good = 0

#start of program
print()
print('Welcome to your health survery to screen for potential covid-19 infection.')
print('Please answer all questions as "yes" or "no" answers')

#fever symptom
print('Have you have a fever of 99 degrees or greater in the past 24hr?')
temp = input()
while temp != 'no' or temp != 'yes':
    if temp == 'yes':
        count += 1
        warning += 1
        break
    elif temp == 'no':
        good += 1
        break
    else:
        print('please try again answering yes or no')
        print('Have you have a fever of 99 degrees or greater in the past 24hr?')
        temp = input()

#difficulty breathing symptom
print('Have you have any difficulty breathing or shortness of breath?')
breath = input()
while breath != 'no' or breath != 'yes':
    if breath == 'yes':
        count +=1
        warning +=1
        break
    elif breath == 'no':
        good += 1
        break
    else:
        print('please try again answering yes or no')
        print('Have you have any difficulty breathing or shortness of breath?')
        breath = input()

#sore throat symptoms
print('have you had a sore throat or has your throat experence any irritation in the past 24-48hrs?')
sore = input()
while sore != 'no' or sore != 'yes':
    if sore == 'yes':
        warning +=1
        count +=1
        break
    elif sore == 'no':
        good += 1
        break
    else: 
        print('please try again answering yes or no')
        print('Have you had a sore throat or has your throat experenced any irritation in the past 24-48hrs?')
        sore = input() 

#diaherria symptom
print('have you experenced any diaherria in the past 24hr?')
poop = input()
while poop != 'no' or poop != 'yes':
    if poop == 'yes':
        count += 1
        break
    elif poop == 'no':
        good += 1
        break
    else:
        print('please try again answering yes or no')
        print('Have you experenced any diaherria in the past 24hr?')
        poop = input()

#fatigue symptom
print('Have you experenced fatigue or an unusual amount of tiredness?')
sleep = input()
while sleep != 'no' or sleep != 'yes':
    if sleep == 'yes':
        count += 1
        break
    elif sleep == 'no':
        good += 1
        break
    else:
        print('Please try again by answering yes or no')
        print('Have you experenced fatigue or an ususual amount of tiredness?')
        sleep = input()

#nausea symptom
print('Have you vomitted or experenced nausea in the past 24hr?')
puke = input()
while puke != 'no' or puke !='yes':
    if puke == 'yes':
        count += 1
        break
    elif puke == 'no':
        good += 1
        break
    else:
        print('Please try again by answering yes or no')
        print('Have you vomitted or experenced nausea in the past 24hrs?')
        puke = input()

#smell symptom
print('Have you experenced a weekened sence of smell or have you lost your sense of smell in the past 24hr?')
nose = input()
while nose != 'no' or nose != 'yes':
    if nose == 'yes':
        count+=1
        print('Have you had any allergy symptoms in the past 24hr?')
        pollen = input()
        if pollen == 'no':
            warning +=1
        break
    elif nose == 'no':
        good += 1
        break
    else:
        print('Please try again by anwering yes or no')
        print('Have you experenced a weekened sence of smell or have you lost yoru sense of smell in the past 24hrs?')
        nose = input()

#aches symptoms
print('have you experenced any unusual headaches or body aches in the past 24-48hr?')
ache = input()
while ache != 'no' or ache != 'yes':
    if ache == 'yes':
        count += 1
        break
    elif ache == 'no':
        good += 1
        break
    else:
        print('Please try again by answering yes or no')
        print('Have you experenced any unsusal headaches or body aches in the bast 24-48hrs?')
        ache = input()



#output the results of the quiz, with three possible results
print()
print('Thank you for completing the survey')
#posibility one, requires quarantine and monitoring
if count >=3 or warning >0 :
    print('Please stay home and continue to monitor your symptoms. Contact a health care professonal for evalutaion if any of your symptions worsen.')
#posibility two, requires user to keep wearing a mask and monitoring
elif count >= 1:
    print('Your symptoms indication you could have a potential infection of some sort.')
    print('Please wear a mask today when you are unable to keep socially distant and wash your hands regularly.')
    print('Continue monitoring your symptoms and if new symptoms develop or worsen please consider isolating yourself from the general population.')
#posibility three, all clear
else:
    print('You are likely to not have any concerning infection. Have a great day!')

print()

    
