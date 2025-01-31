#1
#create input
name=input('What is your name? ')
#print name
print('Hello '+name)

#2
#create input
age=input('What is your age? ')
#attempt print
#print(age+5) error was due to age variable is not an INT
#convert to INT
age_int=int(age)
#attempt print again
print(age_int+5)

#3
#create inputs
new_age=input('What is your age? ')
years_later=input('How many years? ')
#Convert to INT
years_int=int(years_later)
new_age_int=int(new_age)
#add ages together
future_age=new_age_int+years_int
#Turn relevent numbers into string to concatenate
str_future_age=str(future_age)

#Print result
print('In '+years_later + ' years you will be '+ str_future_age + ' years old.')

#4
#Create inputs
hours=input("Enter the number of hours worked: ")
wage=input("Enter your hourly wage, without the $: ")
#turn into floats
f_hours=float(hours)
f_wage=float(wage)

#5
#Make wages (there are around 52 week in a year)
weekly_wage=f_hours*f_wage
yearly_wage=weekly_wage*52
#turn to string
str_weekly_wage=str(weekly_wage)
str_yearly_wage=str(yearly_wage)
print("Your gross pay this week is $"+str_weekly_wage +
      "\nYour estimated annual gross pay will be $"+str_yearly_wage)

