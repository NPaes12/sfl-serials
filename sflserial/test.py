import string

def valid_chars():
    """Return a list of characters which can be used in this serial number schema:

    - Allow uppercase alphanumeric characters
    - Exclude '0' and 'O' characters

    This list of characters also specifies the 'increment' order
    """

    allowed = string.digits + string.ascii_uppercase

    # The following characters are explicitly disallowed in the schema
    disallowed = 'O0'

    for c in disallowed:
        idx = allowed.index(c)
        allowed = allowed[:idx] + allowed[idx + 1:]

    return allowed

def convert_serial_to_int(serial):
    """Convert a serial number (string) to an integer representation.
    Iterate through each character, and if we find a "weird" character, simply return None
    """

    num = 0

    valid = valid_chars()
    N = len(valid)

    # Reverse iterate through the serial number string
    for idx, c in enumerate(serial[::-1]):
        if c not in valid:
            # An invalid character, not sure how to continue
            # Also, should not ever get here due to validate_serial_number routine
            return None

        c_int = valid.index(c) + 1
        c_int *= (N ** idx)

        num += c_int
    #num = int(serial, base=16)

    return num

def convert_serial_to_int_new(serial):
    """Convert a serial number (string) to an integer representation.
    Iterate through each character, and if we find a "weird" character, simply return None
    """
    num = int(serial, base=16)

    return num


def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""

    base36 = ''

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return base36

def increment_serial_number(serial):

    # Iterate to next serial number
    next_num = int(serial, base=36) + 1
    #output = hex(next_num)
    output = base36encode(next_num)
    #output = output[2:]
    #output = output.upper()

    # Validate
    valid = valid_chars()
    invalid_flag = 0

    while 1:
        for c in output:
            # if a char is not in the valid character list, it is not valid we need to go to the next serial number
            if c not in valid:
                invalid_flag = 1

        if invalid_flag == 1:
            next_num = int(output, base=36) + 1
            #output = hex(next_num)
            output = base36encode(next_num)
            #output = output[2:]
            invalid_flag = 0
        else:
            return output

#number = convert_serial_to_int("AAA")
#print(number)
#number = convert_serial_to_int_new("AAA")
#print(number)

sn = increment_serial_number("A")
print(sn)