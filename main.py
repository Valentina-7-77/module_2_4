# Всё не так уж просто!
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers)
# Создание пустых список
primes = []  # список простых чисел
not_primes = []  # список чисел, не являющихся простыми
for i in numbers:  # перебераем список numbers
    is_prime = True  # присваиваем переменной is_prime значение True
    if i == 1:  # у единицы делителей нет, поэтому продолжаем работать со следующим числом
        continue
    else:
        for j in range(2, i - 1):  # перебор делителей числа от двух до самого числа (не включительно))
            if i % j == 0:
                is_prime = False
                break
        if  is_prime == True:
            primes.append(i)
        else:
            not_primes.append(i)
print("Primes:", primes)  # Вывод списка простых чисел
print("Not Primes:", not_primes)  # Вывод списка чисел, не являющихся простыми