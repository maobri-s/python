import random
import playsound

class MusicBox:
    def __init__(self):
        self.variants = "lgbt"  # варианты угадываемых звуков
        self.score = 0  # счёт
        self.sequence = random.choice(self.variants)  # отгадываемая последовательность
    def __next(self):
        dlina = len(self.sequence) + 1  # прибавляем к длине
        self.sequence = ""
        for _ in range(dlina):
            self.sequence += random.choice(self.variants)
    def check(self, user):
        if user == self.sequence:
            playsound.playsound("sounds/correct.wav")
            self.__next()
            self.score += 1
        else:
            playsound.playsound("sounds/incorrect.wav")
            self.score -= 0.5
    def play(self):
        for letter in self.sequence:
            playsound.playsound(f"sounds/{letter}.mp3")
