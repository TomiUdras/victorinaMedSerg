import random

global_variable = 0
global_variable_n = 0


def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            user_answer = int(input("Выберите номер правильного ответа: "))
            global global_variable
            global_variable = user_answer
            if 1 <= user_answer <= len(options):
                break
            else:
                print(f"Пожалуйста, выберите номер от 1 до {len(options)}")
        except ValueError:
            print("Введите целое число.")

    if user_answer == correct_option:
        print("Правильно!\n")
        return 1
    else:
        global global_variable_n
        global_variable_n += 1
        if global_variable_n > 5:
            print("К сожалению, вы не угадали\n")
            return 0
        else:
            if do_it_a_second_time(question, options, correct_option) == 0:
                return 0


def do_it_a_second_time(question, options, correct_option):
    print("\nНеправильно( \nПопробуем еще раз?")
    while True:
        try:
            yesORno = int(input("1. ДА \n2. НЕТ \nВаш ответ: "))
            print("\n")
            if 1 <= yesORno <= 2:
                break
            else:
                print(f"Пожалуйста, выберите номер от 1 до 2")
        except ValueError:
            print("Введите целое число.")
    if yesORno == 1:
        ask_question(question, options, correct_option)
    else:
        return 0


def write_results_to_file(results, filename):
    with open(filename, "w") as file:
        file.write("Вопросы, ответы пользователя и правильные ответы:\n\n")
        for result in results:
            file.write(f"Вопрос: {result['question']}\n")
            file.write(f"Ответ пользователя: {result['user_answer']}\n")
            file.write(f"Правильный ответ: {result['correct_answer']}\n\n")

        file.write(
            f"Итоговый счет: {sum(result['score'] for result in results)}/{len(results)}\n"
        )
        file.write("Результат: Хороший результат" if sum(
            result['score'] for result in results) >= len(results) /
                   2 else "Результат: Плохой результат")


def main():
    score = 0
    results = []

    questions = [
        {
            "question":
            "Что такое анемия??",
            "options": [
                "Недостаточное количество красных клеток в крови",
                "Воспалительный процесс в легких", "Заболевание почек",
                "Сахарный диабет"
            ],
            "correct_option":
            1
        },
        {
            "question":
            "Что такое артериальное давление?",
            "options": [
                "Давление крови в мозге", "Давление крови в венах",
                "Давление крови в артериях", "Давление в легких"
            ],
            "correct_option":
            3
        },
        {
            "question":
            "Что такое инфекционные болезни? ",
            "options": [
                "Болезни, вызванные вирусами, бактериями, грибками или паразитами",
                "Болезни, вызванные генетическими нарушениями",
                "Болезни, вызванные стрессом",
                "Болезни, вызванные вредными привычками "
            ],
            "correct_option":
            1
        },
        {
            "question":
            "Что такое рентгенология?",
            "options": [
                "Метод изучения органов и тканей с помощью радиоволн",
                "Метод изучения органов и тканей с помощью рентгеновских лучей ",
                "Метод изучения органов и тканей с помощью магнитного резонанса",
                "Метод изучения органов и тканей с помощью ультразвука"
            ],
            "correct_option":
            2
        },
        {
            "question":
            "Что такое астма?",
            "options": [
                "Заболевание печени",
                "Заболевание легких, характеризующееся спазмами бронхов",
                "Заболевание сердца", "Заболевание кожи"
            ],
            "correct_option":
            2
        },
        {
            "question":
            "Что такое онкология?",
            "options": [
                "Область медицины, занимающаяся лечением ран, порезов и ушибов",
                " Область медицины, занимающаяся лечением раковых заболеваний",
                "Область медицины, занимающаяся лечением инфекционных болезней",
                "Область медицины, занимающаяся лечением генетических заболеваний"
            ],
            "correct_option":
            2
        },
        {
            "question":
            "Что такое аллергия?",
            "options": [
                "Реакция организма на алкоголь", "Реакция организма на пищу",
                "Реакция организма на вещество, вызывающее повышенную чувствительность",
                " Реакция организма на солнечные лучи"
            ],
            "correct_option":
            3
        },
        {
            "question":
            "Что такое гипертония?",
            "options": [
                " Повышенное артериальное давление",
                "Пониженное артериальное давление", "Заболевание костей",
                "Заболевание кожи"
            ],
            "correct_option":
            2
        },
        {
            "question":
            "Что такое артрит?",
            "options": [
                "Заболевание печени", " Заболевание суставов",
                " Заболевание кожи", "Заболевание сердца"
            ],
            "correct_option":
            2
        },
        {
            "question":
            "Что такое иммунитет?",
            "options": [
                "Способность организма сопротивляться инфекциям и болезням",
                "Способность организма самостоятельно побеждать все болезни",
                "Способность организма побеждать болезни с помощью препаратов",
                "Способность организма вырабатывать вирусы для лечения других болезней"
            ],
            "correct_option":
            1
        },
    ]

    random.shuffle(questions)

    for q in questions:
        score = ask_question(q["question"], q["options"], q["correct_option"])
        if score == None:
            score = 0
        user_answer = global_variable
        user_answer = q["options"][user_answer - 1]
        results.append({
            "question": q["question"],
            "user_answer": user_answer,
            "correct_answer": q["options"][q["correct_option"] - 1],
            "score": score
        })

    write_results_to_file(results, "results.txt")


if __name__ == "__main__":
    main()
