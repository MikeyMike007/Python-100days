# Creating classes

## About classes and objects

- A class is a blueprint

`class Car:`

- In python, you use `snake_case` for naming variables.

- Constructor

```python
Class Car:

  def __init__(self, seats):
	  self.seats = seats
```

- Initiate a object

`my_var = Car(5)`

## Instagram example

```py
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # default value
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)

```

## Quiz program

![](Day%2017%20-%20Creating%20classes/Ska%CC%88rmavbild%202020-12-30%20kl.%2006.27.30.png)

```py
# question_model.py

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

![](Day%2017%20-%20Creating%20classes/Ska%CC%88rmavbild%202020-12-30%20kl.%2007.15.15.png)

```py
# quiz_brain.py

class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        number_of_questions = len(self.question_list)
        if self.question_number < number_of_questions:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct question was: {correct_answer}.")
        print(f"Your current score is {self.score} / {self.question_number}")
```

```py
# main.py

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}
```

```py
# data.py

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
```

![](Day%2017%20-%20Creating%20classes/Ska%CC%88rmavbild%202020-12-30%20kl.%2007.28.27.png)

#Courses/Python/100-days-of-code

