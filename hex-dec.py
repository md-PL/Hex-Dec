"""
Pyton3.13.3
Simple converter from hex numbers to decimal ones
"""


def hex_to_dec_digit(digit_f: str):
    """ Summary:
    Function name:
        dec_to_hex_digit
    Inputs:
        - digit_f: int
    Description:
        The dec->hex partial digit conversion
    """
    dec_digit: int
    match digit_f:
        case "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9":
            dec_digit = int(digit_f)
        case "a":
            dec_digit = 10
        case "b":
            dec_digit = 11
        case "c":
            dec_digit = 12
        case "d":
            dec_digit = 13
        case "e":
            dec_digit = 14
        case "f":
            dec_digit = 15
    return dec_digit


def h_d_convert(number: str):
    """ Summary:
    Function name:
        h_d_convert
    Inputs:
        - number: str
    Description:
        The actual hex->dec conversion
    """
    result_f: int = 0
    length = len(number)
    #
    for i in range(length, 0, -1):
        value: int = hex_to_dec_digit(number[0])
        #
        result_f += value * (16 ** (i - 1))
        #
        number = number[1:]
        i -= 1
    #
    return result_f


def d__hex_dec_conversion():
    """ Summary:
    Function name:
        d__hex_dec_conversion
    Description:
        Converts an inputted hex number into decimal form
    """
    print("\thex -> dec")
    print("Insert a hexadecimal number:")
    #
    user_input_f = input("> ").casefold()
    #
    result_f: str = h_d_convert(user_input_f)
    return result_f


#==============================================================


def dec_to_hex_digit(digit_f: int):
    """ Summary:
    Function name:
        dec_to_hex_digit
    Inputs:
        - digit_f: int
    Description:
        The dec->hex partial digit conversion
    """
    hex_digit_f: str
    match digit_f:
        case 0|1|2|3|4|5|6|7|8|9:
            hex_digit_f = str(digit_f)
        case 10:
            hex_digit_f = "a"
        case 11:
            hex_digit_f = "b"
        case 12:
            hex_digit_f = "c"
        case 13:
            hex_digit_f = "d"
        case 14:
            hex_digit_f = "e"
        case 15:
            hex_digit_f = "f"
    return hex_digit_f


def d_h_convert(number: int):
    """ Summary:
    Function name:
        d_h_convert
    Inputs:
        - number: int
    Description:
        The actual dec->hex conversion
    """
    result_f: str = ""
    remainder_division: bool = True
    #
    while remainder_division:
        quotient: int = int(number / 16)
        remainder: int = number % 16
        #
        number = quotient
        hex_digit = dec_to_hex_digit(remainder)
        #
        result_f = hex_digit + result_f
        #
        if quotient == 0:
            remainder_division = False
    result_f = result_f.upper()
    return result_f


def h__dec_hex_conversion():
    """ Summary:
    Function name:
        h__dec_hex_conversion
    Description:
        Converts an inputted decimal number into hex form
    """
    print("\tdec -> hex")
    print("Insert a decimal number:")
    #
    user_input_f = int(input("> "))
    #
    result_f: str = d_h_convert(user_input_f)
    return result_f


#==============================================================


def main():
    """ Summary:
    Function name:
        main
    Description:
        Runs the program on repeat until user chooses to quit
    """
    print("""
        Type q or quit
            -> exit the app


        Type d or dec or decimal
            -> convert a [hexadecimal] number into a [decimal] number

        Type h or hex or hexadecimal
            -> convert a [decimal] number into a [hexadecimal] number
    """)
    convert: bool = True
    while convert:
        user_input = input("> ").casefold()
        result: str = ""
        #
        match user_input:
            case "q"|"quit":
                convert = False
                print()
                break
            case "d"|"dec"|"decimal":
                result = d__hex_dec_conversion()
            case "h"|"hex"|"hexadecimal":
                result = h__dec_hex_conversion()
            case _:
                pass
        #
        if result != "":
            print(f"\n\tresult = {result}\n")
    a = input()


#==============================================================


if __name__ == "__main__":
    main()
