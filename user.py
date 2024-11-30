#make the questions
questions = [
("What school do I go to", "Northeastern"),("Who is the senior associate Dean of Khoury","Ben Hescott"),
("What is my major", "computer science"), ("Where do I live", "New York")
]
#make a nice intro to the user
name = input("What is your name? ")
print(f"Hello, {name}")
# Prints out question
# gives you choices of A,B,C,D (edge case can be uppercase or lower case and spacing does not matter either)
def playQuiz(): 
    #Has to start with zero points and the first question, wth is question 0 
    score = 0 
    questionNum = 1
    print("let's start with a little game:\n" )
    
    for question in questions: 
        print(f"{questionNum} : {question[0]}") #Just push out the question 
        answer = input("YOU PUT:" ).strip() #you gotta find out how to make it so that if they put 
        #an answer weird - the program can still take it (like edge cases) 
        
        if answer.lower() == question[1].lower():
            score = score + 1 #they got it right!
        else: 
            score = score #They got it wrong!
            print("nu uh")
        questionNum = questionNum + 1 #move to next question
        
    
    print(f"ur final score is: ", score, "out of: ", len(questions)) 
playQuiz()
            