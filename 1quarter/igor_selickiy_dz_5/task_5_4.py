# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Version with Compehansion-----------------------------------
result = [elem for elem in src[1:] if elem > src[src.index(elem) - 1]]
print(result)

# Version with gen and compehansion---------------------------
gen1 = (elem for elem in src[1:] if elem > src[src.index(elem) - 1])
result1 = [elem for elem in gen1]
print(result1)

# Version with gen and unpack--------------------------------
gen2 = (elem for elem in src[1:] if elem > src[src.index(elem) - 1])
result2 = [*gen2]
print(result2)
