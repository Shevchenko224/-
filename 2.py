import random
def guess_the_number():
    secret_number = random.randint(1, 10)
    print("Гра 'Вгадай число'. У вас 3 спроби.")
    for _ in range(3):
        guess = int(input("Введіть число від 1 до 10: "))
        if guess < secret_number:
            print("Більше!")
        elif guess > secret_number:
            print("Менше!")
        else:
            print("Ви вгадали!")
            return
    print(f"Ви програли! Число було: {secret_number}")
def print_range():
    start = int(input("Початок діапазону: "))
    end = int(input("Кінець діапазону: "))
    print(*range(start, end + 1))
def print_reverse_even_numbers():
    n = int(input("Введіть n: "))
    print(*[i for i in range(n, 0, -1) if i % 2 == 0])
def factorial():
    n = int(input("Введіть число для факторіалу: "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Факторіал: {result}")
def determine_grade():
    score = int(input("Введіть бали: "))
    if 0 <= score <= 49:
        print("Незадовільно")
    elif 50 <= score <= 69:
        print("Задовільно")
    elif 70 <= score <= 89:
        print("Добре")
    elif 90 <= score <= 100:
        print("Відмінно")
    else:
        print("Некоректний бал!")