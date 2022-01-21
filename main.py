mass1 = [7, 5, 10, 12]
mass2 = [7, 5]
result = [10, 12]

diff = list(set.difference(set(mass1), set(mass2)))  # находим разницу mass1 и mass2
print(diff == result)  # сравниваем diff и result
