# The random number generator
from random import randint
# The title screen
from Title_Screen import display
# Special color codes and text changing effects.
from col_codes import p, c, dc, b, g, y, r, confetti, logo, star

# Other variables
yes = ["y", "yes", "yep", "affirmative", "yea"]
no = ["n", "no", "nope", "negative", "nah"]
questions = [b + "\nWhich number is highest?\n" + r + " 1: fifty-three\n 2: four\n 3: twelve\n",
             b + "\nIn 1768, Captain James Cook set out to explore which ocean?\n" + g + " 1: Pacific Ocean\n 2: Atlantic Ocean\n 3: Arctic Ocean\n",
             b + "\nWhat is actually electricity?\n" + y + " 1: A flow of Air\n 2: A flow of water\n 3: A flow of electrons\n",
             b + "\nWhat is the capital of Iceland?\n" + c + " 1: Seydisfjordur\n 2: Reykjavík \n 3: Akureyri\n",
             b + "\nHow many breeds of elephant are there?\n" + dc + " 1: 7\n 2: 5\n 3: 3\n",
             b + "\nHow many permanent teeth does a dog have?\n" + p + " 1: 14\n 2: 42\n 3: 24\n",
             b + "\nWhat language is spoken in Brazil?\n" + r + " 1: Brazilian\n 2: Portuguese\n 3: Spanish\n",
             b + "\nGlossectomy is the removal of all of or part of which body part?\n" + y + " 1: Tongue\n 2: Liver\n 3: Kidney\n"
             ]
answers = [1, 1, 3, 2, 3, 2, 2, 1]
used = []
finish = False
score = 0
color = "brown"
l1 = ["red", "green"]
l2 = ["blue", "orange"]
l3 = ["yellow", "purple"]
l4 = ["brown", "pink"]
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]


# This function asks the user yes-no questions
def yes_no(question):
    # Resets answer from any previous yes/no response to prevent error
    answer = None
    # Checks if users response is in the yes and no lists
    answer = input(question).strip().lower()
    if answer in yes:
        # Stores the variable as True, so a flexible response can be used outside the function
        yes_no.answer = True
    elif answer in no:
        # Stores the variable as False, so a flexible response can be used outside the function
        yes_no.answer = False
    else:
        # Error message
        print("Please enter Yes or No\n")
        yes_no(question)


# This function displays the instructions for the user if they haven't played before
def instructions():
    # Displaying instructions for the user
    input("The program will give you a variety of different questions, most of these multi-choice questions, "
          "but some will be short answer questions.")
    input("If the question is multi-choice, please type the corresponding number to the answer you wish to give.")
    input("If the question is a short answer, please follow the on-screen instructions.")
    input("If you get 1 question wrong, you will lose the quiz.")
    print("However, if you get all the way to the end, you win!\n")


# This function asks a short answer question, with the parameters changing with the 'n' input e.g str, int, list
def user_info(question, n):
    while n == "str" or n == "list":
        user_info.response = input(question).lower().strip()
        if n == "str":
            if str.isalpha(user_info.response):
                print("That's a nice name!")
                user_info.name = user_info.response
                break
            else:
                print("Please enter a name using the letters A to Z")
        elif n == "list":
            if user_info.response in colors:
                print("Mine too!")
                user_info.col = user_info.response
                break
            else:
                print("I’m sorry, I don’t think I’ve heard of that colour, could you try another one?")
    while n == "int":
        try:
            user_info.response = int(input(question))
            if 1 <= user_info.response <= 118:
                print("Ok!")
                user_info.age = user_info.response
                break
            else:
                print("I don't think you could be that old...")
        except ValueError:
            print("I don’t recognize that number sorry...")


# This function generates a random question from the list 'Questions'
def question_gen():
    while True:
        # Generates a random question from the list
        rand = randint(0, 7)
        q = questions[rand]
        a = answers[rand]
        # If the question is in the 'used' list, the program carries on until it finds one that isn't
        if q in used:
            continue
        else:
            # This stores the question and adds it to the used list so a repeat question cannot occur
            question_gen.question = questions[rand]
            question_gen.answer = answers[rand]
            used.append(questions[rand])
            break


