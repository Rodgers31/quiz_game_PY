class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        question_len = len(self.question_list)
        # Will return true or false
        return self.question_number < question_len

    def nex_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)
        print(f'Your score is {self.score}/{self.question_number}')
        print("\n")
        return self.score, self.question_number

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Correct answer is: {current_question}")


