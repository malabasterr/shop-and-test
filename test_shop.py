# Write unit tests for your Simple Shop Program in Task 3.
# You may need to refactor your function in Task 3 to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
# Write at least 5 unit tests in total covering various and appropriate cases. 
# An expected test will see your custom error being raised.

# Test functions that determine if the user's funds are sufficient to make a purchase.
# Testing if the shop correctly deducts the purchased amount from the user's available funds.
# Testing when the user has exactly the right amount of money to make a purchase.
# Testing when the user has insufficient funds to buy *any* item.
# Negative Tests: Create tests to verify how the shop handles invalid inputs or exceptional cases for item names
# Testing when the user enters non-numeric values for quantities or funds.

starting = 100

balance = starting

while balance < cost_of_sofa

extra = input("how mcuh more do you have?")

balance = balance + extra 

#start with 100
#user inputs 5
# balance = 100 + 5
#105 is still less than the cost of the 