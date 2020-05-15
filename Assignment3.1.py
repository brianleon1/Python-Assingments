# Write a program to prompt the user for hours and rate per hour using input to compute gross pay
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)
hrs = input('Enter Hours: ')
rph = input('Enter Rate: ')
h = float(hrs)
r = float(rph)
if h <= 40:
    pay = h * r
    print('Pay: ', pay)
else:
    pay1 = h * r
    pay2 = (h-40) * (0.5 * r)
    total = pay1 + pay2
    print(total)
