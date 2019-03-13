def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("Correct! You've got {0} correct so far!".format(score))
            print("")
        else: 
            print("Sorry, that's not right")
            print("")
    
    print("")
    print("----------------------------")
    print("Game over!")
    print("Your final score is {0}/{1}".format(score, number_of_questions))
    print("----------------------------")
    print("")

def add_question():
    print("")
    question = input("Enter a question\n>")
    
    print("")
    print("Okay, now tell me the answer")
    answer = input("{0}\n>".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("You selected an invalid option")
        print("")

game_loop()