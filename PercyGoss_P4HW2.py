#Percy Goss
# 01/04/2025 (1st of April, 2025)
# P4HW2
# Descision structure assesment (P3HW2) v2, using a while loop and stacking outputs to sum up the totals for overtime, regular, and gross pay.

name = input('Enter an employee\'s name, or "Done" to terminate: ')
hours = 0
wage = 0


count = 0
ottotal = 0
paytotal = 0
grosstotal = 0

while name.lower() != "done":
    count += 1
    hours = int(input(f"How many hours did {name} work? "))
    wage = float(input(f"What is {name}'s hourly wage? "))
    
    ot = hours - 40
    if ot < 0: ot = 0
    if ot > 0: pay = wage * (hours - ot)
    else: pay = wage * hours
    otbonus = wage * 1.5
    otpay = otbonus * ot
    gross = pay + otpay

    ottotal += otpay
    paytotal += pay
    grosstotal += gross
    
    print(f'{'Employee Name:':<15}  {name}')
    print()
    print(f'{'Hours Worked':<20}{'Hourly Wage':<20}{'Overtime':<15}{'Overtime Pay':<20}{'Regular Hours Pay':<25}{'Gross Pay':<15}')
    print("----------------------------------------------------------------------------------------------------------------")
    print(f'{hours:<20.1f}{wage:<20.1f}{ot:<15.1f}${otpay:<20.2f}${pay:<25.2f}${gross:<15.2f}')
    
    print()
    name = input('Enter an employee\'s name, or "Done" to terminate: ')

print()
print('Total number of employees entered:', count)
print(f'Total paid in regular hours: ${paytotal}')
print(f'Total paid in overtime hours: ${ottotal}')
print(f'Total paid: ${grosstotal}')