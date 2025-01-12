#1 pet name as f-String
#set pet_type and pet_name(s)
from _datetime import datetime
from calendar import month

pet_type="Bunny"
pet_name1="Boba"
pet_name2="Dumpling"
#print
print(f"I have a pet {pet_type}, her name is {pet_name1}, I also have another {pet_type} and her name is {pet_name2}")

#2
#enter info
name=input("Enter your first name: ")
age=input("Enter your current age: ")
num_age=int(age)
savings=input("Enter your yearly savings: ")
num_save=int(savings)
#print result
print(f"Hello {name}! You are currently {num_age} years old."
      f" In 10 years you will be {num_age+10} years old"
      f"If you save ${num_save} every year in 5 years you will have saved ${num_save*5}"
      f" Your average monthly savings is ${num_save/12}")

#3
#import and set variables
import calendar
from datetime import datetime
today = datetime.now()
month=datetime.now().month
month_name=today.strftime("%b")
year=datetime.now().year

#define seconds_in_month and set num_sec_in_month
def seconds_in_month(year,month):

      days = calendar.monthrange(year,month)[1]
      return days * 24 * 60 * 60

num_sec_in_month = seconds_in_month(year,month)
#print
print(f"The number of seconds in {month_name} is {num_sec_in_month}")


#4
#add input and turn to int
eggs=input("Enter the number of eggs: ")
num_eggs=int(eggs)
#divide int and get left over
dozen_eggs=num_eggs//12
left_over_eggs=num_eggs%12
#print result
print(f"This makes {dozen_eggs} dozen eggs with {left_over_eggs} left over")
