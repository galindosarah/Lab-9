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
