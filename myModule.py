def dzielenie(dzielna, dzielnik):
    return dzielna / dzielnik

print("mymodule.py: ", __name__)

#__name__ to zmienna globalna w Pythonie: zmienia się w zaleznosci od tego,
# w jakim pliku jest wywolana, w ten sposob mozesz odroznic pomiedzy plikiem wykonywanym,
# a importowanym, jezeli wykoujesz plik nieimportowanym,
# zmienna zwroci zawsze wartosc __main__