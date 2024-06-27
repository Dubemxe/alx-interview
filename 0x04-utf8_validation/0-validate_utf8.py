#!/usr/bin/python3
'''
Module for UTF-8 Validation
'''


def validUTF8(data):
    """
    Confirms if a given data set represents a valid
    UTF-8 encoding """
    num_bytes = 0

    code_1 = 1 << 7
    code_2 = 1 << 6

    for i in data:

        encode_byte = 1 << 7

        if num_bytes == 0:

            while encode_byte & i:
                num_bytes += 1
                encode_byte = encode_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (i & code_1 and not (i & code_2)):
                    return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
