for num in range(1, 1000, 2):
    number = num ** 3
    numbers = number
    summ = 0
    while number > 0:
        summ += number % 10
        number = number // 10
    if not summ % 7:
        print('Number:', numbers, 'summ:', summ)
