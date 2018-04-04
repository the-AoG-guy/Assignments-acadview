# Question 1

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# Question 2

len('Ice-Cream') > 0
len('Ice-Cream') < 10
3 == 3
-5 < -1

# Question 3

total = input("Enter Total:")
country = "US"

if country == "US":
  if total <= 50:
    print "Shipping Cost is  $50"
  elif total <= 100:
    print "Shipping Cost is $25"
  elif total <= 150:
    print "Shipping Costs $5"

# Question 4

name = 'Floyd Mayweather'
is_undefeated = 'Yes'

if name == 'Floyd Mayweather'  and  is_undefeated=='Yes':
  print("Floyd is Undefeated yet!")
else:
  print("I don't believe Floyd lost!")
  
# Question 5

n = input("Enter the value of 'n': ")

if n%3 == 0 and n%5 == 0:
  print ('FizzBuzz')
elif n%3 == 0:
  print ('Fizz')
elif n%5 == 0:
  print ('Buzz')
else:
  print n