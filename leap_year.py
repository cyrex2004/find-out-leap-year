import time

print("Find out leap year.")

while True:
    user_input = input("Enter the year (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Bye Bye.")
        break

    if user_input.isdigit():
        year = int(user_input)

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("It is a leap year.")
                else:
                    print("It's not a leap year.")
            else:
                print("It is a leap year.")
        else:
            print("It's not a leap year.")
    else:
        print("Invalid input. Please enter a valid year.")
    
    time.sleep(2)
