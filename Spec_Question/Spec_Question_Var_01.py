name = "N"
color = "blue"
age = 10
l1 = ["red", "green"]
l2 = ["blue", "orange"]
l3 = ["yellow", "purple"]
l4 = ["pink", "lime"]
l5 = ["brown", "teal"]

ans = (age * 3) ** 2 + 1

while True:
    try:
        num_response = int(input("What is ({} x 3) squared + 1?".format(age)))
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
while True:
    color_response = input("What colour is complimentary to the color you chose?").strip().lower()
    if str.isalpha(color_response) == True:
        if color_response != color:
            if color_response in l1 and color in l1:
                print("Correct, {} was the right answer".format(color_response))
                break
            elif color_response in l2 and color in l2:
                print("Correct, {} was the right answer".format(color_response))
                break
            elif color_response in l3 and color in l3:
                print("Correct, {} was the right answer".format(color_response))
                break
            elif color_response in l4 and color in l4:
                print("Correct, {} was the right answer".format(color_response))
                break
            elif color_response in l5 and color in l5:
                print("Correct, {} was the right answer".format(color_response))
                break
            elif color_response in l5 and color in l5:
                print("Correct, {} was the right answer".format(color_response))
                break
            else:
                print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(color_response))
                break
        else:
            print("That was your favourite color, so what is the complimentary color to that?")
    else:
        print("")
