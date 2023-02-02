import easygui
import random


def rock_paper_scissors():
    otvets = {"kamen": "img/kamen.png",
     "noghneci": "img/noghneci.png",
     "bumaga": "img/bumaga.png"}
    result = easygui.buttonbox(
        msg="выбери фигурку👽",
        title="kamen, nozhneci, bumaga",
        images=["img/kamen.png", "img/nozhneci.png", "img/bumaga.png"],
        choices=("протяни свою руку, а я попробую поймать",)
    )

    print(otvets.keys())
    # answer_comp = random.choice(list(otvets.keys()))
    answer_comp = "noghneci"
    print(answer_comp)
    if result == otvets["kamen"] and answer_comp == "noghneci":
        easygui.msgbox(msg="ураааааааа🐸")
        # ТУТ МОЖНО ДОПИСАТЬ С:


def guess_the_number():
    n = easygui.integerbox(msg="какое чиселко?",
                   lowerbound=1,
                   upperbound=99)
    n_c = random.randint(1,99)
    if n == n_c:
        return  # выход из функции

    while n != n_c:
        if n > n_c:


    n = easygui.integerbox(msg="какое чиселко?",
                               lowerbound=1,
                               upperbound=99,
                               image="img/menyushe.png")


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()
