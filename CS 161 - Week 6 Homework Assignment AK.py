#1
#Get input
input_x=input("Enter an integer: ")
#Turn input to int
x=int(input_x)
#Make loop/print
while (x > 0):
    print(x)
    x=x-1
#Print after loop
print ('blastoff!!')

#2
#Get input
input_x=input("Enter an integer: ")
#Turn input to int
x=int(input_x)
#Make loop/print
while (x > 0):
    #check for is even
    is_even=x%2==0
    #add if statement
    if is_even:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
    x=x-1
#Print after loop
print ('blastoff!!')

#3
#Get inputs
input_x=input("Enter an integer: ")
input_y=input("Enter decrease: ")
#Turn input to int
x=int(input_x)
y=int(input_y)
#Make loop/print
while (x > 0):
    #check for is even
    is_even=x%2==0
    #add if statement
    if is_even:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
    x=x-y
#Print after loop
print ('blastoff!!')

#4
#get input
word=input("Enter a word: ")
#get length of input
len_word=len(word)
#loop
while(len_word>=5):
    print(f'{word} has {len_word} letters in it')
    word = input("Enter a word: ")
    len_word = len(word)
#post loop
print("Goodbye")

#4.2
#get count
count=0
#get input
word=input("Enter a word: ")
#get length of input
len_word=len(word)
#loop
while(len_word>=5) and count<=4:
    print(f'{word} has {len_word} letters in it')
    word = input("Enter a word: ")
    len_word = len(word)
    count=count+1
#post loop
if len_word<5:
    print("Goodbye")
elif count>=5:
    print("loser")

#5
#create num
num=10
#while loop
while num<=100:
    binary=bin(num)
    hexadecimal=hex(num)
    print(f'{num} {binary} {hexadecimal}')
    num=num+1

#6
#Create input
star=input("How many starting stars? ")
star_int=int(star)
#First function
def starprint(stars):
    '''
    :param stars is the number of stars wanted:
    :return string with the correct number of stars:
    '''
    count=0
    string=""
    while count<stars:
        string=string+"*"
        count=count+1
    return string
def decrease(stars):
    '''
    :param stars is the number of stars wanted:
    :return a decrease in stars from the inputed number to 1:
    '''
    original_number = stars
    d_count=0
    while d_count<original_number:
        print(starprint(stars))
        stars=stars-1
        d_count=d_count+1

decrease(star_int)