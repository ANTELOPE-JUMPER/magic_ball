import random
from answer import answers


def start():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    user_name = str(input('Как тебя зовут? '))
    print(f'Приветствую тебя {user_name}\nНапиши вопрос который тебя волнует и я дам тебе ответ!')
    question = str(input('Введи вопрос: '))
    answe = random.choice(answers)
    print(f'Мой ответ:\n{answe}')


if __name__ == "__main__":
    start()
