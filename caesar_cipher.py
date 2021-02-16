def encrypted_message(new_message, key):
    secret_message = ""

    for i in range(len(new_message)):
        if new_message[i].isupper():
            secret_message = secret_message + chr((ord(new_message[i]) + key - 65) % 26 + 65)

        elif new_message[i].islower():
            secret_message = secret_message + chr((ord(new_message[i]) + key - 97) % 26 + 97)

        elif new_message[i].isdigit():
            sym_new = (int(new_message[i]) + key) % 10
            secret_message += str(sym_new)

        else:

            secret_message += new_message[i]

    return secret_message
