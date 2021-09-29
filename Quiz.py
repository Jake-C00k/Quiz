from random import randint
from Title_Screen import display


yes = ["y", "yes", "yep", "affirmative", "yea"]
no = ["n", "no", "nope", "negative", "nah"]
finish = False
score = 0
#Special codes
#purple
p = '\033[95m'
#cyan
c = '\033[96m'
#darkcyan
dc = '\033[36m'
#blue
b = '\033[94m'
#green
g = '\033[92m'
#yellow
y = '\033[93m'
#red
r = '\033[91m'
#bold
bf = '\033[1m'
#underline
uf = '\033[4m'
#end
ef = '\033[0m'

confetti = b + "🎉" + r + "--"
logo = p + "QUIZ FIESTA" + b


def question_gen():
    q = randint(1, 3)
    if q == 1:
        question_gen.question = ["Which number is highest?\n", "1: fifty-three\n", "2: four", "3: twelve\n", 1]
    elif q == 2:
        question_gen.question = [" In 1768, Captain James Cook set out to explore which ocean?\n", "1: Pacific Ocean\n", "2: Atlantic Ocean",
      "3: Arctic Ocean\n", 1]
    elif q == 3:
        question_gen.question = ["What is actually electricity?\n", "1: A flow of Air\n", "2: A flow of water", "3: A flow of electrons\n", 3]
    else:
        print("")
    return q

def multi_question(list):
    while True:
        try:
            print(list[0] + list[1] + list[2])
            answer = int(input(list[3]))
            if 1 <= answer <= 3 :
                if answer == list[4]:
                    print("Correct, {} was the right answer".format(answer))
                    multi_question.correct = True
                    break
                else:
                    print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(answer))
                    multi_question.correct = False
                    break

            else:
                print("I’m sorry, but I don’t think there was an option number {}".format(answer))
        except ValueError:
            print("I’m sorry, I didn’t recognize that input. Could you try again, remembering to only use numbers?")

def yes_no(question):
    #Resets answer from any previous yes/no response to prevent error
    answer = None
    #Checks if users response is in the yes and no lists
    answer = input(question).strip().lower()
    if answer in yes:
        #Stores the variable as True, so a flexible response can be used outside the function
        yes_no.answer = True
    elif answer in no:
        #Stores the variable as False, so a flexible response can be used outside the function
        yes_no.answer = False
    else:
        #Error message
        print("Please enter Yes or No\n")
        yes_no(question)

def instructions():
    #Displaying instructions for the user
   input("The program will give you a variety of different questions, most of these multi-choice questions, "
          "but some will be short answer questions.")
   input("If the question is multi-choice, please type the corresponding number to the answer you wish to give.")
   input("If the question is a short answer, please follow the on-screen instructions.")
   input("If you get 1 question wrong, you will lose the quiz.")
   print("However, if you get all the way to the end, you win!\n")



#Main Sequence

#Title Screen
display()
print("-{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}".format(confetti))
input("       PRESS ENTER TO BEGIN            \n")

#Asking the user if they have played before and giving instructions if they haven't
yes_no(b + "Have you played {} before?\n".format(logo))
while not yes_no.answer:
    instructions()
    yes_no("Did you catch all that?\n")
print("Then let the {} begin!\n".format(logo))

#Playing the first four rounds
while not finish:
    for i in range(4):
        question_gen()
        multi_question(question_gen.question, )
        if multi_question.correct:
            finish = False
            score += 1
        elif not multi_question.correct:
            finish = True

