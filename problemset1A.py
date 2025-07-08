# taking in input from user
annual_salary= float(input("Enter your annual salary:  "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:  "))

# we are setting our base amounts that we know
down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

monthly_salary = annual_salary / 12
month = 0

# while our current savings are less than the amount needed for our down payment add a month to our counter
# where our current savings are equal to the previous current savings + our monthly investment income
# + the monthly salary's current savings
# our loop breaks when current savings are greater than or equal to the amount needed for our down payment

while (current_savings < down_payment):
    current_savings = current_savings + (current_savings * r / 12)+ (monthly_salary * portion_saved)
    month += 1

print("Number of months:", month )



