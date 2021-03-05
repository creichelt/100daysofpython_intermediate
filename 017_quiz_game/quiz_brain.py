class QuizBrain:

    def __init__(self,q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    def next_question(self):
        curr_q = self.q_list[self.q_number]
        self.q_number += 1
        user_answ = input(f"\nQ.{self.q_number}: {curr_q.text} (True/False): ")
        self.check_answer(user_answ, curr_q.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self,user_answ, corr_answ):
        if user_answ.lower() == corr_answ.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong :(")
        print(f"The correct answer is: {corr_answ}")
        print(f"Your current score {self.score}/{self.q_number}")