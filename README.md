# Login System

## Purpose
This is a simple Python-based login system that checks the credentials of users and provides personalized messages based on their username and password. If the credentials match predefined values, the system greets the user with a custom message. If the credentials don't match any of the predefined sets, the system denies access.

## How It Works
The program asks the user for their **username** and **password**, then checks the input against a set of predefined usernames and passwords. If a match is found, the program displays a personalized greeting and message. If the credentials do not match any predefined user, it displays an error message.

### Predefined Users and Passwords:
1. **David** with password `password`
   - Custom greeting: "Why hello there David..."
   - Encouragement: "Don't forget to wear a hat in the sun!"

2. **Suzanne** with password `password1`
   - Custom greeting: "Hello there Suzanne..."
   - Encouragement: "I hope you have a splendid day!"

3. **Mark** with password `password2`
   - Custom greeting: "Hello there Mark..."
   - Encouragement: "I hope you have a great start to your week!"

If any user other than **David**, **Suzanne**, or **Mark** tries to log in, the system denies access with the message, "You should not be logging in!"

## Code Explanation
1. **User Input:**
   - The program prompts the user for their **username** and **password** via the `input()` function.
   
2. **Conditionals:**
   - The system uses `if` statements to check whether the entered username and password match any of the predefined combinations.
   - If a match is found, a personalized message is printed.
   - If no match is found, the program prints a denial message.

3. **Output:**
   - Depending on the user credentials, the program will output one of the following:
     - A greeting and message if the user is recognized.
     - An error message ("You should not be logging in!") if the user is not recognized.

## Example Output

### Successful login with **David**:
```plaintext
LOGIN SYSTEM
++++++++++++
Username > David
Password > password
Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password.

Have a great day.

Don't forget to wear a hat in the sun!

