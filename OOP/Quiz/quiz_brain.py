class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1  # Important!

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print("That's correct")
        else:
            print("That's wrong")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is: {self.current_score}/{self.question_number + 1}")
