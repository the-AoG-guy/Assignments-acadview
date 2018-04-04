# Question 1

def find_max(a,b,c):
  if a > b:
   if a > c:
    return a
   else :
    return c
  else:
   if b > c:
    return b
   else :
    return c
	
# Question 2

def authencticate(username,password):
  if username == 'Franny123':
    if password == "Blueberry10":
     return True
  else:
    return False  
	
# Question 3

from datetime import datetime

time = datetime.now()
user_input = raw_input("Enter any of these choices (US, India) : ")

def format_time(user_input):
   if user_input == "US":
      print time.strftime("%b %d %Y %H:%M:%S")
   elif user_input == "India":
      print time.strftime("%d %b %Y %H:%M:%S")
   else:
      print("Wrong Input Specified.")
format_time(user_input)

# Question 4

from datetime import *
now = datetime.now()
print "1 week ago was it: ", now - timedelta(weeks=1)
print "1 week from now is it: ", now + timedelta(weeks=1)