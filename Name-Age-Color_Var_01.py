colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]

while True:
    name = input("What is your name?\n")
    if str.isalpha(name) == True:
        break
    else:
        print("Please enter a name using the letters A to Z")

while True:
    try:
        age = int(input("How old are you?\n"))
        if 1 <= age <= 118:
             break
        else:
            print("I don't think you could be that old...")
    except ValueError:
        print("I don’t recognize that number sorry...")

while True:
    fav_color = input("What is your favourite color?\n").strip().lower()
    if fav_color in colors:
        break
    else:
        print("I’m sorry, I don’t think I’ve heard of that colour, could you try another one?")
