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

# Sophia Pinkston
def decode(encoded_password):
	encoded_password_list = []
	original_password_str = ""
	encoded_password_list[:] = encoded_password
	for element in encoded_password_list:
		element = int(element)
		element -= 3
		element = str(element)
		original_password_str += element
	return original_password_str
# fixed spelling error in encode, and added in the lines that save the passwords in order to use the f string's 
def main():
    while True:
        password = ""
        print("Menu \n-------------")
        print("1. Encode \n2. Decode \n3. Quit")
        print()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        elif user_input == 3:
            break


if __name__ == "__main__":
    main()
