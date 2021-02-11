from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q["text"],q["answer"]) for q in question_data]

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions() == True:
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
