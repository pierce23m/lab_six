

def password_encoder(password):
    encoded_password = ""
    for digit in password:
        # Convert the digit to an integer, add 3, and take the remainder divided by 10
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("EXit")
        selection = int(input("Please enter an option: "))
        if selection == 1:
            password = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
            passcode_encoded = password_encoder(password)
        elif selection == 2:
            print(f"The encoded password is {passcode_encoded}, and the original password is {password}. ")
            exit()
        elif selection == 3:
            exit()






