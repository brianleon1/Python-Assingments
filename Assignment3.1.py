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
