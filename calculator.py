import time

while True:


    print("Please choose an operator:")
    print("""
        1- Addition
        2- Subtraction
        3- Multiplication
        4- Divison""")

    prompt = int(input('Type your prompt here: '))

    if prompt == 1:
        a = float(input('first number: '))
        b = float(input('second number: '))
        print(a + b)
        time.sleep(2)

    elif prompt == 2:
        a = float(input('first number: '))
        b = float(input('second number: '))
        print(a - b)
        time.sleep(2)

    elif prompt == 3:
        a = float(input('first number: '))
        b = float(input('second number: '))
        print(a * b)
        time.sleep(2)

    elif prompt == 4:
        a = float(input('first number: '))
        b = float(input('second number: '))
        print(a / b)
        time.sleep(2)

    else:
        print('Please choose a number between (1 - 4)')
        time.sleep(2)

