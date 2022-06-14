friends = {"Bob", "Rolf", "Ann"}

abroad = {"Bob", "Ann"}
local_friends = {"Rolf"}

local_friends = friends.difference(abroad)
print(local_friends)

local = {"Rolf"}
abroad_friends = {"Bob", "Ann"}

friends = local.union(abroad)
print(friends)

math = {"Bob", "Rolf", "Ann"}
pol = {"Bob", "Ann"}
both = math.intersection(pol)

print(both)