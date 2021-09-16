q1 = ["Which number is highest?\n", "1: fifty-three\n", "2: four", "3: twelve\n", 1]


score = 0
def multi_question(list, score):
    while True
        try:
            print(list[0] + list[1] + list[2])
            answer = int(input(list[3]))
            while True:
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

while 0 <= score < 2:
    multi_question(q1, score)
    if multi_question.correct == True:
        score = 0
    elif multi_question.correct == False:
        score += 1
