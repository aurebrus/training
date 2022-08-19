#wykonywaliśmy już funkcje,np. print()

def hello():
    print("Hello!")

hello()

def user_age_in_seconds():
    user_age = int(input("Wprowadz swoj wiek: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Twój wiek w sekundach to: {age_seconds}.")

#separacja konceputalna
user_age_in_seconds()
print("Do widzenia!")


# zmienne tylko w funkcji

friends = ["Seba", "Lysy"]
def add_friends():
    friend_name = input("Wprowadź imie nowego przyjaciela: ")
    friends = friends + [friend_name]

#shadowing
add_friends()

# poprawna funkcja
def second_add_friends():
    friends.append("Gruby")

print(friends)

# musisz wyzej zdefiniowac funkcje, zanim ja uzyjesz

say_hello()
def say_hello():
    print("Hello!")






