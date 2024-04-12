# Sarah Galindo


from encoder import encode


def main():
    while True:
        password = ""
        print("Menu \n-------------")
        print("1. Encode \n2. Decode \n3. Quit")
        print()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to enocde: ")
            encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == 2:
            #decode()
            print(f"The encoded password is , and the original password is {password}")
        elif user_input == 3:
            break


if __name__ == "__main__":
    main()