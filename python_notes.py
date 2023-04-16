#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Get three test scores and assign them to the 
# test1, test2, and test3 variables.

test1 = float(input("Enter the first test score: "))
test2 = float(input("Enter the second test score: "))
test3 = float(input("Enter the third test score: "))

# Calculate the average of the three scores
# and assign the results to the average variable.

average = (test1 + test2 + test3) / 3.0

# Display the message.

print("The average score is", average)


# In[15]:


# Get the desired future value.
future_value = float(input("Enter the desired future value: "))

# Get the annual interest rate.
rate = float (input("Enter the annual interest rate: "))

# Get the number of years that the money will appreciate.
years = int(input("Enter the number of years the money will grow: "))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)** years

# Display the amount needed to deposit.
print("You will need to deposit this amount:", present_value)



# In[12]:


# Get a number of seconds from the users.
total_seconds = float(input("Enter the number of seconds: "))

# Get the number of hours.
hours = total_seconds // 3600

# Get the number of remaining minutes.
minutes = (total_seconds // 60) % 60

# Get the number of remaining seconds.
seconds = total_seconds % 60

# Display the results.
print("Here is the time in hours, minutes, and seconds:")
print("Hours", hours)
print("Minutes", minutes)
print("Seconds", seconds)


#-------------------------------------------------------------------------------------------

# SUMMARY:

# The input number is float for (Enter the number in seconds: ) -> 11730
# We are learning to use % here.
# Why 3600? well 3600 seconds equal an hour -> number of hours
# Why divide // 60? -> total number of minutes -> 11730 // 60 = 195.5 -> 195.5 % 60 = 15.5
    # why 15 and not 15.5? -> float hasn't been specified -> minutes variable truncates and takes int value
# Why total seconds % 60 -> 30.0 -> you have to work backwards -> 60 * 195 = 11700
    # so now 11730 - 11700 = 30.0


# In[27]:


print("One")
print("Two")
print("Three")
print("---------------------")
print("One", "Two", "Three", sep=" ")
print("One", end=" ")
print("Two", end=" ")
print("Three")
print("-----------------")
print("One", end="")
print("Two", end="")
print("Three")

#--------------------------------------------------------------------

# SUMMARY:
# Notice how sep = " " and end = " " and their forms.
    # The best way to look at them is that one is kind of used towards the end
    # and the other is used as more so of after each line.
# So take a look at the first code even though it may seem self explantory there is something that you need
    # to know -> that "each of the statement displays a string and then puts a newline character"
    # You dont see the new line character but when its displayed it causes the output to advance to the next line.
# Something really IMPORTANT that you need to know is -> that the print statement put a space between 
    # the variable and string or method whatever thats important because the end = "" and sep = "" are not soley
    # responsibile for that alone rather they help in that cause as well but not really thier intended purpose.
    # this thinking is more so of counter intitutive.
# The reason why we are using end=" " is becasue we are telling the compiler 'that hey dont end the line yet 
    # keep it going becasue we are adding more to it'
    # and when we say end = "" and dont specify the space then we are telling the compiler that "hey be sure to
    # get rid of that space" 
# So the next thing that we are going to be talking about is the sep = " " and sep = "" -> The thing to know here 
    # that when you dont want that space between the variables you would use "" and the oppsite vice versa.
# The cruical mistake that I had made was that I didnt think that the print statement had a newline built in it.
    # This made me think that end = " " and sep = " " were doing that when thats not really true they can tho.
# The last thing that I wanted you to know is that when it comes to the sep= and end= you are using "" double brace
    # and for the foramt specifier we are using '' thats IMPORTANT so dont get that confused.


# In[3]:


print("what is the root of existence? \"one would say\" ")
print("What is the meaning of life? \'one would say \' ")
print("What gives life meaning to you \\ that is the question")

#_____________________________________________________________________

# SUMMARY:
    # Notice how this code is using the different escape characters. 


# In[5]:



print(format(12345.6789, ".2f"))

#_______________________________________________________________

# SUMMARY:
    # This is format specifier its job is to basically round the given number.
    # To the right place value in this case 2 place values.
    # The f represent data type in this case we are using float.
    # Notice how there is " " around the .2f 
    


# In[6]:


print(format(12345.6789, "e"))

#________________________________________

# SUMMARY:
    # Format specifer for exponents.


# In[7]:


# This program demonstrates how a floating point
# number can be formatted.
amount_due = 5000.0
monthy_payment = amount_due / 12
print("The monthly payment is", format(monthy_payment, ".2f"))


# In[8]:


# This program demonstrates how a floating point
# number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print("Your annual pay is $", format(annual_pay, ",.2f"), sep="")

#_______________________________________________________________

# SUMMARY:
    # Notice how the sep = "" -> its removing space between the $ and the actual number.
    # This is showing how you can use a separator and a formatter together.
    


# In[28]:


print('The number is', format(12345.6789, "12,.2f"))
print('The number is', format(12345.6789, '12.2f'))

#____________________________________________________

# SUMMARY:
    # Take a look at the 12 this is serving as the place holder meaning ->
    # the code will be indented 12 spaces. The thing to know here is that 12 = spaces wide ->
        # , = adding comas to it, .2 = rounding, and the f = float type.
    # These numbers are right justified meaning they allign to the right. 


# In[3]:


# This program displays the following
# floating point numbers in a column
# with their decimal points aligned.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Display each number in a field of 7 spaces
# with 2 decimal places.
print(format(num1, '7.2f'))
print(format(num2, '7,.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))

#______________________________________________________________

# SUMMARY 
    # These numbers are being right justified.
    # Notice how these are being put the equal amount of spaces -> (7)


# In[30]:


print(format(0.5, "%"))
print(format(0.5, '.0%'))

#________________________________________________________

# SUMMARY:
    # The format specifier -> f (type designator) -> can be used as % to format
        # a floating point number as a percentage.
    # This symbol causes the number to be MULTIPLIED by 100 and displayed with %.
    # Notice the .0 -> it is rounding the answer to appropriate place value ->
        # using percentage format specifier you can also ROUND.


# In[20]:


print(format(123456, 'd'))
print(format(123456, ',d'))
print(format(123456, '10d'))
print(format(123456, '10,d'))

#_____________________________________________________

# SUMMARY:
    # This is known as formatting integers. (The code prior were formatting floats)
    # When formatting integers you CANNOT SPECIFY THE PRECISION and ->
        # You use 'd' as type designator.
    # Notice you are working with INTEGERS here -> works similar to formatting floats.


# In[21]:


import turtle

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.done()

#____________________________________________________________

# SUMMARY:
    # turtle.forward(distance)
    # turtle.left(angle) & turtle.right(angle)
    # Angle is on the cartesian plane
    # IMPORTANT TERM -> 45 degree on right angle & 45 degree on left angle
        # why? -> left and right are changing relative to starting coordinate.
        # Therefore -> direction and angle are two different thing ->
            # Think of roads turn right on bellaire -> you are turning into direction
            # from your starting point.


# In[25]:


import turtle

turtle.forward(100)
turtle.left(120)
turtle.forward(150)
turtle.done()
#____________________________________________________________

# SUMMARY:
    
    # If you were to change the turtle.right to turtle.left you will notice (vice versa) ->
        # That the relative starting point is independent -> left and right
        # are always at the state of change. 


# In[27]:


import turtle

turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.done()


# In[ ]:


import turtle

turtle.showturtle()
turtle.heading()
print(turtle.heading())
turtle.setheading(180)
turtle.heading()
print(turtle.heading())

#_____________________________________________________________________

# SUMMARY:
    # turtle.heading -> display the turtle current heading
    # turtle.setheading -> You can manually set a specified heading.


# In[ ]:


import turtle

turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.done()

#____________________________________________________________________

# SUMMARY:

    # turtle.penup -> doesnt write anything
    # turtle.pendown -> writes 


# In[ ]:


import turtle

turtle.circle(100)
turtle.done()
#_____________________________________________________

# SUMMARY:
    # turtle.circle(radius)


# In[ ]:


import turtle

turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
turtle.done()


# In[ ]:


import turtle

turtle.pensize(5)
turtle.circle(100)
turtle.done()
#_________________________________________________________

# SUMMARY:
    # turtle.pensize(radius)


# In[ ]:


import turtle

turtle.pencolor('red')
turtle.circle(100)

#_____________________________________________________

# SUMMARY:
    # turtle.pencolor(color)


# In[ ]:


import turtle

turtle.bgcolor('gray')
turtle.pencolor('red')
turtle.circle(100)

#_______________________________________________

# SUMMARY:
    # turtle.bgcolor() -> stands for background color
    # you can specify the color that you want using string notation
    # 'red' -> red


# In[ ]:


# SUMMARY:
    # turtle.reset() -> command erases all of the drawing that currently appears in the graphics window
        # resets the drawing color to black and resets the turtle to its original position in the center 
        # of the screen
    # turtle.clear -> command simply erases all drawings that currently appear in the graphics window
        # It doesnt change the turtle positions the drawing color or the graphics windows background color.
    # turtle.clearscreen-> command erases all drawings that currently appear in the graphics window resets
        # the drawing color to black resets the graphics window background color to white and resets the turtle
        # to its original position in the center of the graphics window.


# In[ ]:


import turtle

turtle.setup(640,460)
turtle.done()
#_______________________________________________________

# SUMMARY:
    # turtle.setup(width, height)


# In[ ]:


import turtle

turtle.goto(0, 100)
turtle.goto(-100,0)
turtle.goto(0,0)
print(turtle.pos())
print(turtle.xcor())
print(turtle.ycor())
turtle.done()

#_________________________________________________________

# SUMMARY:
    # turtle.goto(X,Y) -> This means that you are working with a cartesian plane.
    # turtle.pos() -> This is used to find the turtle position of where it is.
    # turtle.xcor() -> used to find the x-cord.
    # turtle.ycor() -> used to find the y-cord.


# In[ ]:


import turtle

turtle.speed(0)
turtle.circle(100)

turtle.speed(1)
turtle.circle(150)

turtle.done()
#__________________________________________________________

# SUMMARY:
    # turtle.speed(speed) -> speed ranges from 0 - 10
    # 0 -> animation disabled
    # 1 -> slowest speed
    # 10 -> fastest speed
    # turtle.hideturtle()
    # turtle.showturtle()


# In[ ]:


import turtle

turtle.write('Hello World')
turtle.done()


# In[ ]:


import turtle

turtle.setup(300, 300)
turtle.penup()
turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Top Left')
turtle.goto(70, -120)
turtle.write('Bottom Right')
turtle.done()


# In[ ]:


import turtle

turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.done()

#________________________________________________________________________

# SUMMARY:
    # You need to specify when to begin fill and when to end fill in order
        # for the code to execute. In this case it was prior to drawing the circle
        # and thus afterwards.
    # Notice how turtle.fillcolor('red') is used prior turtle.begin_fill


# In[ ]:


import turtle

turtle.hideturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
turtle.done()
#_______________________________________________________

# SUMMARY:
    # This code helps you better understand the left and right at an angle.
    # The thing to know is you turn LEFT OR RIGHT based on the direction that you are standing.


# In[ ]:


import turtle

turtle.hideturtle()
turtle.begin_fill()
turtle.goto(120,120)
turtle.goto(200, -100)
turtle.end_fill()
turtle.done()

#________________________________________________________________

# SUMMARY:
    # Notice how you specified 2 coordinates however you are getting a triangle instead
    # The code is teaching that even though you didn't specify the (0,0) this is where the
        # program starts from.


# In[ ]:


# This program draws the stars of the Orion constellation
# the names of the stars, and the constellation lines.
import turtle

# Set the window size.
turtle.setup(500, 600)

# Setup the turtle.
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELLSTAR_X = -40
LEFT_BELLSTAR_Y = -20

MIDDLE_BELLSTAR_X = 0
MIDDLE_BELLSTAR_Y = 0

RIGHT_BELLSTAR_X = 40
RIGHT_BELLSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw the stars.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)   # Left Shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Right Shoulder
turtle.dot()
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)   # Left Belt star
turtle.dot()
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)   # Middle belt star
turtle.dot()
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)     # Right belt star
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)       # Left Knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)     # Right knee
turtle.dot()

