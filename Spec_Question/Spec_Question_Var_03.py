age = 10

ans = (age * 3) + 14

while True:
    try:
        num_response = int(input("What is ({} x 3) + 14?\n".format(age)))
        if num_response == ans:
            print("Correct, {} was the right answer".format(num_response))
            spec_response = True
            break
        elif num_response == ans - 1 or num_response == ans + 1:
            print("So close, {} was unfortunately the wrong response. We’ll give you another shot".format(num_response))
        else:
            print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(num_response))
            spec_response = False
            break
    except ValueError:
        print("I’m sorry, I didn’t recognize that input. Could you try again, remembering to only use numbers?")

