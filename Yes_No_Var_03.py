yes = ["y", "yes", "yep", "affirmative", "yea"]
no = ["n", "no", "nope", "negative", "nah"]


def yes_no(question):
    answer = None
    answer = input(question).strip().lower()
    if answer in yes:
        yes_no.answer = True
    elif answer in no:
        yes_no.answer = False
    else:
        print("Please enter Yes or No\n")
        yes_no(question)

#For infinite loop, not present in final program
while True:
    yes_no("Have you played this quiz before?\n")
    if yes_no.answer == True:
        print("Program continues\n")
    elif yes_no.answer == False:
        print("This is how the game works:...\n")
