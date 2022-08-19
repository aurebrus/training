def multiply(*args):
    print(args)


#mowimy tutaj, ze funcja przyjmuje zestaw argumentow, ktore beda przechowane w
# kolekcji argumentow

multiply(1, 2, 5)


#mozesz iterowac po tych argumentach

def second_multiply(*args):
    total = 1
    for arg in args:
        total = total + arg
    return total

print(second_multiply(1, 3, 5))

# dekonstrukcja tablicy

def add(x, y):
    return x + y

nums = [3, 5]
result = add(*nums)
print(result)

# dekonstrukcja kolekcji

dict = {"x": 15, "y": 25}
print(add(**dict))