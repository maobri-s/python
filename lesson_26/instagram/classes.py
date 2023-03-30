import requests
import random
class User:
    def __init__(self):
        self.__lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sollicitudin id purus eget pulvinar. Aenean ligula enim, bibendum eu euismod non, lobortis a ante. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque luctus orci a tortor interdum accumsan. Ut interdum ipsum arcu, vitae venenatis risus pulvinar eu. Proin consequat interdum justo, vel dictum elit pretium a."
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__data["Login"]
        self.__password = self.__data["Password"]
        self.imya = self.__data["FirstName"]
        self.familya = self.__data["LastName"]
        self.posts = [self.__lorem[random.randint(0, 35):random.randint(36,70)]]