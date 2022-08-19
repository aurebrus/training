movies_watched = {"Matrix", "Green Book", "Watchmen"}
user_movie = input("Wpisz co ostatnio ogladales/ogladalas:")

if user_movie in movies_watched:
    print(f"Takze ogladalem {user_movie}")
else:
    print("jeszcze nie ogladalem tego filmu")


# Zadanie
# Napisz program-gre, gdzie pytasz uzytkownika, czy chce zagrac (moze odpowiedziec y/n),
# a nastepnie ma wylosowac "szczesliwy numer".
# Porownaj numer z lista numerow wygrywajacych.
# Program wypisuje, czy uzytkownik trafil w jedna ze szczesliwych liczb

lucky_numbers = [2, 4, 22, 44]
user_input = input("Wpisz 'y' jezeli chcesz rozpoczac rozgrywke:").lower()

if user_input == "y":
    user_number = int(input("Odgadnij jedna ze szczesliwych liczb:"))
    if user_number in lucky_numbers:
        print("Wygrales")
    else:
        print("Nie udalo ci sie")