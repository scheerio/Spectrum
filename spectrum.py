#Created by Ben Scheer
from tkinter import *
import pyperclip
import translater

#STORES ELEMENTS TO SEARCH AND FINAL CORRECT NAME
elementSearch = []
element = 100

#LISTS OF ALL INFO
firstname=translater.firstname
lastname=translater.lastname
email=translater.email
focus=translater.focus
nickname=translater.nickname

#ASKS WHO YOU WANT TO SEARCH
answer=input('Who are you emailing? Type their first name here: ')
print('\n---------------------------------------\n')

#SEARCHES FOR ALL HITS
count = 0
for x in firstname:
	if (answer==x):
		elementSearch.append(count)
	if (answer==nickname[count] and answer!=x):
		elementSearch.append(count)
	count=count+1

#HANDLES NO MATCH
if (len(elementSearch) == 0):
	print('\n---------------------------------------\n')
	print('That is not a known name. Quit and try again.')
	print('\n---------------------------------------\n')

#HANDLES IF THERE IS MORE THAN ONE MATCH
if (len(elementSearch) > 1):
	print('\n---------------------------------------\n')
	print('There are a few folks with that name:\n')
	for i in elementSearch:
		if (nickname[i]!="n/a"):
			print(' -' + firstname[i] + ' (' + nickname[i] + ') ' + lastname[i])
		else:
			print(' -' + answer + ' ' + lastname[i])
	choose=input('\nType in the last name of the person you are referring to: ')
	count1 = 0
	for y in lastname:
		if (y==choose and (answer==firstname[count1] or answer==nickname[count1])):
			element=count1
		count1=count1+1
	print('\n---------------------------------------\n')

#HANDLES JUST ONE MATCH
else:
	count2=0
	for a in firstname:
		if (answer==a or answer==nickname[count2]):
			element=count2
		count2=count2+1

#CREATES NICKNAME TEXT IF APPLICABLE
nickText=" "
nickTrue=False
exists=False
if (len(elementSearch) != 0):
	exists=True
	if (nickname[element]!="n/a"):
		nickText=" ("+nickname[element]+") "
		nickTrue=True

#FINAL TEXT COMBINED AND COPIED TO CLIPBOARD
if (nickTrue):
	text1 = "Their full name is: " + firstname[element] + " " + lastname[element] + "\nHere is the email address to send to: " + email[element] + "\nTheir focus area is: " + focus[element] + "\n\nHi " + nickname[element] + ",\nI hope that all is well!\n\nBest,\nScheerio"

elif (exists):
	text1 = "Their full name is: " + firstname[element] + nickText + lastname[element] + "\nHere is the email address to send to: " + email[element] + "\nTheir focus area is: " + focus[element] + "\n\nHi " + firstname[element] + ",\nI hope that all is well!\n\nBest,\nScheerio"

if (exists):
	print('The following was copied to your clipboard for your convenience:\n')
	print(text1)
	pyperclip.copy(text1)
	print('\n---------------------------------------')






