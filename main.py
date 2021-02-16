from caesar_cipher import encrypted_message


message = input('Enter your message:')
shift_key = int(input('Enter your key:'))


print(encrypted_message(message, shift_key))