# Display the star names.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)   # Left Shoulder
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Right Shoulder
turtle.write('Meissa')
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)   # Left Belt star
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)   # Middle belt star
turtle.write('Alnilam')
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)     # Right belt star
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)       # Left Knee
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)     # Right knee
turtle.write('Rigel')


# Draw a line from the left shoulder to left belt star.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.penup()

# Draw a line from the right shoulder to right belt star.
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.penup()

# Draw a line from the left belt star to middle belt star
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)
turtle.penup()

# Draw a line from the middle belt star to right belt star
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.penup()

# Draw a line from the left belt star to left knee
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Draw a line from the right belt star to right knee
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

turtle.done()

#___________________________________________________________________________

# SUMMARY:
    # 3 steps -> plot points -> name points -> connect the points


# In[20]:


# This program determines the sales profit ** WROTE MYSELF **

PROFIT_PERCENTAGE = .23
COST_PER_UNIT = 20

# Monthly sales.
jan_sales = 150
feb_sales = 160
march_sales = 100
april_sales = 130

# Profit percentage for Jan.
sales_percentage_jan = (jan_sales * COST_PER_UNIT) * PROFIT_PERCENTAGE

# Profit percentage for Feb.
sales_percentage_feb = (feb_sales * COST_PER_UNIT) * PROFIT_PERCENTAGE

