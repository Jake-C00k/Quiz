choice = [1, 2, 3]

def multi_question(question, c1, c2, c3, ans):
    try:
        answer = int(input(question + c1 + c2 + c3))
        while True:
            if answer in choice:
                if answer == ans:
                    multi_question.score = 0
                    print("Correct, {} was the right answer".format(answer))
                    break
                else:
                    multi_question.score += 1
                    print("Incorrect, {} was unfortunately the wrong response. Better luck next time".format(answer))
                    break
            else:
                print("I’m sorry, but I don’t think there was an option number {}".format(answer))
                break
    except ValueError:
        print("I’m sorry, I didn’t recognize that input. Could you try again, remembering to only use numbers?")


