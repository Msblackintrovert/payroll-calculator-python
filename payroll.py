# Get Employee Pay information and name from user
print('Welcome to your payroll dashboard')
print('Please fill out all fields below to generate paystub')
employee_name = input('Employee name?')
hours_worked = float(input('Hours Worked? '))
hourly_rate = float(input('Hourly Pay Rate? '))
state_rate = float(input('State Tax Rate(convert to decimal)? '))
federal_rate = float(input('Federal Tax Rate(convert to decimal)? '))

# calculate gross pay and display

gross_pay = hours_worked * hourly_rate
print('Gross Pay: ' , gross_pay)
print('Deductions:  ')
state_deductions = gross_pay * state_rate
federal_deductions = gross_pay * federal_rate
print('Federal Taxes Deducted:', federal_deductions)
print('State Taxes Deducted: ' , state_deductions)
total_deductions = federal_deductions + state_deductions
print('Total Deductions: ' , total_deductions)
net_pay = gross_pay - total_deductions
print('Net: ', net_pay)




      