# Profit percentage for March.
sales_percentage_march = (march_sales * COST_PER_UNIT) * PROFIT_PERCENTAGE

# Profit percentage for April.
sales_percentage_april = (march_sales * COST_PER_UNIT) * PROFIT_PERCENTAGE

# Display the months and their net profits.
print("The net profit for Jan is", sales_percentage_jan)
print("The net profit for Feb is", sales_percentage_feb)
print("The net profit for March is", sales_percentage_march)
print("The net profit for April is", sales_percentage_april)
#_______________________________________________________________________________

# SUMMARY:
    # Different convention when it comes to naming variables.
    # camel case -> numberOfcollegeGrads
    # pascal case -> numberofcollegegrads
    # snake case -> number_of_college_grads


# In[24]:


# Calculate acre of land     ** WROTE MYSELF **

# set how many square feet is equal to 1 acre.
Acre = 4356

squarefeet_user = int(input("Please enter the amount of square feet:"))
user_acre = squarefeet_user / Acre
print('The amount of acre your land is close to:', int(user_acre), 'acres')

#________________________________________________________________

# SUMMARY:
    # Its important to specify the int before the input statement because then the
    # variable will be taken as a string when in reality you are storing an int value.


# In[25]:


""" Car traveling program ** WROTE MYSELF **  """
# MPH
car_speed = 70

