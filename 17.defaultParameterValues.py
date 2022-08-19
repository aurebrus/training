def add(x, y=9):
    print(x + y)

add(5)
add(5, 14)
add(y=14)

# parametry defaultowe moga byc podane tylko na koncu listy parametrow
# nie można zrobic tak:
#def add(x=10, y)