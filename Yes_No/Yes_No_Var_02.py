def yes_no():
    answer = input("Have you played this quiz before?").strip().lower()
    if answer == "yes":
        print("Program continues")
    elif answer == "no":
        print("This is how the game works:...")
    else:
        print("Please enter Yes or No")

#For infinite loop, not present in final program
while True:
    yes_no()
