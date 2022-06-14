#listy, krotki, kolekcje
list = ["Bob", "Rolf", "Ann"]
tuple = ("Bob", "Rolf", "Ann")
set = {"Rolf", "Bob", "Ann"}

print(list[2])
print(tuple[2])
#print(set[2]) - w kolekcji kolejnosc nie jest zagwarantowana - nie zadziala
list[0] = "Smith"
print(list)

#tuple[0] = "Smith" - nie zadziala - zdefiniowana krotka nie moze byc modyfikowana
#to samo w kolekcji

list.append("Smith")
print(list)
list.remove("Smith")
print(list)

set.add("Wolf")
print(set)
set.add("Wolf")
print(set)

#set nie ma duplikatow
