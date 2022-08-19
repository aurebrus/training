def dzielenie(dzielna, dzielnik):
    if dzielnik == 0:
        print("Nie dziel przez 0!")
        return
    return dzielna / dzielnik

print(dzielenie(15, 0))


# program oczekuje, ze funkcja bedzie dzialac zawsze poprawnie

grades = [2, 5, 6] # co sie stanie jak tablica bedzie pusta?


print("Witam w programie srednia ocen")
average = dzielenie(sum(grades), len(grades))
print(f"Srednia ocen wynosi: {average}.")

second_grades = []

def second_dzielenie(dzielna, dzielnik):
    if dzielnik == 0:
        raise ZeroDivisionError("Dzielnik nie moze wynosic 0") #ZeroDivisionError to defaultowy error w Pythonie
    return dzielna / dzielnik


#print("Witam w programie srednia ocen")
#average = second_dzielenie(sum(second_grades), len(second_grades))
#print(f"Srednia ocen wynosi: {average}.")


print("Witam w programie srednia ocen")
try:
    average = second_dzielenie(sum(second_grades), len(second_grades))
except ZeroDivisionError as err:
    print("W tablicy nie ma ocen")
else:
    print(f"Srednia ocen wynosi: {average}.")
finally:
    print("Wyswietle sie, jezeli nie zostanie spelniony zaden z powyzszych warunkow")

