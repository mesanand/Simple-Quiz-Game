#make the questions
questions = [
    {
        "question": "What school do I go to?",
        "choices": ["A. Harvard", "B. Princeston", "C. Northeastern", "D. IIT"],
        "answer": "c"
    },
    {
        "question": "Who is the senior associate Dean of Khoury?",
        "choices": ["A. Ben Hescott", "B. Abhishek Pujara", "C. Alavaro Monge", "D. Elizabeth Mynatt"],
        "answer": "a"
    },
    {
        "question": "What is my major?",
        "choices": ["A. Business", "B. Computer Science", "C. Applied Mathematics", "D. Gender Studies"],
        "answer": "b"
    },
    {
        "question": "Where do I live?",
        "choices": ["A. A small hut in Ghana", "B. An hotel in Boston", "C. Presidential Suite at the Ritz", "D. A cave under the Artic desert"],
        "answer": "b"
    }
]
#make a nice intro to the user
name = input("What is your first name ")
print(f"What's up, {name}")
# Prints out question
# gives you choices of A,B,C,D (edge case can be uppercase or lower case and spacing does not matter either)
def playQuiz(): 
    #Has to start with zero points and the first question, wth is question 0 
    score = 0 
    questionNum = 1
    print("let's start with a little game:\n" )
    
    for question in questions: 
        print(f"{questionNum} : {question['question']}") #Just push out the question 
        #an answer weird - the program can still take it (like edge cases) 
        #Same thing now just iterate through all the a-d choices they have
        for choice in question['choices']:
            print(choice)
        
        answer = input("YOU PUT:" ).strip().lower() #you gotta find out how to make it so that if they put
        
        if answer == question['answer']:
            score = score + 1 #they got it right!
        else: 
            score = score #They got it wrong!
            print("WRONG")
            
        questionNum = questionNum + 1 #move to next question
        
    
    print(f"ur final score is: ", score, "out of: ", len(questions)) 
playQuiz()
            