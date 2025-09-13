import random
questions={
    "What is the keyword to define a function in Python?":"def", 
    "Which data type is used to store True or False values?":"boolean",
     "What is the correct file extension for Python files?":".py", 
     "Which symbol is used to comment in Python?":"#”, 
     "What function is used to get input from the user?":"input", 
     "How do you start a for loop in Python?":"for", 
     "What is the output of 2 ** 3 in Python?":"8", 
     "What keyword is used to import a module in Python?":"import", 
     "What does the len() function return?":"length", 
     "What is the result of 10//3?":"3"
}
def quiz_game():
    questions_list=list(questions.keys())
    total_questions=5
    score=0
    random_questions=random.sample(questions_list,total_questions)
    for i,question in enumerate(random_questions):
        print(f"{i+1}.{question}")
        user_input=input("Enter Your Answer : ").lower().strip()
        correct_answer=questions[question]
        if user_input==correct_answer:
            print(f"you correct the answer,congratulations🎉...\n")
            score+=1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")
    print(f"Game over!,Your total score is {score}/{total_questions}✔")
quiz_game()