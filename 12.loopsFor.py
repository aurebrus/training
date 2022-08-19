friends = ["Kamil", "Slawek", "Agnieszki", "Piotr", "Mikolaj"]

for friend in friends:
    print(f"{friend} to moj przyjaciel")


# Cwiczenie
# Masz liste z wynikami testu: test = [35, 67, 90, 98, 100, 100]
# wykorzystaj petle for aby wyliczyc srednią ocen

grades = [35, 67, 90, 98, 100, 100]
total = 0
amount = len(grades)
for grade in grades:
    total += grade #total = total + grade
print(total / amount)

