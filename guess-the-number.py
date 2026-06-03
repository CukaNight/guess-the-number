import random
import time

print("Привет!\nДобро пожаловать в игру «Угадай число».\nТвоя задача — отгадать, какое число загадал компьютер.\nЗа каждую победу ты получаешь одно очко.\nЧем больше очков ты соберешь, тем круче будешь!")
time.sleep(3)

attempts = 0
points = 0

while True:
    
    print("Для начала давай выберем сложность:\n1. Лёгкая от 1 до 50\n2. Нормальная от 1 до 100\n3. Сложная от 1 до 500\n4. Невозможная от 1 до 10.000!\n0. Выход")
    choise1 = int(input("Ваш выбор: "))

    if choise1 == 1:
        print("Начать игру-1\nЗакончить игру-2")
        choise = int(input("Ваш выбор: "))

        if choise ==1:
            number = random.randint(1,50)
            print("Я загадал рандомное число от 1 до 50. Угадывай!")
            while True:
                your_number = int(input("Как ты думаешь какое это число "))
                attempts=attempts+1

                if attempts == 7:
                    print(f"Ты проиграл твоих попыток слишком много 7 число было {number}!")
                    attempts = 0
                    break
                elif your_number > number:
                    print("Число компьютера меньше!")
                elif your_number < number:
                    print("Число компьютера больше!")
                else:
                    print(f"Поздравляю! Угадал за {attempts} попыток")
                    points=points+1
                    print(f"Теперь у тебя {points} очков!")
                    attempts = 0
                    break
        
        elif choise == 2:
            break

        else:
            print("Выбери 1 или 2")
            continue

    elif choise1 == 2:
        print("Начать игру-1\nЗакончить игру-2")
        choise = int(input("Ваш выбор: "))

        if choise ==1:
            number = random.randint(1,100)
            print("Я загадал рандомное число от 1 до 100. Угадывай!")
            while True:
                your_number = int(input("Как ты думаешь какое это число "))
                attempts=attempts+1

                if attempts == 10:
                    print(f"Ты проиграл твоих попыток слишком много 10 число было {number}!")
                    attempts = 0
                    break
                elif your_number > number:
                    print("Число компьютера меньше!")
                elif your_number < number:
                    print("Число компьютера больше!")
                else:
                    print(f"Поздравляю! Угадал за {attempts} попыток")
                    points=points+3
                    print(f"Теперь у тебя {points} очков!")
                    attempts = 0
                    break
        
        elif choise == 2:
            break

        else:
            print("Выбери 1 или 2")
            continue
    
    elif choise1 == 3:
        print("Начать игру-1\nЗакончить игру-2")
        choise = int(input("Ваш выбор: "))

        if choise ==1:
            number = random.randint(1,500)
            print("Я загадал рандомное число от 1 до 500. Угадывай!")
            while True:
                your_number = int(input("Как ты думаешь какое это число "))
                attempts=attempts+1

                if attempts == 25:
                    print(f"Ты проиграл твоих попыток слишком много 25 число было {number}!")
                    attempts = 0
                    break
                elif your_number > number:
                    print("Число компьютера меньше!")
                elif your_number < number:
                    print("Число компьютера больше!")
                else:
                    print(f"Поздравляю! Угадал за {attempts} попыток")
                    points=points+5
                    print(f"Теперь у тебя {points} очков!")
                    attempts = 0
                    break
        
        elif choise == 2:
            break

        else:
            print("Выбери 1 или 2")
            continue
    
    elif choise1 == 4:
        print("Начать игру-1\nЗакончить игру-2")
        choise = int(input("Ваш выбор: "))

        if choise ==1:
            number = random.randint(1,10000)
            print("Я загадал рандомное число от 1 до 10000. Угадывай!")
            while True:
                your_number = int(input("Как ты думаешь какое это число "))
                attempts=attempts+1

                if attempts == 2500:
                    print(f"Ты проиграл твоих попыток слишком много 2500 число было {number}!")
                    attempts = 0
                    break
                elif your_number > number:
                    print("Число компьютера меньше!")
                elif your_number < number:
                    print("Число компьютера больше!")
                else:
                    print(f"Поздравляю! Угадал за {attempts} попыток")
                    points=points+10000
                    print(f"Теперь у тебя {points} очков!")
                    attempts = 0
                    break
        
        elif choise == 2:
            break

        else:
            print("Выбери 1 или 2")
            continue
    elif choise1 == 0:
        break