# Time
car_one_time = 6
car_two_time = 10
car_three_time = 15

# Distance
distance_car_one = car_one_time * car_speed
distance_car_two = car_two_time * car_speed
distance_car_three = car_three_time * car_speed

# Display
print('The distance traveled by car one is:', distance_car_one, 'miles', sep=' ')
print('The distance traveled by car two is:', distance_car_two, 'miles', sep=' ')
print('The distance traveled by car three is:', distance_car_three, 'miles')

#_________________________________________________________________________________

# SUMMARY:
    # This code helped us understand how to use the separator variable more effectively
    # sep = ' ' ->  REFER TO NOTES FROM ABOVE EXPLAINS THIS MORE CLEAR.
    # end = ' ' ->  REFER TO NOTES FROM ABOVE EXPLAINS THIS MORE CLEAR.
    


# In[18]:


""" Sales Tax Program  ** WROTE MYSELF **   """

STATE_TAX = 0.05
COUNTY_TAX = 0.025

# User input.
amount_of_purchase = float(input("Please enter the amount of money spent:"))

# Get the tax cuts from county and state.
state_tax_cut = amount_of_purchase * STATE_TAX
county_tax_cut = amount_of_purchase * COUNTY_TAX
combine_sales_tax = state_tax_cut + county_tax_cut
# Display.
print("The sales tax for the state is:", format(state_tax_cut, '.2f'), 'dollars', sep=' ')
print('The sales tax for the county is:', format(county_tax_cut, '.2f'), 'dollars', sep=' ')
print('The combining sales tax for state plus county is:', format(combine_sales_tax, '.2f'), end=' ')

