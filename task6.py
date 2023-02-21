'''
Ask user to enter his email that should have @gmail.com in the end
If the user enter the email that does not contain @gmail.com then
display a message that you are not providing accurate email


email = input("Enter you google email address ")
c = email.endswith("@gmail.com")

if c == False:
    print("You are not providing accurate email")
else:
    print("Welcome Aboard!")
'''
'''
Ask user name (your good name!)
Hello! (User name) .. Should be titled
I hope you are fine, let me know how I can help you! (Start asking)
If user say yes
Then ask ‘share your problem with us” after user share its problem
then say ‘Thanks for your feedback, we will resolve your problem
If user say anything other than yes take it as No and
Then print,
Okay! Good to see you , stay connected (should be in center)
'''

#name = input("What's your good name? ")

#print("Hello!", name)
#help = input('I hope you are fine, let me know how I can help you! Reply only in yes or no: ')

#if help.upper() == "YES":
 #   input("Share your problem with us ")
  #  print("Thanks for your feedback, we will resolve your problem")
#else:
 #   show = "Okay! Good to see you , stay connected"
  #  disp = show.center(50)
   # print(disp)

#Ask user to enter his URL that should starts with http://www.( user url ) and then convert it into user url.com
'''
url = input("Enter your website's url ")

if url.startswith("http://www."):
    user = url.split("http://www.")
    active_url = user[1]
    print(active_url)

else:
    print("wrong")
'''
#Ask user to set your password that should contains number , alphabets
'''
passw = input("Enter your password ")
if passw == passw.isalnum():
    print("Strong Password")
else:
    print("Use a strong Password")
    
    '''
#Ask user to enter his full name with cast or Father Name After then make a first and last name from this information
'''
name = input("Enter your full name ")
split = name.rsplit(' ')
print("First Name: ", split[0],'\n' "Last Name: ", split[1])
'''