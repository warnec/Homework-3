#Colston Warne
#Program to check whether the inputted year is a leap year


# get a year from the user
print("Please enter a year to check whether it is a leap year")
yearInput = int(input())

#check if the year is divisible by the given numbers in sequential order.  The if statement checking for whether
#the year is divisible by 100 is a special case and will output that the year is not a leap year unless the innermost
#if statment clears as well
if ((yearInput) % 4) == 0:
   if ((yearInput) % 100) == 0:
       if ((yearInput) % 400) == 0:
           print("The entered year is a leap year")
       else:
           print("The entered year is not a leap year")
   else:
       print("The entered year is a leap year")
else:
   print("The entered year is not a leap year")