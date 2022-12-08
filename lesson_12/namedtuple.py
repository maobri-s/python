from collections import namedtuple

citizen = namedtuple("житель", "имя возраст статус какую_группу_ты_уважаешь")
alex = citizen(имя="Лёха Алексеев", возраст=27, статус="предприниматель", какую_группу_ты_уважаешь="Алексеева")

print(alex.имя)
print(alex.какую_группу_ты_уважаешь)
print(alex)