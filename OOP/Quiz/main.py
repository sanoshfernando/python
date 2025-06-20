from question_model import Question
from data import question_data
question_bank=[]
for i in question_data:
    question_text=i["text"]
    question_answer = i["answer"]
    question_bank.append(Question(question_text,question_answer))

print(question_bank)

