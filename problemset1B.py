# taking in input from user
annual_salary= float(input("Enter your annual salary:  "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:  "))
semi_annual_raise = float(input("Enter the semi-annual raise as a decimal: "))

# we are setting our base amounts that we know
down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
month = 0
# over here we are initializing the salary outside so it doesn't reset everytime
monthly_salary = annual_salary / 12


# while our savings are less than our down payment the loop still runs
while( current_savings < down_payment ):
    current_savings = (current_savings + (current_savings * r / 12)
                       + (monthly_salary * portion_saved))
    # calculating our current savings

    month += 1
    # month counter for checking how many months has passed
    # check current savings --> month plus 1 --> is current savings > than down payment if not then continue
    # adding element of raise every six months
    # check if month/ 6 has a remainder of 0 indicating that it is either 6,12,18th so on so forth
    # when we hit a multiple of six month we can adjust our annual salary to the new  annual salary (with raise)
    if month % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        monthly_salary = annual_salary / 12


print("Number of months:", month )




