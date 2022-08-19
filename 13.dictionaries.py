# Słowniki
friend_ages = {"Piotr": 24, "Adam": 30, "Mikolaj": 35}

friend_ages["Robert"] = 40

print(friend_ages["Adam"])

friends = [
    {"name": "Piotr", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Mikolaj", "age": 35}
]

print(friends)
print(friends[2])
print(friends[2]["name"])

for friend in friend_ages:
    print(f"{friend}: {friend_ages[friend]}")


for friend, age in friend_ages.items():
    print(f"{friend}: {age}")

ages = friend_ages.values()
avarge_age = print(sum(ages) / len(ages))

