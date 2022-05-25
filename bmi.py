import time
import sys

def slow_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

slow_print("How much do you weigh in lbs?")
print(" ")
w = input("")
slow_print("How tall are you in inches?")
print(" ")
h = input("")
ww = int(w)
hh = int(h)
g = hh*hh
f = ww/g
b = f * 703
slow_print("Your BMI is " + str(b) + ".")
if(b < 18.5):
    slow_print("This is considered as underweight.")
elif(b < 24.9):
    slow_print("This is considered as normal weight.")
elif(b < 29.9):
    slow_print("This is considered as overweight.")
elif(b >= 30):
    slow_print("You are obese.")