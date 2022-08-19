#parametry

def sample(x, y):
    pass

def add(x, y):
    result = x + y
    print(result)

add(5, 3)


#error, zero parametrow
#def say_hello():
#    print("Hello!")
#
#say_hello("bob")

def second_say_hello(name, surname):
    print(f"Hello, {name} {surname}")

second_say_hello("Gruby", "Seba")


def third_say_hello(name, surname):
    print(f"Hello, {name} {surname}")

#zmiana kejnosci
second_say_hello(surname = "Gruby", name = "Seba")


def dzielenie(dzielna, dzielnik):
    if dzielnik != 0:
        print(dzielna/dzielnik)
    else:
        print("Nie dzielimy przez zero!")


dzielenie(10, 0)
dzielenie(10, 2)

