#make the questions
questions = [
("What school do I go to", "Northeastern"),("Who is the senior associate Dean of Khoury","Ben Hescot"),
("What is my major", "computer science"), ("Where do I live", "New York")
]
#make a nice intro to the user
name = input("What is your name? ")
print(f"Hello, {name}")
#Prints out question
# gives you choices of A,B,C,D (edge case can be uppercase or lower case and spacing does not matter either)
def playQuiz(): 
    #Has to start with zero points and the first question, wth is question 0 
    score = 0 
    questionNum = 1
    print("let's start with a little game:\n" )
    
    for question in questions: 
        print(f"{questionNum} : {question[0]}") #Just push out the question 
        