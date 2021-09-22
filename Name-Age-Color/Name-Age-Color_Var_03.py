colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]

def question_answer(question, n):
    while n == "str" or n == "list":
        question_answer.response = input(question).lower().strip()
        if n == "str":
            if str.isalpha(question_answer.response) == True:
                print("That's a nice name!")
                break
            else:
                print("Please enter a name using the letters A to Z")
        elif n == "list":
            if question_answer.response in colors:
                print("Mine too!")
                break
            else:
                print("I’m sorry, I don’t think I’ve heard of that colour, could you try another one?")
    while n == "int":
        try:
            question_answer.response = int(input(question))
            if 1 <= question_answer.response <= 118:
                print("Ok!")
                break
            else:
                print("I don't think you could be that old...")
        except ValueError:
            print("I don’t recognize that number sorry...")







