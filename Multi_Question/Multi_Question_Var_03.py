from random import randint
score = 0

def question_gen():
    q = randint(1, 3)
    if q == 1:
        question_gen.question = ["Which number is highest?\n", "1: fifty-three\n", "2: four", "3: twelve\n", 1]
    elif q == 2:
        question_gen.question = [" In 1768, Captain James Cook set out to explore which ocean?\n", "1: Pacific Ocean\n", "2: Atlantic Ocean",
      "3: Arctic Ocean\n", 1]
    elif q == 3:
        question_gen.question = ["What is actually electricity?\n", "1: A flow of Air\n", "2: A flow of water", "3: A flow of electrons\n", 3]
    else:
        print("")
    return q
def multi_question(list, score):
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

while 0 <= score < 2:
    question_gen()
    multi_question(question_gen.question, score)
    if multi_question.correct == True:
        score += 0
    elif multi_question.correct == False:
            score += 1
