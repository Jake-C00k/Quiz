colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
response = ["Ok!", "Right", "Sounds about right"]

while True:
    name = input("What is your name?\n")
    if str.isalpha(name) == True:
        print("That's a nice name!")
        break
    else:
        print("Please enter a name using the letters A to Z")

while True:
    try:
        age = int(input("How old are you?\n"))
        if 1 <= age <= 118:
            print("Right!")
             break
        else:
            print("I don't think you could be that old...")
    except ValueError:
        print("I don’t recognize that number sorry...")

while True:
    fav_color = input("What is your favourite color?\n").strip().lower()
    if fav_color in colors:
        print("Mine too!")
        break
    else:
        print("I’m sorry, I don’t think I’ve heard of that colour, could you try another one?")
