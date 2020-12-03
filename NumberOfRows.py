bowls = 0
rows = 5

for i in range(1, rows + 1):
    bowls = bowls + 1 * i

print(bowls)


## drugi sposób
def how_many(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + 1 * i

    return sum


print(how_many(5))