#_______________________________________________________________________

# SUMMARY:
    # This code is showing the difference between sep = ' ' and end = ' ' more clear.
    # Notice how we also used the format variable to make the code more readable


# In[ ]:


""" This program calculates the meal price after set taxes ** WROTE MYSELF ** """

# Variables
tip_percentage = 0.018
sales_tax = 0.07

# User input.
meal_price =  float(input("How much did your food cost?"))

# Meal price after tip.
meal_price_after_tip = meal_price * tip_percentage

# Net price.
net_price = (meal_price - meal_price_after_tip) * sales_tax
net_meal_price = meal_price - meal_price_after_tip

# Display.
print('The amount after the 18% tip and 7% sales tax is', format(net_price, '.2f'), sep=' ')
print('The amount pretax after tip % taken for the meal is:', format(net_meal_price, '.2f'), end=' ')


# In[ ]:


""" STOCK transaction problem ** WROTE MYSELF ** """

# Commission
commission_rate = 0.03

# Acme software.
acme_shares = 2000
acme_price_per_share = 40
acme_price_per_share_SOLD = 42.75

# Find the total share price
acme_share_price = acme_shares * acme_price_per_share

# Find the commission share price
commission_taken = acme_share_price * commission_rate

# Display the commission taken.
print('The total commission that is taken for this transaction was:',
      format(commission_taken, '.2f'), sep=' ')

acme_sold_share = acme_shares * acme_price_per_share_SOLD
net_sales_price = acme_sold_share - acme_share_price

print('The net profit of acme stock is', format(net_sales_price, '.2f'), sep=' ')


# In[ ]:


""" Grape Vines ** WROTE MYSELF ** """

# Calculate for R:
R = float(input('What is the length of the row (in feet)?'))

# Calculate the E:
E = float(input('What is the amount of space used in assembly'
                '(in feet)?'))

# Calculate the S:
S = float(input("What is the space between the vines (in feet)?"))

# Formula:
V = R - 2 * E * S

print('The number of grape vines that will fit will be', format(V, '.2f'), end=" ")

#_______________________________________________________________

# SUMMARY:
    # An important note here is that declare variables first -> declare formula.


# In[ ]:


""" This program calculates the percentage of male and female ** WROTE MYSELF ** """

# Ask for the total number of students in class.
number_of_students_in_class = int(input("what is the number of students in class?"))
number_of_males = int(input("What is the number of males in class?"))
number_of_females = int(input("what is the number of females in class?"))

percentage_male = number_of_males / number_of_students_in_class
percentage_female = number_of_females / number_of_students_in_class

print('The percentage of Males is', format(percentage_male, '.0%'), sep=" ")
print('The percentage of Female is', format(percentage_female, '.0%'), end=" ")

#____________________________________________________________________________

# SUMMARY:
    # This code is showing how we are using % in the format specifier.
    


# In[1]:


""" This program is calculating the average test scores using conditional statements """

# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score.

# The HIGH_SCORE named constants holds the value that is
# considered a high score.
HIGH_SCORE = 95

# Get the three test scores.
test1 = int(input("Enter the score for test 1: "))
test2 = int(input("Enter the score for test 2: "))
test3 = int(input("Enter the score for test 3: "))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print("The average score is", average)

# If the average is a highscore,
# congratulate the user.
if average >= HIGH_SCORE:
    print("Congrats!")
    print("That is a great average")
