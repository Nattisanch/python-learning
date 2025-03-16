#Practicing my Python knowledge by creating a task planner app.
#TODO.
#INPUT A TEXT WELCOMING USER.. (DONE)
#Input task name entry(DONE)
#input add
#input delete
#input mark as done
#input retrieve
#input view of tasks


#What imports???
#For now it is in terminal. DO I WANT TO MAKE IT INTO A GUI?? (WAIT!!)
def login():
#LOGIN
    userName = input("""
    Please input your username: """)

    userPass = input("Please Insert your password: ")

    if userPass == "Test":
        #THIS WILL NOT STAY HERE IT WILL GRAB THE USER'S PASSWORD FROM A FILE OR SOMEWHERE!!

        print("Welcome ", userName)
        #will set to continue to app () later on
    else: 
        print("Inccorect password.")


#Create account
def createAccount():
    #TODO ADD MY LOGIC FOR CREATING ACCOUNT
    #MAKE IT SAVE THE ACCOUNT INFORMATION.
    #I HAVE TO RESEARCH HOW.
    #TODO Create a DB to store Username and password??? do I really need to?
    pass


print("""--------------------------
Welcome to the tasks planners!
------------------------------------""")
input("""Press 1 to sign in.
Press 2 to Create Account.
""")

if "1":
    login()
else:
    if "2":
        createAccount()