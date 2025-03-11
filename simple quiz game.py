quiz={"what is python:":"Python is a versatile programming language.","what are variables:":"Variables are named storage for data."
,"define data:":"Data is information, often in digital form, for processing.","what are python functions:":"Python functions are reusable blocks of code performing specific tasks."
}
score=0
for question, correct_answer in quiz.items():
    
    print("\n Question:")
    print(question)

    #take users from the users
    answer=input("answers the question:")

    if  answer.strip().lower()==correct_answer.strip().lower():
        print("correct")
        score +=1
        
    else:
        print("incorrect answer")
    print("score:",score)
    