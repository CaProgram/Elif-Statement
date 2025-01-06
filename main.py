print("LOGIN SYSTEM")
print("++++++++++++")
username = input("Username > ")
password = input("Password > ")
if username == "David" and password == "password":
  print("Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password.")
  print()
  print("Have a great day.")
  print()
  print("Don't forget to wear a hat in the sun!")
elif username == "Suzanne" and password == "password1":
  print("Hello there Suzanne, what a lovely accent you have, you could have charmed your way in here even without a password.")
  print()
  print("The weather is nice today.")
  print()
  print("I hope you have a splended day!")
elif username == "Mark" and password == "password2":
  print("Hello there Mark, todays weather is nice, you could have charmed me in here even without a password.")
  print()
  print("Today is a Monday!")
  print()
  print("I hope you have a great start to your week!")
else:
 print("You should not be logging in!")