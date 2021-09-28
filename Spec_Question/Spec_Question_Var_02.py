color = "brown"
l1 = ["red", "green"]
l2 = ["blue", "orange"]
l3 = ["yellow", "purple"]
l4 = ["brown", "pink"]
question = ["What color is Skobeloff most similar to?\n", "1. Blue\n", "2. Red", "3. Yellow\n", 1]
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
def spe_color():
    while True:
        if color in l1 or color in l2 or color in l3:
            color_response = input("What colour is complimentary to the color you chose?").strip().lower()
            if str.isalpha(color_response) == True:
                if color_response != color:
                    if color_response in l1 and color in l1:
                        print("Correct, {} was the right answer".format(color_response))
                        col = True
                        break
                    elif color_response in l2 and color in l2:
                        print("Correct, {} was the right answer".format(color_response))
                        col = True
                        break
                    elif color_response in l3 and color in l3:
                        print("Correct, {} was the right answer".format(color_response))
                        col = True
                        break
                    elif color_response in l4 and color in l4:
                        print("Correct, {} was the right answer".format(color_response))
                        col = True
                        break
                    else:
                        print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(color_response))
                        col = False
                        break
                else:
                    print("That was your favourite color, so what is the complimentary color to that?")
            else:
                print("I’m sorry, I didn’t recognize that input. Could you try again, remembering to type the complimentary colour to your favourite?")
        else:
            multi_question(question)
            break
