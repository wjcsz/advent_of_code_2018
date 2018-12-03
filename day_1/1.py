input = open("input", "r+")

numbers_sum = 0
for number in input:
    if number[0] == "+":
        numbers_sum = numbers_sum + int(number[1::])
    else:
        numbers_sum = numbers_sum - int(number[1::])
print(numbers_sum)
