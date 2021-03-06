# 1. Сумма чисел, кратных 3 или 5
def e1(limit):
    total = 0
    for i in range(0, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# Чётные числа Фибоначчи
def e2(limit):
    pass


# Наибольший простой делитель числа 600851475143
def e3():
    for num in range(2, 10):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            print(num)


# Число-палиндром
def e4():
    s = [1, 3, 7]
    result = 0
    for i in range(1000):
        for j in range(1000):
            m = i * j
            if str(m) == str(m)[::-1] and m > result:
                print(f'a = {i}; b = {j}')
                result = m
    print(result)


def e5():
    def is_divisible(number):
        for i in range(1, 21):
            if number % i != 0:
                return False
        return True

    n = 20
    while True:
        if is_divisible(n):
            break
        n += 20

    print(n)


def e6():
    a = 0
    b = 0
    for i in range(1, 101):
        a += i ** 2
        b += i
    result = b ** 2 - a
    print(result)


def e7():
    primes = []
    num = 2
    while len(primes) < 10001:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            primes.append(num)
        num += 1
    print(primes[-1])


# Наибольшее произведение четырех последовательных цифр в нижеприведенном 1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
# Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
def e8():
    n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

    # Преобразуем число в последовательность цифр
    l = [int(i) for i in str(n)]
    c = 13
    m = 1
    r = 0
    for i in range(len(l) - c):
        for j in range(c):
            m *= l[i + j]
        if m > r:
            r = m
        m = 1
    print(r)


def e9():
    pass


# Мой вариант - очень долгий, неоптимальный.
def e10_1():
    import time
    limit = 10
    result = 0
    start_time = time.time()
    for num in range(2, limit):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            result += num
    print(result)
    print('Time:', time.time() - start_time, 'sec')


# Намного быстрее
# https://youtu.be/vuC9b5-XPo8
def e10_2():
    import time

    limit = 2000000
    is_prime_array = [True] * limit

    def prime_sieve(prime_array):
        summ = 0
        for i in range(2, len(prime_array)):
            if prime_array[i]:
                summ += i
                k = i + i
                while k < len(prime_array):
                    prime_array[k] = False
                    k += i
        return summ

    start_time = time.time()
    the_sum = prime_sieve(is_prime_array)

    print(the_sum)
    print("Time:", time.time() - start_time, 'Sec')


# External lib - самый быстрый
# https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p010.py
def e10_3():
    import eulerlib
    ans = sum(eulerlib.primes(1999999))
    return ans


import timeit

t = timeit.timeit(lambda: e10_3(), number=1)
print(t)
# e10_2()
# e10_3()
