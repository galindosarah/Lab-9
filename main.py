# Sarah Galindo
def encode(password):
    if len(password) == 8:
        og_password_digit_list = []
        encoded_password_string = ""
        og_password_digit_list[:] = password
        for digit in og_password_digit_list:
            digit = int(digit)
            digit += 3
            digit = str(digit)
            encoded_password_string += digit
        return encoded_password_string


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