#__________________________________________________________________________________

# SUMMARY:
    # Overall this code is fairly simple to understand however the thing that you need to know
        # that when using conditional statements be sure to incorporate terminators in this case the 
        # : (colons) because this lets the compiler know that the if clause has ended and the rest of 
        # statements within the clause or known as block is part of the if clause.
    # The thing to understand this from c++ is that in c++ you have to user a terminator for everything 
        # but for python the only thing that you are using terminator thus far is the conditional statements
        # or anything that is branching out in a block.


# In[2]:


""" This program calculates OT pay + standard pay """

# Named constants to represent the base hours and
# the overtime multiplier.
BASE_HOURS = 40         # Base hours per week.
OT_MULTIPLIER = 1.5     # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# Calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First get the number of overtime hours worked.
    overtime_hours = hours - BASE_HOURS

    # Calculate the amount of overtime pay
    ovetime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # Calculate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + ovetime_pay

else:
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print("The gross pay is $", format(gross_pay, ",.2f", ), sep="")

#____________________________________________________________

# SUMMARY:
    # So lets begin to examine this code this program very concept is to calculate overtime pay.
    # At first glance it seems really simple however there are some tips and tricks that saves you time.
        # First and foremost is we have to get the base number of hours and the OT multiplier.
        # The next thing that we are going to get is how much the person get paid per hour and how many hours
            # the person has worked.
        # So one mistake that I made when writing this program was that I wrote to many lines of codes
            # So I calculated the standard salary and the salary plus Ot and then declared a new variable
                # that wold hold both of two variables combined. Now this is not really wrong rather there
                # is a more efficient way to write this code down using less lines.
            # For example in the gross_pay variable we are using the BASE_HOURS just using this is saving us three
                # steps.
    # Something that I learned while writing this code was that notice the print statement instead of writing a 
        # a different print statement for each clause you can keep consistency by using the same variable name since
        # they are being used in different clause and for similar function so that way the compiler can print out that 
        # specific variables that are doing two different things but have the same name. 
        # SIDENOTE: I found this to be rather interesting because this is almost like an element in C++ where you write 
            # a line of code and reuse the same variable. Overall that is an important concept to remember when it 
            # comes to consistency. 


# In[ ]:


""" This program calculates OT pay plus standard pay ** WROTE MYSELF ** """

# This is my version of the if and else statement for calculating overtime pay

# Establish the base hours and the multiplier
BASE_HOURS = 40
OT_MULTIPLIER = 1.5

# Gather input from user regarding the number hours worked and pay rate.
pay_rate = float(input("How much did you get paid per hour?"))
number_hours_worked = float(input("How many hours did you work?"))

# use conditional statement to separate overtime and within 40 hours.

if number_hours_worked > BASE_HOURS:

    # Calculate the overtime hours.
    OT_hours = number_hours_worked - BASE_HOURS

    # Calculate the overtime pay.
    OT_pay = OT_hours * pay_rate * OT_MULTIPLIER

    # Calculate the salary.
    # standard_salary = BASE_HOURS * pay_rate     **EXTRA STEP**

    # Add the OT pay + salary.
    # salary_plus_OT = standard_salary + OT_pay   **EXTRA STEP**

    # Gross Pay:
    gross_pay = BASE_HOURS * pay_rate + OT_pay

    # Display the information.
    # print("The salary that you earned for your effort was", format(gross_pay, ',.2f'), sep= " ") **EXTRA STEP**

else:

    # Calculate the salary.
    # standard_salary = BASE_HOURS * pay_rate
    gross_pay = number_hours_worked * pay_rate
    # print("The salary that you earned for your effort was", format(standard_salary, ",.2f"), sep=" ") **EXTRA STEP**

 # Display the gross pay.
print("The gross pay is $", format(gross_pay, ",.2f"), sep="")

#____________________________________________________________

# SUMMARY:
    # So this code compare it the code previous the thing to know is that this is teaching how to avoid the 
        # writing extra steps within the code. Right now it might not seem like a big deal but when you have to write
        # a code that is 1000 lines then you wanna save as much as time on your hand.


