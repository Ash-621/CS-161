#1
#Create input
input_num=input("Enter any INT: ")
#make INT
int_input_num=int(input_num)
#If statement/print
if int_input_num%5==0:
    print(f'{input_num} is divisible by 5')
else:
    print(f'{input_num} is not divisible by 5')

#2
#Input
State=input("Enter the name of a state: ")
#Else ifs
if (State == 'Wisconsin'):
	print ('Madison')
elif (State == 'Colorado'):
	print('Denver')
elif (State == 'Oregon'):
	print('Salem')
elif (State == 'Washington'):
	print('Olympia')
elif (State == 'Idaho'):
	print('Boise')
elif (State == 'Texas'):
	print('Austin')
else:
    print("I don't know that one sorry")

#3
#input
State=input("Enter the name of a state: ")
#Dictionary
state = {
	"Oregon": "Salem",
	"Washington": "Olympia",
	"Idaho": "Boise",
	"Wisconsin": "Madison",
	"Colorado": "Denver",
	"Texas": "Austin"
}
capital = (state.get(State, "Not found"))
print(capital)

#4
#print prices
print("Prices are as follows:"
	  "Under 2 years old: Free, Age 2-11: $3, Age 11-60: $6 Over 60: $4")
#input
age=input("How old are you? ")
#make int
int_age=int(age)
def pool_admission(age):
	'''
	Arg age Is the age that the visitor is:
	Return the price that they get depending on their age:
	'''
	if (age < 2):
		return 0
	elif (age < 12):
		return 3
	elif (age<61):
		return 6
	elif (age>60):
		return 4
#print
print(f'At your age of {age} your price will be ${pool_admission(int_age)}')

#5
#Import
import requests
#request site
x=requests.get('http://coccbobcat.com')
#Turn to text
x_text=x.text
#Count 160s in text
x_count=x_text.count('160')
#Print result
print(f'In this site there are {x_count} instances of the number 160 in this site')


#6
#Import
import psutil
#get number of running processes
x=len(psutil.pids())
#print
print(f'You currently have {x} number of processes ')