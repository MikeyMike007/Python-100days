# Quiz game
# Data -> Brain -> UI format

from question_model import Question
from data import QuestionData
from quiz_brain import QuizBrain
from ui import QuizInterface

ENDPOINT = "https://opentdb.com/api.php"
PARAMS = {"amount": "10", "type": "boolean"}

data = QuestionData(ENDPOINT, PARAMS)
question_bank = []

for question in data.fetch_data():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