# In[ ]:


""" This program is comparing two set of strings """

name1 = "Mark"
name2 = "Mary"

if name1 == name2:
    print("The names are the same")
else:
    print("The names are not the same")
#____________________________________________________

# SUMMARY:
    # Mark and Mary are not the same values becasue of thier ASCII codes. Each letter has a specific value
        # number wise. 


# In[ ]:


""" This program is teaching how you can use conditional statements with strings"""
# This program compares two string
# Get a password from the user.
password = input("Enter the passwod:")

# Determine whether the correct passwords was used.
if password == "Zaidaslam99":
    print("Password is correct")
else:
    print("Sorry incorrect password")
#_________________________________________________________

# SUMMARY:
    # This program is really self explanatory but the thing that you need to know is that 
        # you can use conditional statements to compare values. Which helps you understand how 
        # companies compare data.


# In[ ]:


# This program compares strings with the < operator
# Get two names from the user.
name1 = input("Enter a name (last name first):")
name2 = input("Enter a name (last name first):")

# Display the name in alphabetical order.
print("Here are the names, listed alphabetically",)

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)

#___________________________________________________________________________________________

# SUMMARY:
    # So fun fact I learned something new when writing this code, the first thing that I learned was
        # that you can store entire string values here and the compiler will measure each and every character
        # we already learned how it compares it using the ASCII codes but the mistake that I made was that 
        # I was thinking of only putting one name, in other words only putting one line of string as suppose 
        # of a first and last name. 


# In[ ]:


# This program determines whether a bank customer
# qualifies for a lon.
MIN_SALARY = 30000.0         # The minimum annual salary
MIN_YEARS = 2                # The minimum years on the job

# Get the customers annual salary
salary = float(input("Enter your annual salary: "))

# Get the years on the current job.
years_on_job = int(input("Enter the number of" + "years employed: "))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print("You qualify for the loan.")
    else:
        print("You must have been employed",
            "for at least", MIN_YEARS,
            "years to qualify;.")
else:
    print("You must earn at least $",
          format(MIN_SALARY, ",.2f"),
          "per year to qualify", sep=' ')


#_____________________________________________________________________________________

# Summary:
    # So to recap some notes - > there is are two things you need to know the difference between
        # decision structures vs sequence structures -> decision str. -> is when the compiler is making
        # a comparison or in other words is cross referencing to compare if terms equal to true or not.
        # while sequence structures are when the compiler goes in sequence its really not stopping its
        # compiler process rather it is just going down as if it were to be reading.
    # The reason why this is important is because this shows how you can use conditional statement and the
        # logic behind them in other words the why? now there are different ways you can set up conditional
        # statements one being 1) sequence structure -> decision structure 2) decision structure -> sequence str.
        # 3) decision structure -> decision structure. The code that you are seeing above is decis. -> decis. format
    # The thing to know here is that when working with a d -> d format you are checking conditions within conditions
        # meaning if both conditions evaluates to true.
    # Take a look at the if statement and try to understand how the logic is set up. "if we follow the flow execution
        # we see that the condition salary >= 30000 is tested. if this condition is false there is no need to perform
        # further tests we know the customer does not qualify for the loan" The MOST IMPORTANT thing to understand
        # about this code is how the compiler is testing each if statement and then discarding (referring to else)
        # statement meaning if set condition is true continue and then test next if statement and if that is true then
        # execute the if clause rather and wherever it is false then take that appropriate exit.
    # The best way to think about nested conditional statement is a car driving on the highway think it this way if
        # your exit hasn't shown up then you keep driving the similar logic is here think only slightly opposite yet
        # similar that if the statement is TRUE move to next if block if true then move to the next if block and
        # wherever its false STOP at that respected else statement that matches with its corresponding if block.


# In[ ]:


""" This program is useful for calculating student grade """

# Named Constant for Grades:
A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60

# User input
user_grade = int(input("Please enter the grade that you made: "))

