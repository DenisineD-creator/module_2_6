from random import randint

left_number = randint(3, 20)
result = ''

for i in range(1, left_number):
    for j in range(i + 1, left_number):
        if left_number % (i + j) == 0:
            result += str(i) + str(j)


print(result)