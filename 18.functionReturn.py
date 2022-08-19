def add(x, y):
    print(x + y)

add(5, 8)
result = add(5, 8) # nie przypisało zadnej wartosci, funkcje zwracaja "None" domyslnie
print(result)

def second_add(x, y):
    return x + y

second_add(5, 9) # nic nie wypisze - tylko zwraca

result = second_add(5, 10)
print(result)
print(second_add(5, 9)) # mozna tez krocej, od razu wywolac funkcje wewnatrz funkcji print


#zadanie - zmodyfikujcie funkcje dzielenie() z jednej z poprzednich przykladow
def dzielenie(dzielna, dzielnik):
    if dzielnik != 0:
        print(dzielna/dzielnik)
    else:
        print("Nie dzielimy przez zero!")


def dzielenie(dzielna, dzielnik):
    if dzielnik != 0:
        return dzielna / dzielnik
    else:
        return "Nie dziel przez zero"


