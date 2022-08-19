#Cwiczenie
#1. Utworz funkcje user_name(), która zapyta uzytkownika o imie i zwroci to imie
#2. Utworz funkcje greeting(), ktora przyjmuje imie jako argument
# i wypisze "Czesc {imie}, jak sie masz?"

def user_name():
    user_input = input("Jak masz na imie?")
    return user_input

def greeting(name):
    print(f"Czesc, {name}. jak sie masz?")

def main():
    name = user_name()
    greeting(name)

if __name__ == '__main__':
    main()

#Zadanie
# Czy liczba a jest podzielna przez liczbe b?
# Funkcja divisible ponizej bierze dwie liczby i sprawdza, czy liczba num1 jest podzielna przez num2
# divisible(6, 2) zwraca True ponieważ 6/2 is 3, bez reszty
# divisible(7, 2) zwraca False ponieważ 7/2 to 3, z resztą (1)
def divisible(num1, num2):
    return num1 % num2 == 0


def user_even():
    first_number = int(input("podaj dzielnik"))
    second_number = int(input("podaj dzielna"))
    if divisible(first_number, second_number) == True:
        print(f"liczba {first_number} jest podzielna przez liczbe {second_number}")
    else:
        print(f"liczba {first_number} nie jest podzielna przez liczbe {second_number}")


user_even()

# podpowiedź num1 % num2 == 0
# skorzystaj z niej w srodku funkcji user_even

# zapytaj uzytkownika o 2 liczby.
# Wypisz "liczba {num1} jest podzielna przez liczbe {num2}" - bedzie tak, jezeli reszta z dzielenia bedzie wynosic 0.
# I odwrotnie.
# (upewnij sie, ze rzutujesz input uzytkownika na int!)