# conditional statements
if user_grade >= A_GRADE:
    print("You made a grade of an A")

elif user_grade >= B_GRADE:
    print("You made a grade of an B")

elif user_grade >= C_GRADE:
    print("You made a grade of an C")

elif user_grade >= D_GRADE:
    print("You made a grade of an D")

else:
    print("You made a grade of F")
#_______________________________________________________________

# Summary:
    # So overall this code I did right the only thing that I had messed up in was not naming 
        # the name constants earlier its always best practice when it comes to naming the constants 
        # before hand because when doing so your keeping a pattern of consistency and it becomes more 
        # easier to read for anyone else who is reading he code.
    # Something else that I noticed was when it comes to elif clause notice the spacing compared to writing 
        # else if and then else if doing so you are starting to indent towards the right side of the screen
        # and by doing elif whats happening is that you are keeping the same consistent spacing which makes it
        # easier to read 


# In[ ]:


# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0        # The minimum annual salary
MIN_YEARS = 2               # The minimum years on the job

# Get the customers annual salary.
salary = float(input("Enter your annual salary: "))

# Get the number of years on the current job.
years_on_job = int(input("Enter the number of" +
                         "years employed"))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print("You qualify for the loan.")
else:
    print("You do not qualify for this loan.")

#___________________________________________________________________________________________

# SUMMARY:
    # So earlier we learned about nested decision structures -> The thing to understand when it comes to 
        # nested decision structures is how they are formatted one if clause within another this is the key step 
        # when it come to structuring another thing to keep in mind is having the if clause respected else clause
    # The thing that makes this code different from the previous code that we had wrote down is take a look at the 
        # and operator just by doing so we are saving the trouble of having to write another if and else clause.
        # Now the thing to remember is that when it comes to if and else clause known as nested decision structures
        # the reason why they are executed is because you need both statements to be true in order for it to execute
        # that is an important point to consider when using conditional statements.
    # Something else that I forgot to mention was regarding the other code this code is basically saying that you
        # don't qualify for the loan but the other code that we wrote regarding the nested decision structure it said
        # more detailed message on why the person didn't qualify. This is something I didn't really catch but then 
        # the thought came to me maybe its best to use nested decision structures when you need a specific message 
        # printed after each clause and you can use the conditional operator for more broad things like for things to
        # match.


# In[ ]:


# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000           # The minimum annual salary.
MIN_YEARS = 2                # The minimum years on the job

# Get the customers annual salary.
salary = float(input("Enter the annual salary: "))

# Get the number of years on the current job.
years_on_job = int(input("Enter the number of" + "years employed "))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print("You qualify for the loan.")
else:
    print("You do not qualify for this loan.")

#__________________________________________________________

# Summary:
    # So this code is test the or operator the thing to know here is the logic behind the or operator.
    # What I really found interesting in this code was not necessarily the programming aspect of the code
        # rather for me it was the logic behind it. For example this code was written so that banks can attract
        # more people therefore they turn down their selection level and get just about anyone. The reason why
        # this logical thinking had struck different was it gave a very practical example that when you are trying 
        # to be selective then you refer to the and statement and when you want your program to be less selective 
        # you then tun to or statement. It kind of taught the why and gave it very visually.


# In[ ]:


""" This program reads three coefficients of a quadratic equation
AX^2 + BX + C and find the roots of the equation """

# Set the display:
print("This program is used to calculate the square root of the" +
      "equation\n" + "Please enter the values for A, B, C:")


# Gather the User input.
A = int(input("What is the value for A? "))
B = int(input("What is the value for B? "))
C = int(input("What is the value for C? "))

# Set up the formula.

root_one = ((-B + 1/2 ** (B ** 2) - (4 * A * C)) / (2 * A))
root_two = ((-B - 1/2 ** (B ** 2 - (4 * A * C))) / (2 * A))

# Display the outputs.
print("The coefficient for A is", A)
print("The coefficient for B is", B)
print("The coefficient for C is", C, "\n")
print("Their respected roots are:", "\n" ,root_one, "\n",
      root_two)

