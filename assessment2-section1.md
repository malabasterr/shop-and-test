## Section 1: Theory Questions [31 marks]

### 1.1    What does SDLC stand for?

Software development lifecycle
### 1.2   What exception is thrown when you divide a number by 0?

`ZeroDivisionError`
### 1.3   What is the git command that moves code from the local repository to the remote repository?

`git push`
### 1.4   What does NULL represent in a database?

NULL represents no value/empty value. I.e. there is no value for the specified field
### 1.5   Name 2 responsibilities of the Scrum Master

The Scrum Master is responsible for the scrum framework being followed, and facilitating this. They are also responsible for working with all team members and guide them through the framework, asssisting with coaching, understanding and removing obstacles. They ensure their team understands and follows the principles of the scrum framework.
### 1.6   Name 2 debugging methods, and when you would use them.

One simple method for debugging in Python, is the print and check method. This involves using the `print()` function to show variables in the console, and then checking whether the values are as expected or not. This is a very simple method and therefore is useful to use for a quick check. However, as these statements will likely have to be deleted, they are not ideal.

Another method for debugging is an `assert` statement. This method will test a given condition for whether it is true or false, and if it is False the program will raise an AssertionError. It is also useful as it can be adapted to raise a certain message if the condition is False, making it easier to locate the problem.
### 1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need.

`def can_pay(price, cash_given):`<br>
`   if cash_given >= price:`<br>
`      return True`<br>
`   else:`<br>
`      return False`

This function is assuming that the `price` and `cash_given` are numbers. An example where this function would throw an error is when one or both of the parameters (`cash_given` and `price`) are strings. Strings cannot be compared using logical operators such as `>=`. In this case, you would need exception handling- i.e. to use an `except` statement to cover a `TypeError`. You could then you raise a custom error.
### 1.8    What is git branching? Explain how it is used in Git.

Git branching is a way of making a copy of the main line of development, in order to complete work without changing the main line. This can be incredibly useful as it can allow different team members (or even teams) to work on the same code independtly of one another. Once work has been completed on a branch, this can be merged back into the main branch where the main line of development will then reflect the changes that have been made in the branch.
### 1.9  Design a restaurant ordering system.
**You do not need to write code, but describe a high-level approach:**
**a.	Draw a list of key requirements**
**b.	What are your main considerations and problems?**
**c.	What components or tools would you potentially use?**