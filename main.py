#Practicing my Python knowledge.

user = {}
#For now it is in terminal. DO I WANT TO MAKE IT INTO A GUI??
def login():
#LOGIN
    userName = input("""
    Please input your username: """) #This will grab the username from the user dict

    userPass = input("Please Insert your password: ") 

    if userPass == "Test": #This will grab the users password from the user dict

        print("Welcome ", userName)
    else: 
        print("Inccorect password.")


#Create account
def createAccount():
    user_email = input("Please inser an email: ")
    user_name = input("Please insert a username: ")
    user_password = input("Please insert a password: ")
    

    #Save it to the user dictionary
    #make sure there isnt an account already made

    print("You have created an account!")


print("""--------------------------
Welcome to the tasks planners!
------------------------------------""")
userselect = input("""Press 1 to sign in.
Press 2 to Create Account.
""")

if  userselect == "1":
    login()
else:
    if userselect == "2":
        createAccount()