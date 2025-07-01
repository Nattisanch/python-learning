#Simple madlibs project I did in javascript now In python 
welcome = int(input("Please type 1 or 2: option 1 (Start Madlibs) option 2(Close app): "))

def running_madlib():
    print("Welcome to my madlibs!")
    verb = input("Insert verb: ")
    adjective = input ("Insert adjective: ")
    noun = input("Insert noun: ")
    name = input("Insert a name: ")

    print('There was a',adjective, noun, 'and we decided to',verb,'we called it', name)
    def roundtwo():
        print("Round two!")
        verb = input("Insert verb: ")
        adjective = input ("Insert adjective: ")
        noun = input("Insert noun: ")
        name = input("Insert a name: ")
        print("We saw a", adjective,noun,"and we decided to", verb,"we named it", name)
    userchoice = int(input("Do you want to try another round? 1 = yes 2 = no: "))
    if userchoice == 1 :
        roundtwo()
    elif userchoice == 2:
        print("Goodbye!")

if welcome == 1:
    running_madlib()
elif welcome == 2:

    print("Goodbye!")
    
