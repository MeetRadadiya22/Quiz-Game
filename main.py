from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data["results"]:
  
  q = i["question"]
  a = i["correct_answer"]
 
  question = Question(q, a)
  
  question_bank.append(question)


quiz = QuizBrain(question_bank)

while  quiz.still_has_questions() == True: 
  quiz.next_question()
print("\nYou have completed the Quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
  
  