# This function takes the random question and answer, asks it and evaluates the response
def multi_question(question, ans):
    while True:
        try:
            # Asking the question
            answer = int(input(question))
            # Checking if the response fits the criteria before telling the user the result
            if 1 <= answer <= 3:
                if answer == ans:
                    print("Correct, {} was the right answer".format(answer))
                    multi_question.correct = True
                    break
                else:
                    # If the user gets the answer wrong
                    print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(answer))
                    multi_question.correct = False
                    break
            else:
                # If the user enters a number other than 1,2 or 3, then error
                print("I’m sorry, but I don’t think there was an option number {}".format(answer))
        except ValueError:
            # If the user enters something other than a number
            print("I’m sorry, I didn't recognize that input. Could you try again, remembering to only use numbers?")


# This function triggers the sequence of events at the end of the quiz in a losing scenario
def endgame():
    print("Sorry, {}, you lost the Quiz Fiesta".format(user_info.name))
    print("Your score was {}".format(score))
    exit()


# Asks the user a special question regarding colors
def spec_color():
    while True:
        if user_info.col in l1 or user_info.col in l2 or user_info.col in l3:
            color_response = input(r + "What colour is complimentary to the color you chose?\n").strip().lower()
            if str.isalpha(color_response):
                if color_response != user_info.col:
                    if color_response in l1 and user_info.col in l1:
                        print("Correct, {} was the right answer".format(color_response))
                        break
                    elif color_response in l2 and user_info.col in l2:
                        print("Correct, {} was the right answer".format(color_response))
                        break
                    elif color_response in l3 and user_info.col in l3:
                        print("Correct, {} was the right answer".format(color_response))
                        break
                    elif color_response in l4 and user_info.col in l4:
                        print("Correct, {} was the right answer".format(color_response))
                        break
                    else:
                        print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(
                            color_response))
                        endgame()
                        break
                else:
                    print("That was your favourite color, so what is the complimentary color to that?")
            else:
                print(
                    "I’m sorry, I didn’t recognize that input. Could you try again, remembering to type the complimentary colour to your favourite?")
        else:
            multi_question("What color is Skobeloff most similar to?\n 1. Blue\n 2. Red\n 3. Yellow\n", 1)
            break


# Asks the user a special question regarding numbers
def spec_num():
    ans = (user_info.age * 3) + 14

    while True:
        try:
            num_response = int(input("What is ({} x 3) + 14?\n".format(user_info.age)))
            if num_response == ans:
                print("Correct, {} was the right answer".format(num_response))
                break
            elif num_response == ans - 1 or num_response == ans + 1:
                print("So close, {} was unfortunately the wrong response. We’ll give you another shot".format(
                    num_response))
            else:
                print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(num_response))
                endgame()
                break
        except ValueError:
            print("I’m sorry, I didn’t recognize that input. Could you try again, remembering to only use numbers?")


# *****************************************************Main Sequence*****************************************************

# Title Screen
display()
print("-{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}".format(confetti))
input("       PRESS ENTER TO BEGIN            \n")

# Asking the user if they have played before and giving instructions if they haven't
yes_no(b + "Have you played {} before?\n".format(logo))
while not yes_no.answer:
    instructions()
    yes_no("Did you catch all that?\n")
input("Now, before we start, just a few questions...")
user_info("What is your name?\n", "str")
user_info("Thanks, {}, and how old did you say you were?\n".format(user_info.name), "int")
user_info("Last question: What's your favorite color?\n", "list")

input("All set now...")
print("Let the {} begin!".format(logo))

# Main Question asking sequence
while not finish:
    for i in range(2):
        for i in range(4):
            question_gen()
            multi_question(question_gen.question, question_gen.answer)
            if multi_question.correct:
                finish = False
                score += 1
            elif not multi_question.correct:
                endgame()
        # Runs the two special questions
        print("\n{0}{0}B{0}O{0}N{0}U{0}S{0}{0}Q{0}U{0}E{0}S{0}T{0}I{0}O{0}N{0}{0}\n".format(star))
        print("Wow, you're good to have made it this far!\n")
        if spec_color:
            spec_color()
            spec_color = False
        else:
            spec_num()
            finish = True
# The end screen of the game
print("Wow, you got a perfect score on {}!".format(logo))
print("\n{0}{0}C{0}O{0}N{0}G{0}R{0}A{0}T{0}U{0}L{0}A{0}T{0}I{0}O{0}N{0}S{0}{0}\n".format(star))
