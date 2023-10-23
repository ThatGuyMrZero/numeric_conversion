def hex_char_decode(digit):
    digit = digit.lower()
    hex_chars = "0123456789abcdef"
    if digit in hex_chars:
        return hex_chars.index(digit)
    else:
        return None


def hex_string_decode(hex_string):
    hex_string = hex_string.lower().lstrip("0x")
    decimal_value = 0

    for digit in hex_string:
        digit_value = hex_char_decode(digit)
        if digit_value is not None:
            decimal_value = decimal_value * 16 + digit_value
        else:
            return None

    return decimal_value


def binary_string_decode(binary_string):
    binary_string = binary_string.lstrip("0b")  # Remove the "0b" prefix if present
    decimal_value = 0

    for digit in binary_string:
        if digit == '0':
            decimal_value = decimal_value * 2
        elif digit == '1':
            decimal_value = decimal_value * 2 + 1
        else:
            return None

    return decimal_value


def binary_to_hex(binary_string):
    decimal_value = binary_string_decode(binary_string)
    if decimal_value is not None:
        hex_result = hex(decimal_value).rstrip("L").lstrip("0x")
        return hex_result.upper().zfill((len(hex_result) + 3) // 4 * 4)[1:]
    else:
        return None


if __name__ == '__main__':
    while True:
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        print()

        choice = input("Please enter an option: ")

        if choice == "1":
            hex_string = input("Please enter the numeric string to convert: ")
            decoded_value = hex_string_decode(hex_string)
            if decoded_value is not None:
                print(f"Result: {decoded_value}")
                print()
            else:
                print("Invalid hexadecimal input.")
                print()
        elif choice == "2":
            binary_string = input("Please enter the numeric string to convert: ")
            decoded_value = binary_string_decode(binary_string)
            if decoded_value is not None:
                print(f"Result: {decoded_value}")
                print()
            else:
                print("Invalid binary input.")
                print()
        elif choice == "3":
            binary_string = input("Please enter the numeric string to convert: ")
            hex_result = binary_to_hex(binary_string)
            if hex_result is not None:
                print(f"Result: {hex_result}")
                print()
            else:
                print("Invalid binary input.")
                print()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
