from musicbox import MusicBox
musicbox = MusicBox()  # проигрыватель
while True:
    musicbox.play()
    user = input("что ты услышал?: ").lower()
    if user == "":  # если ответ пустой
        break
    musicbox.check(user)