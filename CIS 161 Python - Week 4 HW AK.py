#1

#create function
def average(x,y,z):
    '''Calculates the average (mean) of three numbers
    Args:
        x,y, and z are just random numbers
    Return:
        function returns the mean of the numbers'''
    return  (x+y+z)/3

#print
print(average(7,5,9))
print(average(6,6,7))


#2 (Explanation is at the bottom)
#print
#print(average2(7,5,9))
#print(average2(6,6,7))

#create function
#def average2(x,y,z):
#    '''Calculates the average (mean) of three numbers
#   Args:
#        x,y, and z are just random numbers
#    Return:
#        function returns the mean of the numbers'''
#    return  (x+y+z)/3

#The issue with reversing the order of calling the function and defining the function is that
#you are trying to call a function that doesn't exist yet


#3(Explanation is at the bottom)
#create function
def average(x,y,z):
    '''Calculates the average (mean) of three numbers
    Args:
        x,y, and z are just random numbers
    Return:
        function returns the mean of the numbers'''
    return  (x+y+z)/3

#print
print(average(7,5,9))
print(average(6,6,7))
#print(x)
#The issue is that x is only defined in the function and does not have a definition in the script itself


#4
#create function
def dog_to_human(dog_age):
    '''Calculates the age a dog is in human years from dog years
    Args:
        dog_age is how old a dog is in dog years
    Return:
        function returns what the dog's age would be in human years'''
    return 24+(dog_age-2)*4
#print
print("5 dog years is equivalent to",dog_to_human(5),"human years")
print("11 dog years is equivalent to",dog_to_human(11),"human years")
print("8 dog years is equivalent to",dog_to_human(8),"human years")

#5
#Create function
'''Calculates the value loss of a car over time
Args:
    years is how many years old the car is
    country is what country the car is from
    value is the inital value of the car
Return:
    function returns the current value of the car'''
def car_loss(years,country,value):
    if country=="German" or country=="german":
        loss=.95
    if country=="Japanese"or country=="japanese":
        loss=.93
    if country=="Italian"or country=="italian":
        loss=.95
    for i in range(years):
        value=value*loss
    value=round(value,2)
    return value
#create inputs
value=input("How much was you car worth when you got it? (Don't add the $ sign) ")
country=input("What kind of car do you have from German, Japanese, or Italian? ")
years=input("How many years have you had this car? ")
#edit inputs for function
float_value=float(value)
int_years=int(years)
#call function
final_value=car_loss(int_years,country,float_value)
#print result
print(f'The value of a {country} car that was worth ${float_value} will be worth ${final_value} after {years} years.')


#6
#function
def dog_to_human(dog_age):
    '''Calculates the age a dog is in human years from dog years
    Args:
        dog_age is how old a dog is in dog years
    Return:
        function returns what the dog's age would be in human years'''
    return 24+(dog_age-2)*4

dog_name=input("What is your dog's name? ")
dog_age=input(f'How old is {dog_name}? ')
int_dog_age=int(dog_age)
dog_to_human_age=dog_to_human(int_dog_age)
print(f'Your {dog_name} is {dog_to_human_age} human years old')

#7
#create function
def ice_cream_price(scoops):
    '''Calculates the price of an ice cream based on the number of scoops
    Args:
        Scoops is the number of scoops that the person wants
    return:
        returns the final price of the ice cream based on the scoops'''
    return scoops*1.15+2.25

#input
scoops=input("How many scoops? ")
int_scoops=int(scoops)
final_price=ice_cream_price(int_scoops)
#print
print(f'A {int_scoops}-scoop cone will cost ${final_price}')
