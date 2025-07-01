#Object learning in python
#person
class person():
    def __init__(self, name, age):
       self.name = name
       self.age = age
##Account
class account():
    def __init__(self,username,password):
        self.username = username
        self.password = password

##Inputs for the person
name = input("Enter your name: ")
age = int(input("Enter your age: "))
p1 = person(name, age)
print("Your name is",p1.name,"and you are",p1.age, "years old")

#function for app
def run_app():
    username = input("Please insert a username: ")
    userpass = input("Please insert a password: ")
    user1 = account(username,userpass)
    print("Welcome!",user1.username,"to the app!")

#if user is 21+ they can sign up if not they can't
if p1.age >= 21:
    print("You can sign up for app!")
    run_app()
elif p1.age < 21:
    print("You are too young for this app!")

