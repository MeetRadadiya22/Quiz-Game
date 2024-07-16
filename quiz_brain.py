class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0
  
  def next_question(self):
    final_question = self.question_list[self.question_number]
    self.question_number += 1
    typo = True
    while typo == True:
      user_question = input(f"\nQ.{self.question_number}: {final_question.text}(True/False): ") 
      user_question.lower()
      if user_question == "true" or user_question == "false" or user_question == "False" or user_question == "True":
        self.check_answer(user_question, final_question.answer)
        typo = False
      else:
        print("Invalid input. Try again.")
        typo = True
        
    
  def still_has_questions(self):
    return self.question_number < len(self.question_list)
  
  def check_answer(self, u_answer, c_answer):
    if u_answer.lower() == c_answer.lower():
      print("\nYou got it right.")
      self.score += 1
      print(f"Your score is {self.score}/{self.question_number}.")
      print()
    else:
      print("\nThat was the wrong answer.")
      print(f"The correct answer is {c_answer}.")
      print(f"Your score is {self.score}/{self.question_number}.")
    
      


     