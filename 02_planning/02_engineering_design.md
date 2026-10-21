# Engineering Design

**Team members:** Robert Coats - Benjamin Endo

Plan how your code will meet the product requirements. Keep answers brief.

gather inputs from the user
input that data into a function that lets us determine the state of the conditional in a nested if loop
print output from the nested if loop to the console

## Inputs

*List each input and its Python data type. Note the input assumptions.*
String GB used
String Cost of plan

## Processing and decisions
*What calculations and conversions are needed? How will you organize the decisions, including the nested decision?*

convert both strings to doubles

function():
    if the GB used > 10, return true

    else, return false

if true, needs overage processing

if(): function() = true
    if GB used > 10 AND < 15:
        print(over the limit moderate)
    if GB used >15:
        print(over the limit high)





## Output

*What will the program display for each usage category?*
if usage under 10 gb
print("You are within the data limit")
print("Your total bill is: " + Cost of plan )

if usage above 10 gb but less than 15 gb
print("You are above your data limit")
print("Moderate extra usage")
print("Your total bill is: " + Cost of plan )

if usage above 15 gb
print("You are above your data limit")
print("High extra usage")
print("Your total bill is: " + Cost of plan )
 
 
## Function design

*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*

