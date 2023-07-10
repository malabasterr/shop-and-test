## Section 1: Theory Questions [31 marks]

### 1.1    What does SDLC stand for?

Software Development Lifecycle
### 1.2   What exception is thrown when you divide a number by 0?

`ZeroDivisionError`
### 1.3   What is the git command that moves code from the local repository to the remote repository?

`git push`
### 1.4   What does NULL represent in a database?

NULL represents no value/empty value. I.e. there is no value for the specified field
### 1.5   Name 2 responsibilities of the Scrum Master

The Scrum Master is responsible for the scrum framework being followed, and facilitating this. They are also responsible for working with all team members to guide them through the framework, asssisting with coaching, understanding and removing obstacles. They ensure their team understands and follows the principles of the scrum framework.
### 1.6   Name 2 debugging methods, and when you would use them.

One simple method for debugging in Python, is the "print and check" method. This involves using the `print()` function to show the values of variables in the console, and then checking whether the values are as expected or not. By inspecting these printed values in the console, you can verify if they match expectations or also to identify any unexpected behavior. This method is particularly useful for quickly checking the state of variables and identifying potential issues. It can also be helpful within functions, as you can place print statements at different key intervals to see if the flow of the program is following the expected path. However these print statements are not ideal as they are not intended to be permanent additions and will likely have to be deleted.

Another method for debugging is an `assert` statement. This method will test a given condition for whether it is True or False, and if it is False the program will raise an `AssertionError`. It is also useful as it can be adapted to raise a custom message if the condition is False, making it easier to identify where the problem lies within the code. The assert statement is particularly useful when you want to validate the correctness of a particular section of code.
### 1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need.

`def can_pay(price, cash_given):`<br>
`   if cash_given >= price:`<br>
`      return True`<br>
`   else:`<br>
`      return False`

This function is assuming that the `price` and `cash_given` are numbers. An example where this function would throw an error is when one or both of the parameters (`cash_given` and `price`) are strings. Strings cannot be compared using logical operators such as `>=` and therefore the function would result in a `TypeError`. In this case, you would need exception handling- i.e. to use an `except` statement to catch the `TypeError` and handle it. You could then you raise an error, with or without a custom message.
### 1.8    What is git branching? Explain how it is used in Git.

Git branching is a way of making a copy of the main line of development, in order to complete work without changing the main line. It allows for parallel development, where different team members or teams can work on independent features or bug fixes without disrupting the main line of development. As well as isolating work, branches can be useful for experimentation as it won't alter the main line. Once work has been completed on a branch, this can be merged back into the main branch where the main line of development will then reflect the changes that have been made in the branch.
### 1.9  Design a restaurant ordering system.
**You do not need to write code, but describe a high-level approach:**
**a.	Draw a list of key requirements**
**b.	What are your main considerations and problems?**
**c.	What components or tools would you potentially use?**

If I were to design a restaurant ordering system, these are the key requirements I would want to include:<br>
- A secure payment system
- A way to select between eat-in, collection and delivery
- A way to apply discount codes or special deals for specific combinations of items
- A way of having time-specific deals, e.g. a lower price during lunchtime hours
- A user-friendly interface, clearly showing categories, images, titles, prices and descriptions
- Multiple options for the same item- e.g. different sauces, sides or sizes
- A simple basket feature showing which items have been selected and the total cost
- Compatibility with different size screens such as computers, mobile phones and tablets
- A tracking system that shows how far off the delivery is to the customer
- An account system where people can log in, see their previous orders, save their home address etc.
- A inventory database which would keep track of the items in stock
- A way of searching for certain allergens in food
- An accessible interface that supports different devices such as screen-readers
- A feature that suggests extra items the customer may wish to order
- A function that allows a customer to make simple alterations to their order- e.g. removing certain ingredients
- The option for a customer to add a tip at the payment stage

Main considerations and problems are:
- How to ensure the restaurant is receiving instant notification of new orders
- How can the restaurant interact with the program so the user is notified when their order is in progress or out for delivery
- How to ensure the payments are going through a secure portal
- How to ensure multiple different payment methods are accepted
- How to ensure that the inventory database is updated every time an order goes through and an item is used
- How to ensure the program works on all different browsers
- How to ensure the program can handle multiple orders at once
- How to ensure the program is accessible for people with different devices- e.g. screen readers
- How to ensure relevant discounts are automatically applied at checkout
- How to ensure the interface is user friendly on all sizes of screens
- How to save user's information so it can be accessed through their account
- How to store usernames and passwords for customer's accounts
- A way of tracking key metrics such as number of orders
- How to allow a customer to make simple alterations to their order- e.g. removing certain ingredients
- An option to refund an order if neccessary

Components or tools I would potentially use include:
- A front-end system such as HTML/CSS/JavaScript to make the program user-friendly and interactive
- A relational database that is able to store the restaurant's menu (including items, prices & allergens) and inventory (items, stock, delivery dates)
- Integration with a Kitchen Display System (KDS) so the kitchen staff can see the orders when they need to prepare them
- A back-end system that could handle the placing of the order and the real-time tracking updates given to customers
- Integration with different payment gateways such as PayPal, Apple Pay to handle secure online payments
- Reporting tools that track sales, top selling items, and other metrics