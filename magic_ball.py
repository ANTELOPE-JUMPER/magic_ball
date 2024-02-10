import random
from answer import answers


def start():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    user_name = str(input('Как тебя зовут? '))
    print(f'Приветствую тебя {user_name}\nНапиши вопрос который тебя волнует и я дам тебе ответ!')
    answet_to_question()


def answet_to_question():
    question = str(input('Введи вопрос: '))
    answe = random.choice(answers)
    print(f'Мой ответ:\n{answe}')
    question = int(input('Будут ли еще вопросы? 1=Да 0=Нет\n'))
    print(question)
    if question == 1:
        answet_to_question()
    else:
        print('Возвращайся если возникнут вопросы!')


if __name__ == "__main__":
    start()
