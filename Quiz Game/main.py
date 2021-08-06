from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = data["text"]
    answer = data["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You've completed the quiz.")
print(f"Your final score is : {quizBrain.score}/{quizBrain.question_number}.")
