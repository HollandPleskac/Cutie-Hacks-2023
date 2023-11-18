import random
user_input = input("What level of school are you in? Grade, Middle, High: ")
if user_input == "Grade":
    user_input = input("What subject would you like to learn about? Math, Science, English: ")
    if user_input == "Math":
        user_input = input("What topic would you like to learn? times tables, add/sub, fractions: ")
        if user_input == "times tables":
            while True:
                num1 = random.randint(0,13)
                num2 = random.randint(0,13)
                product = num1*num2
                print(f'Practice: \nwhat is {num1}x{num2}?: ')
                user_input = int(input())
                if user_input == product:
                    print("nice!")
                    user_output = input("Would you like to practice again? type y/n: ")
                    if user_output == 'n':
                        break
                elif user_input != product:
                    print(f'Try Again:')
                    user_input = input("Would you like to practice again? type y/n: ")
                if user_input == 'n':
                    break

                elif user_input != product:
                    print(f'Try Again:')
            print('Heres a link to a worksheet with more multiplication practice: https://tinyurl.com/kp92jf22')
        #next category
        if user_input == "add/sub":
            while True:
                num1 = random.randint(0,31)
                num2 = random.randint(0,31)
                operation = random.choice(['+', '-'])
                if operation == '+':
                    sum = num1 + num2
                else:
                    sum = num1 - num2
                result = num1;sum;num2
                print(f'Practice:\n what is {num1}{operation}{num2}?: ')
                user_input = int(input())
                if user_input == sum:
                    print("nice!")
                    user_output = input("Would you like to practice again? type y/n: ")
                    if user_output == 'n':
                        break
                elif user_input != sum:
                    print(f'Try Again:')
                    user_input = input("Would you like to practice again? type y/n: ")
                if user_input == 'n':
                    break
            print(f'Heres a link to a worksheet with more addition/subtraction practice: https://tinyurl.com/b6xdaper')
        #next category
        if user_input == 'fractions':
            print(f'Here are some videos that can help you understand more about fractions: https://tinyurl.com/5dzbrm99')
            print("Would you like more videos? y/n: ")
            user_input = input()
            if user_input == 'y':
                print('Here are some more videos:\n https://tinyurl.com/4c3enrch, https://tinyurl.com/2r5mdzjn')
        else:
            print('Have a nice day')
if user_input == "Middle":
    user_input = input("What topic would you like to learn? Geometry, Algebra: ")
    if user_input == "Geometry":
        while True:
            print(f'Geometry focuses on the unit circle, angles, and lengths')
            print('for a full geometry review please review the following video: \n https://tinyurl.com/bdehskpz')
            break
    if user_input == "Algebra":
        while True:
            x = random.randint(0,11)
            solution = (5*x)/2
            rounded_result = round(solution, 0)
            print(f'What is (5*{x})/2 round your answer to the nearest int: ')
            user_input = int(input())
            if user_input ==  rounded_result:
                print('nice!')
                user_output = input("Would you like to practice again? type y/n: ")
                if user_output == 'n':
                    break
            if user_input != solution:
                print(f'Try Again:')
                user_input = input("Would you like to practice again? type y/n: ")
        print(f'Heres a link to a worksheet with more Algebra practice:\nhttps://tinyurl.com/3vd7p6hn')
if user_input == "High":
    user_input = input("What topic would you like to learn? Trigonometry, Precalculus, Calculus,: ")
    if user_input == "Trigonometry":
        while True:
            print('Trigonometry is used to measure unkown angles and distances.\nRemember sin(x), cos(x), and tan(x) where x equals theata')
            print('all angles in any triange always add up to 180 degress.\nTry finding the unkown angles:')
            ang1 = random.randint(1,89)
            ang2 = random.randint(1,89)
            x = 180 - ang1 - ang2
            print(f'Find x given {ang1} and {ang2}: ')
            user_input = int(input())
            if user_input ==  x:
                print('nice!')
                user_output = input("Would you like to practice again? type y/n: ")
                if user_output == 'n':
                    break
            if user_input != x:
                print(f'Try Again:')
                user_input = input("Would you like to practice again? type y/n: ")
        print(f'Heres a link to a worksheet with more Algebra practice:\nhttps://tinyurl.com/ysfx7aub')
        print(f"When you're more familar with trigonometry, try practice problems: https://tinyurl.com/4h7wr4ce ")
    if user_input == "Precalculus":
        print("Once you're more familiar with Trignometry, try applyings trig identities and operations to solve Precalculus level problems.\nHeres a link to learn more: https://tinyurl.com/2dpvcead ")
    if user_input == "Calculus": 
        print('For calculus review watch the following video: https://www.youtube.com/watch?v=WmBzmHru78w')
else:
    print('Wrong input')