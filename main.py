# Cam Abaqueta
#function is given a password entered by the user and adds 3 to each digit in the password
def encoder(password):
    encoded_message = ''
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_message += new_digit
    return encoded_message

#function does the opposite of the encoder and subtracts 3 from every digit entered

def decoder(encoded_password):
    password = ""
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        password += new_digit
    return password

#main logic
if __name__ == '__main__':
    menu_continue = True
    while menu_continue:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            #decoder function is optional since you can just use the original password entered by the user
            decoded_password = decoder(encoded_password)
            print('The encoded password is', encoded_password, ', and the original password is', decoded_password, ".")
        elif option == 3:
            break
