import random
#I was asked to make a magic 8 ball in python
#asking for users name
name = input("Enter your name: ")

#asking user to insert a yes or no question
question = input("Enter a yes or no question: ")

#keeping the answer as an empty string
answer = ""

#Generating a random number
random_number = random.randint(1,9)


#Control Flow
#Task 6
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
#Task 8
else:
  answer = "Error"

print(name, "asks:", question)
print("Magic 8-ball's answer: ", answer)

