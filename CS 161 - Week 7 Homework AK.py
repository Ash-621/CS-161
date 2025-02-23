#1
#Create inputs
num1=input("Enter the starting number: ")
num2=input("Enter the end number: ")
#make ints
int_num1=int(num1)
int_num2=int(num2)
#make function
def is_even(num1,num2):
    '''
    :param num1 user input:
    :param num2 user input:
    :return a list of all even numbers between the two params:
    '''
    result=""
    for i in range(num1, num2+1):
        if i % 2 == 0:
            str_i=str(i)
            result=result+str_i+" "
    return result
print(f'The even numbers between {num1} and {num2} are: {is_even(int_num1,int_num2)}')

#2
#Get input/turn to int
num=int(input("Enter a positive integer: "))
#Function
'''
'''
def factors(num):
    result=""
    for i in range(1, num+1):
        if num%i==0:
            result=result+str(i)+" "
    return result
print(f'The factors of {num} are: {factors(num)}')

#3
#list
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#name
name="smith"
#make function
def name_num(name):
    '''
    :param name a name that is then turned into a number:
    :return the sum of the letter positions:
    '''
    total = 0
    for letter in name.lower():
        total += alphabet.index(letter)
    return total
result=name_num(name)
print(f'The total sum of the letter position in {name} is: {result}')

#4
#Get input
x=int(input("Enter a number: "))
#make function
def square_recursion(num):
    '''
    :param num user input:
    :return all the squares from 1 to the input:
    '''
    if num < 1:
        return
    square_recursion(num - 1)
    print(num * num)
#use function
square_recursion(x)

#5
#make list
unsorted_list = (12, 43, 22, 34, 2, 21, 3, 33, 81)
#Make even and odd lists
even_num_list=[number for number in unsorted_list if number%2==0]
odd_num_list=[number for number in unsorted_list if number%2==1]
#Sort lists
even_num_list.sort(reverse=True)
odd_num_list.sort()
#Concat lists
full_sorted_list=odd_num_list+even_num_list
#print
print(full_sorted_list)

#6
#get number
num=int(input("Enter a number:"))
#turn number into list in reverse
def number_to_list(number):
    return [int(digit) for digit in reversed(str(number))]
num_list=number_to_list(num)
#use list to compare number to number to see if they can swap
for digits in range(len(num_list)):
    if digits==num_list[-1]:
        break
    if num_list[digits]>num_list[digits+1]:
        num_list[digits],num_list[digits+1]=num_list[digits+1],num_list[digits]
        break
#Turn the reversed new list into the proper INT number
r_result = int("".join(map(str, num_list)))
str_result=(str(r_result))
real_str_result=str_result[::-1]
real_final_result=int(real_str_result)
#Print final result
if real_final_result==num:
    print("No higher value found try again")
else:
    print(real_final_result)
