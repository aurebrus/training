#Pętle

lucky_numbers = [2, 4, 22, 44]
user_input = input("Czy chcialbys zagrac? (Y/n):")

#while
while user_input != "n":
    user_number = int(input("Odgadnij jedna ze szczesliwych liczb:"))
    if user_number in lucky_numbers:
        print("Wygrales")
    else:
        print("Nie udalo ci sie")
    user_input = input("Czy chcialbys zagrac? (Y/n):")

#jeszcze lepiej
while True:
    if user_input == "n":
        break
    user_input = input("Czy chcialbys zagrac? (Y/n):")
    user_number = int(input("Odgadnij jedna ze szczesliwych liczb:"))
    if user_number in lucky_numbers:
        print("Wygrales")
    else:
        print("Nie udalo ci sie")
